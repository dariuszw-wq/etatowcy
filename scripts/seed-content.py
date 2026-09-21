# Generuje przykładowe oferty i wiadomości (PL/EN/ES). Uruchom: python scripts/seed-content.py
import os
ROOT = os.path.join(os.path.dirname(__file__), '..', 'src', 'content')

J = {
'operator-linii-produkcyjnej': {
 'pl': dict(title='Operator linii produkcyjnej', city='Poznań', industry='Produkcja', contract='Umowa o pracę', pay='32,50 zł / h brutto', terms='3 zmiany · zakwaterowanie · dowóz do zakładu', tags=['Od zaraz'], body="""## Czym będziesz się zajmować
- obsługa linii pakującej — podawanie komponentów, kontrola jakości,
- prosta rejestracja produkcji w systemie,
- utrzymanie porządku na stanowisku.

## Czego oczekujemy
- gotowość do pracy w systemie trzyzmianowym,
- dokładność i sumienność,
- **nie wymagamy doświadczenia** — szkolimy na miejscu.

## Co oferujemy
- 32,50 zł/h brutto + premia frekwencyjna,
- umowa o pracę od pierwszego dnia,
- zakwaterowanie w pokojach 2-osobowych, dowóz do zakładu,
- pomoc w formalnościach dla cudzoziemców (zezwolenie na pracę — dokument, który pozwala legalnie pracować w Polsce)."""),
 'en': dict(title='Production line operator', city='Poznań', industry='Manufacturing', contract='Employment contract', pay='32.50 PLN / h gross', terms='3 shifts · accommodation · transport to the plant', tags=['Immediate start'], body="""## What you will do
- operate the packing line — feeding components, quality checks,
- simple production logging in the system,
- keep the workstation tidy.

## What we expect
- availability for a three-shift system,
- accuracy and reliability,
- **no experience needed** — we train on site.

## What we offer
- 32.50 PLN/h gross + attendance bonus,
- employment contract from day one,
- accommodation in double rooms, transport to the plant,
- help with paperwork for foreign workers (zezwolenie na pracę — the document that lets you work legally in Poland)."""),
 'es': dict(title='Operario de línea de producción', city='Poznań', industry='Producción', contract='Contrato de trabajo', pay='32,50 PLN / h bruto', terms='3 turnos · alojamiento · transporte a la planta', tags=['Incorporación inmediata'], body="""## Qué harás
- manejar la línea de envasado — alimentar componentes, control de calidad,
- registro sencillo de la producción en el sistema,
- mantener el puesto ordenado.

## Qué esperamos
- disponibilidad para tres turnos,
- precisión y responsabilidad,
- **no se requiere experiencia** — formamos en el puesto.

## Qué ofrecemos
- 32,50 PLN/h bruto + prima de asistencia,
- contrato de trabajo desde el primer día,
- alojamiento en habitaciones dobles, transporte a la planta,
- ayuda con los trámites para extranjeros (zezwolenie na pracę — el permiso que te permite trabajar legalmente en Polonia)."""),
},
'pracownik-magazynu': {
 'pl': dict(title='Pracownik magazynu', city='Wrocław', industry='Logistyka', contract='Umowa zlecenie', pay='30,00 zł / h brutto', terms='od zaraz · UA / EN · elastyczny grafik', tags=['UA / EN'], body="""## Czym będziesz się zajmować
- kompletacja zamówień ze skanerem,
- rozładunek i załadunek palet (wózek ręczny),
- kontrola ilości i etykietowanie.

## Czego oczekujemy
- podstawowa znajomość polskiego, angielskiego lub ukraińskiego,
- sprawność fizyczna,
- mile widziane uprawnienia UDT na wózki widłowe (płacimy więcej).

## Co oferujemy
- 30 zł/h brutto, wypłata co dwa tygodnie,
- grafik do wyboru: dzień / noc / weekendy,
- możliwość przejścia na umowę o pracę po 3 miesiącach."""),
 'en': dict(title='Warehouse worker', city='Wrocław', industry='Logistics', contract='Civil contract (zlecenie)', pay='30.00 PLN / h gross', terms='immediate start · UA / EN · flexible schedule', tags=['UA / EN'], body="""## What you will do
- order picking with a scanner,
- unloading and loading pallets (hand pallet truck),
- quantity checks and labelling.

## What we expect
- basic Polish, English or Ukrainian,
- physical fitness,
- forklift licence (UDT) welcome — higher rate.

## What we offer
- 30 PLN/h gross, paid every two weeks,
- schedule of your choice: days / nights / weekends,
- switch to an employment contract after 3 months."""),
 'es': dict(title='Operario de almacén', city='Wrocław', industry='Logística', contract='Contrato civil (zlecenie)', pay='30,00 PLN / h bruto', terms='incorporación inmediata · UA / EN · horario flexible', tags=['UA / EN'], body="""## Qué harás
- preparación de pedidos con escáner,
- descarga y carga de palés (transpaleta manual),
- control de cantidades y etiquetado.

## Qué esperamos
- polaco, inglés o ucraniano básico,
- buena forma física,
- se valora carné de carretilla (UDT) — tarifa más alta.

## Qué ofrecemos
- 30 PLN/h bruto, pago cada dos semanas,
- horario a elegir: días / noches / fines de semana,
- paso a contrato de trabajo tras 3 meses."""),
},
'specjalista-ds-kadr': {
 'pl': dict(title='Specjalista ds. kadr i płac', city='Warszawa', industry='Biuro', contract='Umowa o pracę', pay='7 500 – 9 000 zł brutto', terms='hybrydowo · pełny etat · zespół 6 osób', tags=['Hybrydowo'], body="""## Czym będziesz się zajmować
- prowadzenie akt osobowych i naliczanie wynagrodzeń (ok. 250 osób),
- zgłoszenia ZUS, PIT, PPK,
- legalizacja zatrudnienia cudzoziemców — powiadomienia, zezwolenia, terminy.

## Czego oczekujemy
- min. 2 lata w kadrach i płacach,
- znajomość Płatnika i jednego z systemów kadrowych (Enova, Optima, Symfonia),
- angielski B1 — część pracowników nie mówi po polsku.

## Co oferujemy
- 7 500 – 9 000 zł brutto zależnie od doświadczenia,
- 2 dni w biurze (Warszawa-Mokotów), 3 zdalnie,
- prywatna opieka medyczna, szkolenia z prawa pracy."""),
 'en': dict(title='HR & payroll specialist', city='Warsaw', industry='Office', contract='Employment contract', pay='7,500 – 9,000 PLN gross', terms='hybrid · full-time · team of 6', tags=['Hybrid'], body="""## What you will do
- personnel files and payroll for c. 250 people,
- ZUS, PIT and PPK filings,
- legalising foreign employment — notifications, permits, deadlines.

## What we expect
- 2+ years in HR & payroll,
- Płatnik plus one HR system (Enova, Optima, Symfonia),
- English B1 — some employees do not speak Polish.

## What we offer
- 7,500 – 9,000 PLN gross depending on experience,
- 2 days in the office (Warsaw-Mokotów), 3 remote,
- private healthcare, labour-law training."""),
 'es': dict(title='Especialista en RR. HH. y nóminas', city='Varsovia', industry='Oficina', contract='Contrato de trabajo', pay='7 500 – 9 000 PLN bruto', terms='híbrido · jornada completa · equipo de 6', tags=['Híbrido'], body="""## Qué harás
- expedientes de personal y nóminas de unas 250 personas,
- declaraciones ZUS, PIT y PPK,
- legalización del empleo de extranjeros — notificaciones, permisos, plazos.

## Qué esperamos
- más de 2 años en RR. HH. y nóminas,
- Płatnik y un sistema de RR. HH. (Enova, Optima, Symfonia),
- inglés B1 — parte de la plantilla no habla polaco.

## Qué ofrecemos
- 7 500 – 9 000 PLN bruto según experiencia,
- 2 días en oficina (Varsovia-Mokotów), 3 en remoto,
- seguro médico privado, formación en derecho laboral."""),
},
'kierowca-ce': {
 'pl': dict(title='Kierowca C+E', city='Cała Polska', industry='Transport', contract='Umowa o pracę', pay='9 000 zł netto', terms='kraj i UE · nowe ciągniki · weekendy w domu', tags=['Kod 95'], body="""## Czym będziesz się zajmować
- przewozy plandeką na trasach Polska – Niemcy – Beneluks,
- 3 tygodnie w trasie / 1 tydzień w domu (możliwy system 2/1),
- obsługa tachografu i dokumentów przewozowych.

## Czego oczekujemy
- prawo jazdy C+E, kod 95, karta kierowcy,
- min. rok doświadczenia w przewozach międzynarodowych,
- komunikatywny angielski lub niemiecki.

## Co oferujemy
- 9 000 zł netto miesięcznie (podstawa + diety), terminowo,
- ciągniki nie starsze niż 3 lata,
- pomoc w uzyskaniu kodu 95 i karty kierowcy dla cudzoziemców."""),
 'en': dict(title='C+E truck driver', city='Nationwide', industry='Transport', contract='Employment contract', pay='9,000 PLN net', terms='Poland & EU · new tractors · weekends at home', tags=['Code 95'], body="""## What you will do
- curtain-sider haulage on Poland – Germany – Benelux routes,
- 3 weeks on the road / 1 week at home (2/1 possible),
- tachograph and transport documents.

## What we expect
- C+E licence, Code 95, driver card,
- 1+ year in international haulage,
- working English or German.

## What we offer
- 9,000 PLN net per month (base + per diems), paid on time,
- tractors no older than 3 years,
- help obtaining Code 95 and a driver card for foreign drivers."""),
 'es': dict(title='Conductor C+E', city='Toda Polonia', industry='Transporte', contract='Contrato de trabajo', pay='9 000 PLN neto', terms='Polonia y UE · tractoras nuevas · fines de semana en casa', tags=['Código 95'], body="""## Qué harás
- transporte con lona en rutas Polonia – Alemania – Benelux,
- 3 semanas en ruta / 1 en casa (posible 2/1),
- tacógrafo y documentación de transporte.

## Qué esperamos
- permiso C+E, código 95, tarjeta de conductor,
- más de 1 año en transporte internacional,
- inglés o alemán funcional.

## Qué ofrecemos
- 9 000 PLN netos al mes (base + dietas), puntual,
- tractoras de menos de 3 años,
- ayuda para obtener el código 95 y la tarjeta de conductor para extranjeros."""),
},
}

