#!/usr/bin/env node
/* Export an Obsidian-flavored Markdown note to PDF with Playwright.
 *
 * Install dependency when needed:
 *   npm install
 */

const fs = require("fs");
const path = require("path");
const { chromium } = require("playwright");
const { marked } = require("marked");

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function normalizeObsidianEmbeds(markdown) {
  return markdown.replace(/!\[\[([^|\]]+)(?:\|([^\]]+))?\]\]/g, (_, target, width) => {
    const safeTarget = target.trim();
    const alt = path.basename(safeTarget);
    const widthAttr = width && /^\d+$/.test(width.trim()) ? ` width="${width.trim()}"` : "";
    return `<img src="${escapeHtml(safeTarget)}" alt="${escapeHtml(alt)}"${widthAttr}>`;
  });
}

function stripObsidianImageWidth(markdown) {
  return markdown.replace(/!\[([^\]]*)\]\(([^)|]+)\|(\d+)\)/g, (_, alt, target, width) => {
    return `<img src="${escapeHtml(target.trim())}" alt="${escapeHtml(alt)}" width="${width}">`;
  });
}

function resolveRelativeImages(html, baseDir) {
  return html.replace(/<img([^>]+)src="([^"]+)"/g, (match, attrs, src) => {
    if (/^(https?:|data:|file:)/.test(src)) return match;
    const absolute = path.resolve(baseDir, src);
    return `<img${attrs}src="file://${absolute.replace(/\\/g, "/")}"`;
  });
}

async function main() {
  const [noteArg, outArg] = process.argv.slice(2);
  if (!noteArg) {
    console.error("Usage: node export_obsidian_note_pdf.js <note.md> [output.pdf]");
    process.exit(2);
  }

  const notePath = path.resolve(noteArg);
  const outPath = path.resolve(outArg || notePath.replace(/\.md$/i, ".pdf"));
  const baseDir = path.dirname(notePath);
  const raw = fs.readFileSync(notePath, "utf8");
  const normalized = stripObsidianImageWidth(normalizeObsidianEmbeds(raw));
  const body = resolveRelativeImages(marked.parse(normalized), baseDir);

  const css = `
    body { font-family: "Segoe UI", Arial, sans-serif; line-height: 1.62; color: #111827; }
    main { max-width: 920px; margin: 0 auto; }
    h1, h2, h3 { line-height: 1.25; page-break-after: avoid; }
    h1 { font-size: 30px; border-bottom: 2px solid #dbeafe; padding-bottom: 10px; }
    h2 { margin-top: 34px; color: #1f2937; }
    img { max-width: 100%; display: block; margin: 16px auto; border: 1px solid #e5e7eb; border-radius: 8px; }
    blockquote { border-left: 4px solid #2563eb; background: #f8fafc; margin: 16px 0; padding: 10px 16px; }
    table { width: 100%; border-collapse: collapse; font-size: 13px; }
    th, td { border: 1px solid #e5e7eb; padding: 8px; vertical-align: top; }
    code { background: #f3f4f6; padding: 2px 4px; border-radius: 4px; }
    pre code { display: block; padding: 12px; white-space: pre-wrap; }
  `;

  const html = `<!doctype html><html><head><meta charset="utf-8"><style>${css}</style></head><body><main>${body}</main></body></html>`;

  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setContent(html, { waitUntil: "networkidle" });
  await page.pdf({ path: outPath, format: "A4", printBackground: true, margin: { top: "18mm", bottom: "18mm", left: "16mm", right: "16mm" } });
  await browser.close();
  console.log(`Wrote ${outPath}`);
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
