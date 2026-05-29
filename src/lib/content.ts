import type { CollectionEntry } from "astro:content";

export function entrySlug(
  entry: CollectionEntry<"projects"> | CollectionEntry<"writing">,
) {
  return entry.id.replace(/\.mdx?$/, "");
}