N = {
'minimalna-stawka-2027': {
 'pl': dict(title='Minimalna stawka godzinowa w 2027 r. — co zmienia się dla pracowników tymczasowych', excerpt='Nowa kwota, kogo dotyczy i jak sprawdzić, czy Twoja umowa jest zgodna.', rt=3, body="""Minimalne wynagrodzenie i minimalna stawka godzinowa są ogłaszane co roku rozporządzeniem Rady Ministrów. Poniżej wyjaśniamy, jak sprawdzić, czy Twoja umowa je spełnia.

## Kogo dotyczy stawka godzinowa
Minimalna stawka godzinowa obowiązuje przy **umowie zleceniu** i umowie o świadczenie usług. Przy umowie o pracę obowiązuje minimalne wynagrodzenie miesięczne — przeliczane na godziny wychodzi zbliżona kwota.

## Jak sprawdzić swoją umowę
- Znajdź w umowie kwotę za godzinę (brutto).
- Porównaj z aktualną stawką ogłoszoną w Monitorze Polskim.
- Jeśli kwota jest niższa — masz prawo do wyrównania. Napisz do nas, pomożemy.

## Uwaga na potrącenia
Koszt zakwaterowania lub dojazdu może być potrącany tylko za Twoją pisemną zgodą i tylko do wysokości określonej przepisami.

*Wartość stawki sprawdź w aktualnym rozporządzeniu — publikujemy ją tutaj po ogłoszeniu.*"""),
 'en': dict(title='Minimum hourly rate in 2027 — what changes for temporary workers', excerpt='The new amount, who it applies to and how to check your contract complies.', rt=3, body="""The minimum wage and the minimum hourly rate are announced every year by a regulation of the Council of Ministers. Here is how to check whether your contract meets them.

## Who the hourly rate applies to
The minimum hourly rate applies to **civil contracts (umowa zlecenie)** and service contracts. Employment contracts follow the monthly minimum wage — converted to hours it is a similar amount.

## How to check your contract
- Find the gross hourly amount in your contract.
- Compare it with the current rate published in Monitor Polski.
- If yours is lower, you are entitled to back pay. Write to us — we will help.

## Watch out for deductions
Accommodation or transport costs may only be deducted with your written consent and only up to the limits set by law.

*Check the exact rate in the current regulation — we publish it here once announced.*"""),
 'es': dict(title='Salario mínimo por hora en 2027 — qué cambia para los trabajadores temporales', excerpt='La nueva cantidad, a quién afecta y cómo comprobar si tu contrato cumple.', rt=3, body="""El salario mínimo y la tarifa mínima por hora se anuncian cada año mediante un reglamento del Consejo de Ministros. Así puedes comprobar si tu contrato los cumple.

## A quién afecta la tarifa por hora
La tarifa mínima por hora se aplica a los **contratos civiles (umowa zlecenie)** y de prestación de servicios. Los contratos de trabajo siguen el salario mínimo mensual — convertido a horas es una cantidad similar.

## Cómo comprobar tu contrato
- Busca en el contrato el importe bruto por hora.
- Compáralo con la tarifa vigente publicada en Monitor Polski.
- Si la tuya es inferior, tienes derecho a la diferencia. Escríbenos y te ayudamos.

## Cuidado con las deducciones
El alojamiento o el transporte solo pueden descontarse con tu consentimiento por escrito y hasta el límite legal.

*Consulta la cantidad exacta en el reglamento vigente — la publicamos aquí en cuanto se anuncie.*"""),
},
'zezwolenie-czy-oswiadczenie': {
 'pl': dict(title='Zezwolenie na pracę czy oświadczenie — którą ścieżkę wybrać', excerpt='Dwie drogi do legalnego zatrudnienia cudzoziemca, porównane krok po kroku.', rt=4, body="""Pracodawca, który chce zatrudnić osobę spoza Unii Europejskiej, ma do wyboru dwie główne ścieżki. Różnią się czasem, kosztem i tym, dla kogo są dostępne.

## Oświadczenie o powierzeniu wykonywania pracy
- dla obywateli wybranych państw (m.in. Ukraina, Białoruś, Mołdawia, Gruzja, Armenia),
- wpis do ewidencji w powiatowym urzędzie pracy — zwykle w kilka dni,
- praca do 24 miesięcy.

## Zezwolenie na pracę
- dla obywateli wszystkich państw,
- wydaje wojewoda; postępowanie trwa dłużej,
- wymaga zwykle testu rynku pracy (informacji starosty), chyba że zawód jest na liście zwolnionej.

## Jak wybrać
Jeśli kandydat ma obywatelstwo z listy oświadczeniowej i zatrudnienie nie przekroczy 24 miesięcy — oświadczenie jest szybsze i tańsze. W pozostałych przypadkach zostaje zezwolenie. W obu ścieżkach sam pobyt cudzoziemca musi być legalny niezależnie od dokumentu do pracy.

*Stan prawny i listy państw zmieniają się — przed decyzją potwierdzamy je w aktualnych przepisach.*"""),
 'en': dict(title='Work permit or declaration — which route to choose', excerpt='Two ways to legally employ a foreign worker in Poland, compared step by step.', rt=4, body="""An employer hiring a person from outside the EU has two main routes. They differ in time, cost and who is eligible.

## Declaration (oświadczenie o powierzeniu wykonywania pracy)
- for citizens of selected countries (incl. Ukraine, Belarus, Moldova, Georgia, Armenia),
- registered at the district labour office — usually within days,
- work for up to 24 months.

## Work permit (zezwolenie na pracę)
- for citizens of any country,
- issued by the voivode; takes longer,
- usually requires a labour-market test unless the occupation is on the exempt list.

## How to choose
If the candidate's nationality is on the declaration list and the job will not exceed 24 months, the declaration is faster and cheaper. Otherwise it is the work permit. In both cases the worker's stay must be legal independently of the work document.

*Rules and country lists change — we confirm them against current regulations before any decision.*"""),
 'es': dict(title='Permiso de trabajo o declaración — qué vía elegir', excerpt='Dos caminos para contratar legalmente a un extranjero en Polonia, comparados paso a paso.', rt=4, body="""Un empleador que contrata a una persona de fuera de la UE tiene dos vías principales. Se diferencian en tiempo, coste y a quién están abiertas.

## Declaración (oświadczenie o powierzeniu wykonywania pracy)
- para ciudadanos de determinados países (Ucrania, Bielorrusia, Moldavia, Georgia, Armenia, entre otros),
- inscripción en la oficina de empleo del distrito — normalmente en pocos días,
- trabajo hasta 24 meses.

## Permiso de trabajo (zezwolenie na pracę)
- para ciudadanos de cualquier país,
- lo emite el voivoda; tarda más,
- suele exigir un test del mercado laboral, salvo profesiones exentas.

## Cómo elegir
Si la nacionalidad del candidato está en la lista de la declaración y el empleo no superará 24 meses, la declaración es más rápida y barata. En los demás casos, el permiso. En ambas vías la estancia debe ser legal con independencia del documento de trabajo.

*Las normas y las listas de países cambian — las confirmamos en la legislación vigente antes de decidir.*"""),
},
'sezon-2026-podsumowanie': {
 'pl': dict(title='Sezon 2026 na rynku pracy tymczasowej — trzy rzeczy, które zostaną', excerpt='Więcej umów o pracę, krótsze rekrutacje, pracownicy z nowych kierunków.', rt=3, body="""Kończący się sezon pokazał trzy trendy, które naszym zdaniem zostaną na dłużej.

## 1. Umowa o pracę wygrywa ze zleceniem
Zakłady produkcyjne coraz częściej oferują etat od pierwszego dnia — bo kandydaci go oczekują, a rotacja przy zleceniach kosztuje więcej niż składki.

## 2. Rekrutacja trwa dni, nie tygodnie
Kto odpowiada kandydatowi w ciągu doby, ten go zatrudnia. Firmy z tygodniowym procesem tracą ludzi do konkurencji.

## 3. Nowe kierunki
Obok Ukrainy rośnie zatrudnienie osób z Ameryki Południowej i Azji Południowej. To oznacza więcej formalności — zezwolenia zamiast oświadczeń — i większą rolę agencji, która je prowadzi.

*Obserwacje własne z obsługiwanych rekrutacji; nie są to dane statystyczne.*"""),
 'en': dict(title='The 2026 temporary-work season — three things that will stay', excerpt='More employment contracts, shorter hiring, workers from new countries.', rt=3, body="""The closing season showed three trends we think are here to stay.

## 1. Employment contracts beat civil contracts
Plants increasingly offer a full contract from day one — candidates expect it, and turnover on civil contracts costs more than the contributions.

## 2. Hiring takes days, not weeks
Whoever answers a candidate within 24 hours gets to hire them. Companies with a week-long process lose people to competitors.

## 3. New countries of origin
Alongside Ukraine, hiring from South America and South Asia is growing. That means more paperwork — permits instead of declarations — and a bigger role for the agency that handles it.

*Our own observations from recruitments we ran; not statistical data.*"""),
 'es': dict(title='La temporada 2026 del trabajo temporal — tres cosas que se quedan', excerpt='Más contratos de trabajo, selecciones más cortas, trabajadores de nuevos países.', rt=3, body="""La temporada que termina mostró tres tendencias que, creemos, han llegado para quedarse.

## 1. El contrato de trabajo gana al contrato civil
Las fábricas ofrecen cada vez más contrato desde el primer día — los candidatos lo esperan y la rotación en contratos civiles cuesta más que las cotizaciones.

## 2. La selección dura días, no semanas
Quien responde al candidato en 24 horas es quien lo contrata. Las empresas con procesos de una semana pierden gente frente a la competencia.

## 3. Nuevos países de origen
Junto a Ucrania crece la contratación desde Sudamérica y el sur de Asia. Eso significa más trámites — permisos en lugar de declaraciones — y un papel mayor de la agencia que los gestiona.

*Observaciones propias de las selecciones gestionadas; no son datos estadísticos.*"""),
},
}

