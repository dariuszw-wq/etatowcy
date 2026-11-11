# Kontrola DNS — etatowcy.pl, 2026-11-05

Strona działa; do zakończenia wskazanej weryfikacji Search Console brakuje rekordu TXT.

| Obszar | Status | Uwagi |
|---|---|---|
| Hosting | GitHub Pages | Repozytorium https://github.com/dariuszw-wq/etatowcy; cztery rekordy A 185.199.108–111.153 |
| DNS | dhosting | ns1.dhosting.pl, ns2.dhosting.pl; panel https://dpanel.pl/domains/v/list/ |
| www | Poprawny | CNAME dariuszw-wq.github.io; przekierowanie na https://etatowcy.pl/ |
| HTTPS | Działa | Oba adresy HTTPS odpowiadają; HTTP przekierowuje na HTTPS |
| Poczta | MX i SPF obecne | mx-1.dpoczta.pl, mx-2.dpoczta.pl; SPF include:_mail.dhosting.pl; DKIM i DMARC niebadane |
| Search Console | Brak wskazanego TXT | Token odczytany z docs/audyt-seo-2026-09-22.md; zgodny z widocznym początkiem na zrzucie użytkownika. Bieżącego panelu Google nie odczytano. |
| Mapa witryny | HTTP 200 | https://etatowcy.pl/sitemap-index.xml wskazuje sitemap-0.xml; zgłoszenie w Google niesprawdzone |
| Indeksacja | Nieustalona | Wymaga dostępu do Search Console |

## Co zmieniłem

Nie zmieniano DNS ani strony. Zapisano tę notatkę.

## Co zostaje do zrobienia

W dhosting → Domeny → etatowcy.pl → Rekordy DNS dodać osobny rekord TXT dla domeny głównej, TTL domyślny (obecne rekordy: 900 s):

```text
google-site-verification=VF3RE7dSyHKm47EivNGskAWejGo81_v2Av1ideR_UfI
```

W dPanel wartość TXT wpisać w cudzysłowach, jeśli formularz tego wymaga. Nie usuwać istniejących rekordów Google ani pocztowych. Po publikacji i propagacji kliknąć Weryfikuj w Search Console na koncie wskazanym w poprzednim audycie: dariusz.w@kancelaria-trc.pl. Następnie zgłosić mapę witryny. Nie potwierdzono ukończenia weryfikacji.
