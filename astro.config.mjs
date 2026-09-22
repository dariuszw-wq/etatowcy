// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// Lokalnie: base /etatowcy (jak dawny adres testowy); produkcja: zmienne SITE_URL/SITE_BASE w GitHub Actions
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
      // Root bez języka (`/`) ma noindex i przekierowuje — do mapy trafiają tylko adresy kanoniczne.
      filter: (page) => page !== new URL(BASE, SITE).href,
      // Kody języków takie same jak hreflang w <head> (Base.astro): pl / en / es.
      i18n: { defaultLocale: 'pl', locales: { pl: 'pl', en: 'en', es: 'es' } },
    }),
  ],
  build: { inlineStylesheets: 'auto' },
  prefetch: { prefetchAll: true, defaultStrategy: 'viewport' },
});