dates = {'operator-linii-produkcyjnej': '2026-09-18', 'pracownik-magazynu': '2026-09-15', 'specjalista-ds-kadr': '2026-09-10', 'kierowca-ce': '2026-09-05'}
ndates = {'minimalna-stawka-2027': '2026-09-21', 'zezwolenie-czy-oswiadczenie': '2026-09-14', 'sezon-2026-podsumowanie': '2026-09-07'}

def q(s):
    return '"' + s.replace('"', '\\"') + '"'

for slug, langs in J.items():
    for l, d in langs.items():
        os.makedirs(f'{ROOT}/jobs/{l}', exist_ok=True)
        fm = (f"---\nlang: {l}\ntitle: {q(d['title'])}\ncity: {q(d['city'])}\nindustry: {q(d['industry'])}\n"
              f"contract: {q(d['contract'])}\npay: {q(d['pay'])}\nterms: {q(d['terms'])}\n"
              f"tags: [{', '.join(q(t) for t in d['tags'])}]\npublished: {dates[slug]}\nexample: true\n---\n")
        open(f'{ROOT}/jobs/{l}/{slug}.md', 'w', encoding='utf-8').write(fm + d['body'] + '\n')
for slug, langs in N.items():
    for l, d in langs.items():
        os.makedirs(f'{ROOT}/news/{l}', exist_ok=True)
        fm = f"---\nlang: {l}\ntitle: {q(d['title'])}\nexcerpt: {q(d['excerpt'])}\npublished: {ndates[slug]}\nreadingTime: {d['rt']}\n---\n"
        open(f'{ROOT}/news/{l}/{slug}.md', 'w', encoding='utf-8').write(fm + d['body'] + '\n')
print('ok')
