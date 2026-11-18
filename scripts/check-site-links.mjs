import { readFile, readdir, stat } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { fileURLToPath, pathToFileURL } from "node:url";

const SITE_ORIGIN = "https://gioiazheng.github.io";
const SKIPPED_SCHEMES = /^(?:data|mailto|tel|javascript):/i;

async function walkFiles(root, predicate) {
  const files = [];

  async function visit(directory) {
    for (const entry of await readdir(directory, { withFileTypes: true })) {
      const absolute = path.join(directory, entry.name);
      if (entry.isDirectory()) {
        await visit(absolute);
      } else if (predicate(absolute)) {
        files.push(absolute);
      }
    }
  }

  await visit(root);
  return files;
}

function decodeHtmlAttribute(value) {
  return value
    .replaceAll("&amp;", "&")
    .replaceAll("&quot;", '"')
    .replaceAll("&#39;", "'")
    .replaceAll("&lt;", "<")
    .replaceAll("&gt;", ">");
}

function pageUrlForFile(file, distDir) {
  const relative = path.relative(distDir, file).split(path.sep).join("/");
  if (relative === "index.html") return new URL("/", SITE_ORIGIN);
  if (relative.endsWith("/index.html")) {
    return new URL(`/${relative.slice(0, -"index.html".length)}`, SITE_ORIGIN);
  }
  return new URL(`/${relative}`, SITE_ORIGIN);
}

function candidateTargets(pathname, distDir) {
  const decoded = decodeURIComponent(pathname);
  const relative = decoded.replace(/^\/+/, "");
  const direct = path.join(distDir, relative);

  if (decoded.endsWith("/")) {
    return [path.join(direct, "index.html"), `${direct.replace(/[\\/]$/, "")}.html`];
  }
  if (path.extname(decoded)) return [direct];
  return [direct, `${direct}.html`, path.join(direct, "index.html")];
}

async function firstExisting(paths) {
  for (const candidate of paths) {
    try {
      if ((await stat(candidate)).isFile()) return candidate;
    } catch (error) {
      if (error.code !== "ENOENT") throw error;
    }
  }
  return null;
}

function extractAttributes(html) {
  const values = [];
  const pattern = /\b(?:href|src)\s*=\s*(["'])(.*?)\1/gi;
  for (const match of html.matchAll(pattern)) {
    values.push(decodeHtmlAttribute(match[2].trim()));
  }
  return values;
}

function extractAnchors(html) {
  const anchors = new Set();
  const pattern = /\b(?:id|name)\s*=\s*(["'])(.*?)\1/gi;
  for (const match of html.matchAll(pattern)) {
    anchors.add(decodeHtmlAttribute(match[2]));
  }
  return anchors;
}

export async function validateInternalLinks(distDir) {
  const absoluteDist = path.resolve(distDir);
  const htmlFiles = await walkFiles(absoluteDist, (file) => file.endsWith(".html"));
  const errors = [];
  const anchorCache = new Map();
  let checked = 0;

  for (const sourceFile of htmlFiles) {
    const html = await readFile(sourceFile, "utf8");
    const sourceUrl = pageUrlForFile(sourceFile, absoluteDist);

    for (const rawValue of extractAttributes(html)) {
      if (!rawValue || rawValue === "#" || SKIPPED_SCHEMES.test(rawValue)) continue;

      let targetUrl;
      try {
        targetUrl = new URL(rawValue, sourceUrl);
      } catch {
        errors.push(`${path.relative(absoluteDist, sourceFile)}: invalid URL ${rawValue}`);
        continue;
      }

      if (targetUrl.origin !== SITE_ORIGIN) continue;
      checked += 1;

      const targetFile = await firstExisting(candidateTargets(targetUrl.pathname, absoluteDist));
      if (!targetFile) {
        errors.push(
          `${path.relative(absoluteDist, sourceFile)}: missing target ${targetUrl.pathname}`,
        );
        continue;
      }

      if (targetUrl.hash && targetFile.endsWith(".html")) {
        const anchor = decodeURIComponent(targetUrl.hash.slice(1));
        if (!anchorCache.has(targetFile)) {
          anchorCache.set(targetFile, extractAnchors(await readFile(targetFile, "utf8")));
        }
        if (!anchorCache.get(targetFile).has(anchor)) {
          errors.push(
            `${path.relative(absoluteDist, sourceFile)}: missing anchor ${targetUrl.pathname}${targetUrl.hash}`,
          );
        }
      }
    }
  }

  if (errors.length) {
    throw new Error(`Internal link check failed:\n${errors.map((error) => `- ${error}`).join("\n")}`);
  }

  return { pages: htmlFiles.length, links: checked };
}

async function main() {
  const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
  const internal = await validateInternalLinks(path.join(root, "dist"));
  console.log(`Internal links OK: ${internal.links} links across ${internal.pages} pages.`);
}

const invokedAsScript =
  process.argv[1] && pathToFileURL(path.resolve(process.argv[1])).href === import.meta.url;

if (invokedAsScript) {
  main().catch((error) => {
    console.error(error.message);
    process.exitCode = 1;
  });
}
