import assert from "node:assert/strict";
import { mkdtemp, mkdir, rm, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";

import { validateInternalLinks } from "./check-site-links.mjs";

test("validates emitted pages, assets, and anchors", async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), "site-links-"));
  try {
    await mkdir(path.join(directory, "about"), { recursive: true });
    await writeFile(
      path.join(directory, "index.html"),
      '<a href="/about/#details">About</a><img src="/asset.svg">',
    );
    await writeFile(
      path.join(directory, "about", "index.html"),
      '<main id="details"><a href="/">Home</a></main>',
    );
    await writeFile(path.join(directory, "asset.svg"), "<svg></svg>");

    const result = await validateInternalLinks(directory);
    assert.deepEqual(result, { pages: 2, links: 3 });
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

test("reports the source page and broken target", async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), "site-links-"));
  try {
    await writeFile(path.join(directory, "index.html"), '<a href="/missing/">Missing</a>');
    await assert.rejects(
      validateInternalLinks(directory),
      /index\.html: missing target \/missing\//,
    );
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});

test("accepts Astro's special 404.html output for the /404/ route", async () => {
  const directory = await mkdtemp(path.join(os.tmpdir(), "site-links-"));
  try {
    await writeFile(path.join(directory, "404.html"), '<link href="/404/">');
    const result = await validateInternalLinks(directory);
    assert.deepEqual(result, { pages: 1, links: 1 });
  } finally {
    await rm(directory, { recursive: true, force: true });
  }
});
