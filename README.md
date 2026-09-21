# Etatowcy — strona agencji pracy

Astro (statyczny HTML) · PL / EN / ES · GitHub Pages.

- System projektowy (tokeny, komponenty, logo): Claude Design — https://claude.ai/artifact/RD6BWzW5sNPbHdZDQ9QX1X
- Oferty pracy: `src/content/jobs/<pl|en|es>/<slug>.md` (ten sam slug w trzech językach = ta sama oferta)
- Wiadomości: `src/content/news/<pl|en|es>/<slug>.md`
- Teksty interfejsu: `src/i18n/ui.ts` · dane kontaktowe: `src/config.ts`

## Praca lokalna

```bash
npm install
npm run dev      # http://localhost:4321/etatowcy/
npm run build    # dist/
```

## Wdrożenie

Każdy push na `main` buduje i publikuje stronę (GitHub Actions → Pages).
Przy podpinaniu domeny ustaw zmienne repozytorium `SITE_URL=https://etatowcy.pl` i `SITE_BASE=/` oraz dodaj `public/CNAME`.
