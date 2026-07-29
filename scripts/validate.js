import { existsSync, readFileSync, readdirSync } from "node:fs";
import { extname, join, relative, resolve } from "node:path";

const root = resolve(process.cwd(), "dist");
const failures = [];

function walk(directory) {
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const location = join(directory, entry.name);
    return entry.isDirectory() ? walk(location) : [location];
  });
}

const htmlFiles = walk(root).filter((file) => file.endsWith(".html"));
const stylesheetPath = join(root, "static/css/site.css");
const legacyPatterns = [
  /static\/css\/dist\/styles\.css/i,
  /href="#"/i,
  /developer name/i,
  /\[placeholder\]/i,
  /trusted by business owners at companies like/i,
  /DTB_logo\.png/i,
  /DTB-banner-removebg-preview/i,
  /brand-strike/i,
  /circuit-wash/i,
  /hero-grid/i,
];

if (!existsSync(stylesheetPath)) {
  failures.push("static/css/site.css: shared stylesheet missing");
} else {
  const stylesheet = readFileSync(stylesheetPath, "utf8");
  const visualRegressionPatterns = [
    [/background-repeat:\s*repeat/i, "tiled background treatment"],
    [/logo-background-image-resized/i, "legacy raster background"],
    [/brand-strike/i, "legacy headline strike effect"],
  ];

  for (const [pattern, label] of visualRegressionPatterns) {
    if (pattern.test(stylesheet)) failures.push(`static/css/site.css: ${label} is still present`);
  }
}

for (const file of htmlFiles) {
  const html = readFileSync(file, "utf8");
  const page = relative(root, file);

  for (const pattern of legacyPatterns) {
    if (pattern.test(html)) failures.push(`${page}: legacy or placeholder content matched ${pattern}`);
  }

  if (!["sage/index.html", "devs/index.html"].includes(page)) {
    if (!html.includes('<header class="site-header"')) failures.push(`${page}: shared header missing`);
    if (!html.includes('<footer class="site-footer"')) failures.push(`${page}: shared footer missing`);
    if (!html.includes('/static/css/site.css')) failures.push(`${page}: shared stylesheet missing`);
  }

  for (const match of html.matchAll(/(?:href|src)="([^"]+)"/g)) {
    const value = match[1];
    if (/^(https?:|mailto:|tel:|#)/.test(value)) continue;

    const [pathname, fragment] = value.split("#");
    const cleanPath = pathname.split("?")[0];
    let target = join(root, cleanPath.replace(/^\//, ""));

    if (cleanPath.endsWith("/") || extname(target) === "") {
      target = join(target, "index.html");
    }

    if (!existsSync(target)) {
      failures.push(`${page}: missing target ${value}`);
      continue;
    }

    if (fragment && target.endsWith(".html")) {
      const targetHtml = readFileSync(target, "utf8");
      const fragmentPattern = new RegExp(`id=["']${fragment}["']`);
      if (!fragmentPattern.test(targetHtml)) {
        failures.push(`${page}: missing fragment #${fragment} in ${relative(root, target)}`);
      }
    }
  }
}

if (failures.length) {
  console.error("DTB validation failed:");
  failures.forEach((failure) => console.error(`- ${failure}`));
  process.exit(1);
}

console.log(`Validated ${htmlFiles.length} routes, shared shell, local targets, and DTB visual-regression rules.`);
