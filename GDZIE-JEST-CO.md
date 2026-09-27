# Etatowcy — gdzie jest co

**Ten folder (`D:\PROJEKTY\STRONY\Etatowcy`) jest miejscem pracy nad stroną.** Tu się edytuje, buduje i wypycha zmiany.

| | |
|---|---|
| Strona na żywo | https://etatowcy.pl |
| Kod (źródło prawdy) | https://github.com/dariuszw-wq/etatowcy — push na `main` = automatyczne wdrożenie (~1 min) |
| System projektowy | https://claude.ai/artifact/RD6BWzW5sNPbHdZDQ9QX1X (tokeny, komponenty, logo) |
| Kopia zapasowa | repozytorium GitHub (pełna historia). Innych kopii nie ma i nie tworzymy — ten folder jest jedyny. |

## Co gdzie leży

- `src/content/jobs/<pl|en|es>/<slug>.md` — oferty pracy (ten sam slug w trzech językach = ta sama oferta)
- `src/content/news/<pl|en|es>/<slug>.md` — artykuły „Rynek pracy"
- `src/i18n/ui.ts` — teksty interfejsu · `src/i18n/form.ts` — pytania kwestionariusza kontaktowego
- `src/config.ts` — e-mail, telefon, endpoint formularza
- `public/` — logo, fonty, favicon, obraz do social mediów
- `docs/tematy-opublikowane.md` — rejestr opublikowanych artykułów

## Codzienna praca

```bash
npm run dev
```

Publikacja: `npm run build` → commit → `git push origin main`.

## Zadania automatyczne

W aplikacji Claude, zakładka Code → sekcja **Scheduled**:
- **etatowcy-publikacja-artykulow** — dni robocze 9:00, pisze i publikuje artykuły „Rynek pracy"
- **etatowcy-monitor-tygodniowy** — cotygodniowa kontrola strony i indeksowania

Oba wskazują na ten folder. Przy zmianie lokalizacji projektu trzeba w nich poprawić ścieżkę.
