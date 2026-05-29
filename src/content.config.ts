import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const projects = defineCollection({
  loader: glob({ base: "./src/content/projects", pattern: "**/*.md" }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    order: z.number().default(99),
    featured: z.boolean().default(false),
    status: z
      .enum(["active", "maintained", "experimental", "archived"])
      .default("active"),
    last_updated: z.string().optional(),
    repo: z.string().url().optional(),
    tags: z.array(z.string()).default([]),
  }),
});

const writing = defineCollection({
  loader: glob({ base: "./src/content/writing", pattern: "**/*.md" }),
  schema: z.object({
    title: z.string(),
    summary: z.string(),
    date: z.string().optional(),
    status: z.enum(["draft", "planned", "published"]).default("planned"),
    order: z.number().default(99),
  }),
});

export const collections = { projects, writing };
