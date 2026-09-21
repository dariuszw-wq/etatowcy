// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Etap 1 (test): GitHub Pages pod https://dariuszw-wq.github.io/etatowcy/
// Etap 2 (domena): SITE_URL=https://etatowcy.pl SITE_BASE=/ + plik public/CNAME
const SITE = process.env.SITE_URL || 'https://dariuszw-wq.github.io';
const BASE = process.env.SITE_BASE || '/etatowcy';

export default defineConfig({
  site: SITE,
  base: BASE,
  trailingSlash: 'always',
  i18n: {
    defaultLocale: 'pl',
    locales: ['pl', 'en', 'es'],
    routing: { prefixDefaultLocale: true },
  },
  integrations: [
    sitemap({
      i18n: { defaultLocale: 'pl', locales: { pl: 'pl-PL', en: 'en', es: 'es' } },
    }),
  ],
  build: { inlineStylesheets: 'auto' },
  prefetch: { prefetchAll: true, defaultStrategy: 'viewport' },
});
