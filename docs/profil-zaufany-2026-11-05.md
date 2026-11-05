# Profil zaufany — publikacja 5 listopada 2026

Cel: etatowcy.pl, zgodnie z doprecyzowaniem wydawcy. Języki projektu: PL, EN, ES.
Punkt przywrócenia sprzed zmian: commit `87a88d29c89907b74eca03290a9bd66e3e6b6270`.

## Pochodzenie danych

- Instrukcja: https://cosc.org.pl/artykul-profil-zaufany-cudzoziemiec-instrukcja.html
- Baza: https://cosc.org.pl/punkty-potwierdzajace-profil-zaufany.html
- Zachowana data danych źródłowych: 2026-11-05.
- Nie pobierano nowej listy z pz.gov.pl. Zachowano wszystkie 2293 unikalne identyfikatory, nazwy, miejscowości, województwa, adresy, 922 uwagi, 2293 adresy map i 399 adresów rezerwacji.
- Suma SHA-256 źródłowego HTML zapisana w `src/data/trusted-profile-points.json`.
- Nazwy placówek, adresy i uwagi pozostają w oryginale we wszystkich językach; przetłumaczono interfejs i instrukcję.
- Ilustracja: biblioteka COSC, `https://cosc.org.pl/img/urzad-punkt-obslugi-cudzoziemca.jpg`, podpisana jako ilustracja AI.

## Weryfikacja instrukcji

Sprawdzono oficjalne FAQ https://www.gov.pl/web/profilzaufany/najczesciej-zadawane-pytania2: PESEL, minimum 13 lat, zdolność do czynności prawnych, bezpłatność, bank, dokumenty w punkcie, dowolność wyboru placówki, warunki wideorozmowy, ważność 3 lata, pomoc techniczna. Bieżące wskazówki dotyczące braku SMS opisano zgodnie z FAQ.

Odczytano urzędowy tekst Dz.U. 2023 poz. 2551 oraz nowelizacje Dz.U. 2025 poz. 831 i Dz.U. 2026 poz. 482 z api.sejm.gov.pl. Potwierdzono termin 30 dni (§ 3 ust. 2), osobistą wizytę i weryfikację (§ 4), ważność 3 lata (§ 11). Nowelizacja z 2026 r. zmienia § 10, nie wskazane terminy.

## Kontrola przed publikacją

- Produkcyjny build Astro: 140 stron, bez błędów.
- `python scripts/verify-trusted-profile.py`: porównanie każdego rekordu z importem w trzech wersjach HTML; 6/6 nowych stron, poprawne canonical/hreflang, metadane, dane strukturalne, linki i mapa witryny.
- Wyszukiwanie w przeglądarce: „Lodz” 41 wyników, razem z łódzkim 29; nieistniejący punkt 0; reset 2293. „Warszawa” 35. EN „Gdansk” 32. ES filtr pomorskie 133.
- Brak błędów konsoli podczas testu PL.
- Mobilne 390 px: artykuł i baza bez poziomego przepełnienia; formularz w jednej kolumnie.
- Wszystkie rekordy są w statycznym HTML. Bez JS lista działa poprzez natywne rozwijane sekcje województw.
- Stałe linki na stronach głównych i listach „Rynek pracy” oraz w globalnej stopce.

## Google Search Console

Nowe adresy zawiera automatycznie generowana mapa witryny. Ręczne zgłoszenie URL nie jest obowiązkowe; można poprosić o indeksowanie sześciu adresów przez Inspekcję URL. Nie oznacza to gwarancji ani natychmiastowego indeksowania. Jeśli mapa nie została wcześniej zgłoszona w usłudze, zgłosić `https://etatowcy.pl/sitemap-index.xml`. Nie wykonywano operacji na koncie GSC.
