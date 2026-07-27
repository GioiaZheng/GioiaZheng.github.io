import { getCollection } from "astro:content";
import type { APIRoute } from "astro";
import { entrySlug } from "../lib/content";

const escapeXml = (value: string) =>
  value.replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll(">", "&gt;");

export const GET: APIRoute = async ({ site }) => {
  const base = site ?? new URL("https://gioiazheng.github.io");
  const projects = (await getCollection("projects"))
    .filter((entry) => entry.data.featured || entry.data.academic)
    .map((entry) => ({
      path: `/projects/${entrySlug(entry)}/`,
      lastmod: entry.data.last_updated,
    }));
  const writing = (await getCollection("writing"))
    .filter((entry) => entry.data.status === "published")
    .map((entry) => ({
      path: `/writing/${entrySlug(entry)}/`,
      lastmod: entry.data.date,
    }));
  const pages = [
    { path: "/" },
    { path: "/projects/" },
    { path: "/writing/" },
    { path: "/materials/" },
    { path: "/contact/" },
    ...projects,
    ...writing,
  ];
  const urls = pages
    .map(({ path, lastmod }) => {
      const location = escapeXml(new URL(path, base).toString());
      const modified = lastmod ? `<lastmod>${escapeXml(lastmod)}</lastmod>` : "";
      return `<url><loc>${location}</loc>${modified}</url>`;
    })
    .join("");

  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urls}</urlset>`,
    { headers: { "Content-Type": "application/xml; charset=utf-8" } },
  );
};
