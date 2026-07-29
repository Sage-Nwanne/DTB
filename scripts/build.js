import {
  cpSync,
  existsSync,
  mkdirSync,
  readdirSync,
  readFileSync,
  rmSync,
  statSync,
  writeFileSync,
} from "node:fs";
import { extname, join, resolve, relative } from "node:path";
import { siteFooter, siteHeader } from "./templates.js";

const root = resolve(process.cwd());
const publicDir = resolve(root, "public");
const distDir = resolve(root, "dist");
const maxWorkerAssetSize = 25 * 1024 * 1024;
const skippedFiles = [];

if (!existsSync(publicDir)) {
  console.error("Build failed: public/ directory was not found.");
  process.exit(1);
}

rmSync(distDir, { recursive: true, force: true });
mkdirSync(distDir, { recursive: true });

cpSync(publicDir, distDir, {
  recursive: true,
  filter: (source) => {
    const stats = statSync(source);

    if (stats.isFile() && stats.size > maxWorkerAssetSize) {
      skippedFiles.push(relative(publicDir, source));
      return false;
    }

    return true;
  },
});

function walk(directory) {
  return readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const location = join(directory, entry.name);
    return entry.isDirectory() ? walk(location) : [location];
  });
}

const requiredRoutes = [
  "index.html",
  "about/index.html",
  "blog/index.html",
  "contact/index.html",
  "privacy/index.html",
  "reviews/index.html",
  "services/index.html",
  "shawn/index.html",
  "terms/index.html",
  "works/index.html",
];

const requiredAssets = [
  "assets/icons.svg",
  "assets/site.js",
  "static/css/site.css",
  "static/Images/dtb-mark.png",
  "static/Images/dtb-favicon.png",
  "static/Images/dtb-header-circuit.png",
  "static/Images/DTB-LOGO-BACKGROUND.png",
  "static/Images/dtb-network-field.svg",
  "images/dtb-logo-transparent-full.png",
];

for (const requiredPath of [...requiredRoutes, ...requiredAssets]) {
  if (!existsSync(resolve(distDir, requiredPath))) {
    console.error(`Build failed: required output is missing: ${requiredPath}`);
    process.exit(1);
  }
}

for (const htmlFile of walk(distDir).filter((file) => extname(file) === ".html")) {
  const source = readFileSync(htmlFile, "utf8");
  const rendered = source
    .replace(/[ \t]*<!-- DTB_HEADER -->/, `\n${siteHeader}`)
    .replace(/[ \t]*<!-- DTB_FOOTER -->/, `\n${siteFooter}`);

  if (rendered.includes("<!-- DTB_HEADER -->") || rendered.includes("<!-- DTB_FOOTER -->")) {
    console.error(`Build failed: shell placeholder was not rendered in ${relative(distDir, htmlFile)}`);
    process.exit(1);
  }

  writeFileSync(htmlFile, rendered);
}

console.log("Built DTB static assets into dist/ for Cloudflare Workers.");

if (skippedFiles.length) {
  console.warn("Skipped files larger than Cloudflare Workers' 25 MiB asset limit:");
  for (const file of skippedFiles) {
    console.warn(`- ${file}`);
  }
}
