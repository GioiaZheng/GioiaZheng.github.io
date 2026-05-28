import { defineConfig } from "astro/config";

// Deployed to https://gioiazheng.github.io/ (user pages).
// Keep `base: "/"` — switching to a project-pages repo would require updating
// `base` and `site` to match.
export default defineConfig({
  site: "https://gioiazheng.github.io",
  base: "/",
  trailingSlash: "ignore",
  build: {
    format: "directory",
  },
});
