import type { Lang } from './ui';

export type Option = { v: string; label: string };
export type Step = {
  /** klucz do podsumowania wysyłanego mailem */
  key: string;
  question: string;
  hint?: string;
  /** lista przycisków; pusta = pytanie otwarte */
  options?: Option[];
  /** true = można zaznaczyć kilka odpowiedzi */
  multi?: boolean;
  /** pole tekstowe pod przyciskami (albo zamiast nich) */
  free?: { label: string; placeholder: string; required?: boolean; long?: boolean };
};
export type Path = { id: 'candidate' | 'employer'; label: string; desc: string; steps: Step[] };

export type FormCopy = {
  intro: string;
  chooseRole: string;
  back: string;
  next: string;
  skip: string;
  step: string;
  of: string;
  summary: string;
  summaryLead: string;
  edit: string;
  contact: {
    name: string; namePh: string;
    contact: string; contactPh: string;
    langs: string; langsHint: string;
    note: string; notePh: string;
    consent: string;
  };
  send: string;
  sending: string;
  done: string;
  errContact: string;
  errRequired: string;
  errNet: string;
  or: string;
  callUs: string;
  paths: Path[];
};

const pl: FormCopy = {
  intro: 'Kilka krótkich pytań — dzięki nim od razu wiemy, w czym pomóc. Zajmuje około minuty.',
  chooseRole: 'Zacznijmy od tego, kim jesteś.',
  back: '← Wstecz', next: 'Dalej →', skip: 'Pomiń', step: 'Pytanie', of: 'z',
  summary: 'Twoje odpowiedzi', summaryLead: 'Sprawdź i dopisz, co uznasz za ważne.', edit: 'Zmień',
  contact: {
    name: 'Imię i nazwisko', namePh: 'Jan Kowalski',
    contact: 'Telefon lub e-mail', contactPh: '+48 600 100 200 albo jan@example.com',
    langs: 'W jakim języku się z Tobą kontaktować?', langsHint: 'Rozmawiamy po polsku, angielsku i hiszpańsku.',
    note: 'Chcesz coś dodać?', notePh: 'Napisz własnymi słowami, jeśli coś nie pasowało do pytań.',
    consent: 'Zgadzam się na przetwarzanie moich danych w celu odpowiedzi na wiadomość.',
  },
  send: 'Wyślij zgłoszenie', sending: 'Wysyłanie…',
  done: 'Zgłoszenie wysłane. Odpowiadamy w jeden dzień roboczy.',
  errContact: 'Wpisz numer telefonu albo e-mail — jedno wystarczy.',
  errRequired: 'To pytanie jest potrzebne, żebyśmy mogli pomóc.',
  errNet: 'Nie udało się wysłać. Zadzwoń albo napisz na',
  or: 'albo', callUs: 'Zadzwoń',
  paths: [
    {
      id: 'candidate', label: 'Szukam pracy', desc: 'Chcę podjąć pracę w Polsce albo zmienić obecną.',
      steps: [
        { key: 'Czego dotyczy sprawa', question: 'Czego dotyczy Twoja sprawa?', options: [
          { v: 'szukam-pracy', label: 'Szukam pracy' },
          { v: 'konkretna-oferta', label: 'Pytam o konkretną ofertę' },
          { v: 'legalizacja', label: 'Legalna praca i pobyt w Polsce' },
          { v: 'problem', label: 'Mam problem w obecnej pracy' },
        ] },
        { key: 'Status pobytu i pracy', question: 'Jaka jest Twoja sytuacja w Polsce?', hint: 'Od tego zależy, jakich dokumentów potrzebujesz do pracy.', options: [
          { v: 'pl', label: 'Jestem obywatelem Polski' },
          { v: 'ue', label: 'Jestem obywatelem UE / EOG' },
          { v: 'spoza-ue-z-prawem', label: 'Spoza UE — mam już prawo do pracy' },
          { v: 'spoza-ue-bez', label: 'Spoza UE — nie mam jeszcze dokumentu do pracy' },
          { v: 'nie-wiem', label: 'Nie jestem pewien / pewna' },
        ] },
        { key: 'Rodzaj pracy', question: 'Jaka praca Cię interesuje?', hint: 'Możesz zaznaczyć kilka.', multi: true, options: [
          { v: 'produkcja', label: 'Produkcja' },
          { v: 'magazyn', label: 'Magazyn i logistyka' },
          { v: 'kierowca', label: 'Kierowca' },
          { v: 'budowa', label: 'Budowa' },
          { v: 'biuro', label: 'Biuro i administracja' },
          { v: 'inne', label: 'Inne' },
        ], free: { label: 'Stanowisko lub zawód', placeholder: 'np. operator wózka widłowego, spawacz' } },
        { key: 'Miejsce i termin', question: 'Gdzie i od kiedy możesz pracować?', options: [
          { v: 'od-zaraz', label: 'Od zaraz' },
          { v: 'do-miesiaca', label: 'W ciągu miesiąca' },
          { v: 'pozniej', label: 'Później / planuję' },
        ], free: { label: 'Miasto lub region', placeholder: 'np. Poznań, cała Polska, tylko z zakwaterowaniem' } },
        { key: 'Doświadczenie i uprawnienia', question: 'Masz doświadczenie albo uprawnienia?', hint: 'Nie musisz — wiele ofert nie wymaga doświadczenia.', options: [
          { v: 'brak', label: 'Bez doświadczenia' },
          { v: 'do-2', label: 'Do 2 lat' },
          { v: 'ponad-2', label: 'Ponad 2 lata' },
        ], free: { label: 'Uprawnienia, prawo jazdy, języki', placeholder: 'np. UDT wózki widłowe, prawo jazdy C+E, angielski podstawowy', long: true } },
      ],
    },
    {
      id: 'employer', label: 'Szukam pracowników', desc: 'Prowadzę firmę i potrzebuję ludzi do pracy.',
      steps: [
        { key: 'Czego potrzebujesz', question: 'W czym możemy pomóc?', multi: true, options: [
          { v: 'rekrutacja', label: 'Rekrutacja stała' },
          { v: 'tymczasowa', label: 'Praca tymczasowa' },
          { v: 'cudzoziemcy', label: 'Zatrudnienie cudzoziemców' },
          { v: 'outsourcing', label: 'Outsourcing procesu' },
        ] },
        { key: 'Stanowisko', question: 'Kogo szukasz?', free: { label: 'Stanowisko i branża', placeholder: 'np. 20 operatorów produkcji, zakład spożywczy', required: true } },
        { key: 'Liczba osób', question: 'Ile osób potrzebujesz?', options: [
          { v: '1-5', label: '1–5' }, { v: '6-20', label: '6–20' },
          { v: '21-50', label: '21–50' }, { v: '50+', label: 'Ponad 50' },
        ] },
        { key: 'Miejsce i termin', question: 'Gdzie i na kiedy?', options: [
          { v: 'pilne', label: 'Pilnie — w tym tygodniu' },
          { v: 'miesiac', label: 'W ciągu miesiąca' },
          { v: 'planujemy', label: 'Planujemy na później' },
        ], free: { label: 'Miejsce pracy', placeholder: 'np. Wrocław, zakład pod Poznaniem' } },
        { key: 'Warunki', question: 'Co już wiesz o warunkach?', hint: 'Stawka, system zmianowy, zakwaterowanie — im więcej, tym szybciej odpowiemy.', free: { label: 'Warunki zatrudnienia', placeholder: 'np. 30 zł/h brutto, 3 zmiany, zapewniamy zakwaterowanie i dowóz', long: true } },
      ],
    },
  ],
};

const en: FormCopy = {
  intro: 'A few short questions — they tell us straight away how we can help. About a minute.',
  chooseRole: "Let's start with who you are.",
  back: '← Back', next: 'Next →', skip: 'Skip', step: 'Question', of: 'of',
  summary: 'Your answers', summaryLead: 'Check them and add anything important.', edit: 'Change',
  contact: {
    name: 'Full name', namePh: 'John Smith',
    contact: 'Phone or e-mail', contactPh: '+48 600 100 200 or john@example.com',
    langs: 'Which language should we use?', langsHint: 'We speak Polish, English and Spanish.',
    note: 'Anything to add?', notePh: "Write in your own words if the questions didn't fit.",
    consent: 'I agree to the processing of my data in order to reply to my message.',
  },
  send: 'Send enquiry', sending: 'Sending…',
  done: 'Enquiry sent. We reply within one business day.',
  errContact: 'Enter a phone number or an e-mail — one is enough.',
  errRequired: 'We need this answer to be able to help.',
  errNet: "Couldn't send. Call us or write to",
  or: 'or', callUs: 'Call',
  paths: [
    {
      id: 'candidate', label: 'I am looking for work', desc: 'I want to start working in Poland or change my job.',
      steps: [
        { key: 'What it is about', question: 'What is your enquiry about?', options: [
          { v: 'szukam-pracy', label: 'Looking for a job' },
          { v: 'konkretna-oferta', label: 'Asking about a specific offer' },
          { v: 'legalizacja', label: 'Legal work and stay in Poland' },
          { v: 'problem', label: 'A problem at my current job' },
        ] },
        { key: 'Residence and work status', question: 'What is your situation in Poland?', hint: 'This determines which documents you need in order to work.', options: [
          { v: 'pl', label: 'I am a Polish citizen' },
          { v: 'ue', label: 'I am an EU / EEA citizen' },
          { v: 'spoza-ue-z-prawem', label: 'Non-EU — I already have the right to work' },
          { v: 'spoza-ue-bez', label: 'Non-EU — no work document yet' },
          { v: 'nie-wiem', label: "I'm not sure" },
        ] },
        { key: 'Type of work', question: 'What kind of work are you interested in?', hint: 'You can pick several.', multi: true, options: [
          { v: 'produkcja', label: 'Manufacturing' },
          { v: 'magazyn', label: 'Warehouse & logistics' },
          { v: 'kierowca', label: 'Driver' },
          { v: 'budowa', label: 'Construction' },
          { v: 'biuro', label: 'Office & admin' },
          { v: 'inne', label: 'Other' },
        ], free: { label: 'Position or trade', placeholder: 'e.g. forklift operator, welder' } },
        { key: 'Place and start date', question: 'Where and from when can you work?', options: [
          { v: 'od-zaraz', label: 'Immediately' },
          { v: 'do-miesiaca', label: 'Within a month' },
          { v: 'pozniej', label: 'Later / planning ahead' },
        ], free: { label: 'City or region', placeholder: 'e.g. Poznań, anywhere in Poland, only with accommodation' } },
        { key: 'Experience and licences', question: 'Do you have experience or licences?', hint: "You don't have to — many offers need no experience.", options: [
          { v: 'brak', label: 'No experience' },
          { v: 'do-2', label: 'Up to 2 years' },
          { v: 'ponad-2', label: 'Over 2 years' },
        ], free: { label: 'Licences, driving licence, languages', placeholder: 'e.g. forklift licence (UDT), C+E licence, basic English', long: true } },
      ],
    },
    {
      id: 'employer', label: 'I am looking for workers', desc: 'I run a company and need people.',
      steps: [
        { key: 'What you need', question: 'How can we help?', multi: true, options: [
          { v: 'rekrutacja', label: 'Permanent recruitment' },
          { v: 'tymczasowa', label: 'Temporary staffing' },
          { v: 'cudzoziemcy', label: 'Hiring foreign workers' },
          { v: 'outsourcing', label: 'Process outsourcing' },
        ] },
        { key: 'Position', question: 'Who are you looking for?', free: { label: 'Position and industry', placeholder: 'e.g. 20 production operators, food plant', required: true } },
        { key: 'Number of people', question: 'How many people do you need?', options: [
          { v: '1-5', label: '1–5' }, { v: '6-20', label: '6–20' },
          { v: '21-50', label: '21–50' }, { v: '50+', label: 'Over 50' },
        ] },
        { key: 'Place and timing', question: 'Where and by when?', options: [
          { v: 'pilne', label: 'Urgent — this week' },
          { v: 'miesiac', label: 'Within a month' },
          { v: 'planujemy', label: 'Planning ahead' },
        ], free: { label: 'Place of work', placeholder: 'e.g. Wrocław, plant near Poznań' } },
        { key: 'Terms', question: 'What do you already know about the terms?', hint: 'Rate, shift system, accommodation — the more you tell us, the faster we reply.', free: { label: 'Employment terms', placeholder: 'e.g. 30 PLN/h gross, 3 shifts, accommodation and transport provided', long: true } },
      ],
    },
  ],
};

const es: FormCopy = {
  intro: 'Unas preguntas breves — así sabemos enseguida cómo ayudarte. Un minuto aproximadamente.',
  chooseRole: 'Empecemos por quién eres.',
  back: '← Atrás', next: 'Siguiente →', skip: 'Omitir', step: 'Pregunta', of: 'de',
  summary: 'Tus respuestas', summaryLead: 'Revísalas y añade lo que consideres importante.', edit: 'Cambiar',
  contact: {
    name: 'Nombre y apellidos', namePh: 'Juan Pérez',
    contact: 'Teléfono o e-mail', contactPh: '+48 600 100 200 o juan@example.com',
    langs: '¿En qué idioma te contactamos?', langsHint: 'Hablamos polaco, inglés y español.',
    note: '¿Quieres añadir algo?', notePh: 'Escríbelo con tus palabras si algo no encajaba en las preguntas.',
    consent: 'Acepto el tratamiento de mis datos para responder a mi mensaje.',
  },
  send: 'Enviar consulta', sending: 'Enviando…',
  done: 'Consulta enviada. Respondemos en un día laborable.',
  errContact: 'Escribe un teléfono o un e-mail — con uno basta.',
  errRequired: 'Necesitamos esta respuesta para poder ayudarte.',
  errNet: 'No se pudo enviar. Llámanos o escribe a',
  or: 'o', callUs: 'Llamar',
  paths: [
    {
      id: 'candidate', label: 'Busco trabajo', desc: 'Quiero trabajar en Polonia o cambiar de empleo.',
      steps: [
        { key: 'Motivo de la consulta', question: '¿De qué se trata tu consulta?', options: [
          { v: 'szukam-pracy', label: 'Busco empleo' },
          { v: 'konkretna-oferta', label: 'Pregunto por una oferta concreta' },
          { v: 'legalizacja', label: 'Trabajo y estancia legal en Polonia' },
          { v: 'problem', label: 'Tengo un problema en mi trabajo actual' },
        ] },
        { key: 'Situación de estancia y trabajo', question: '¿Cuál es tu situación en Polonia?', hint: 'De esto depende qué documentos necesitas para trabajar.', options: [
          { v: 'pl', label: 'Soy ciudadano polaco' },
          { v: 'ue', label: 'Soy ciudadano de la UE / EEE' },
          { v: 'spoza-ue-z-prawem', label: 'Fuera de la UE — ya tengo derecho a trabajar' },
          { v: 'spoza-ue-bez', label: 'Fuera de la UE — aún sin documento de trabajo' },
          { v: 'nie-wiem', label: 'No estoy seguro / segura' },
        ] },
        { key: 'Tipo de trabajo', question: '¿Qué tipo de trabajo te interesa?', hint: 'Puedes elegir varios.', multi: true, options: [
          { v: 'produkcja', label: 'Producción' },
          { v: 'magazyn', label: 'Almacén y logística' },
          { v: 'kierowca', label: 'Conductor' },
          { v: 'budowa', label: 'Construcción' },
          { v: 'biuro', label: 'Oficina y administración' },
          { v: 'inne', label: 'Otro' },
        ], free: { label: 'Puesto u oficio', placeholder: 'p. ej. carretillero, soldador' } },
        { key: 'Lugar y fecha', question: '¿Dónde y desde cuándo puedes trabajar?', options: [
          { v: 'od-zaraz', label: 'De inmediato' },
          { v: 'do-miesiaca', label: 'En un mes' },
          { v: 'pozniej', label: 'Más adelante' },
        ], free: { label: 'Ciudad o región', placeholder: 'p. ej. Poznań, toda Polonia, solo con alojamiento' } },
        { key: 'Experiencia y carnés', question: '¿Tienes experiencia o carnés?', hint: 'No es obligatorio — muchas ofertas no requieren experiencia.', options: [
          { v: 'brak', label: 'Sin experiencia' },
          { v: 'do-2', label: 'Hasta 2 años' },
          { v: 'ponad-2', label: 'Más de 2 años' },
        ], free: { label: 'Carnés, permiso de conducir, idiomas', placeholder: 'p. ej. carné de carretilla (UDT), permiso C+E, inglés básico', long: true } },
      ],
    },
    {
      id: 'employer', label: 'Busco personal', desc: 'Tengo una empresa y necesito trabajadores.',
      steps: [
        { key: 'Qué necesitas', question: '¿En qué podemos ayudarte?', multi: true, options: [
          { v: 'rekrutacja', label: 'Selección permanente' },
          { v: 'tymczasowa', label: 'Trabajo temporal' },
          { v: 'cudzoziemcy', label: 'Contratación de extranjeros' },
          { v: 'outsourcing', label: 'Externalización de procesos' },
        ] },
        { key: 'Puesto', question: '¿A quién buscas?', free: { label: 'Puesto y sector', placeholder: 'p. ej. 20 operarios de producción, planta alimentaria', required: true } },
        { key: 'Número de personas', question: '¿Cuántas personas necesitas?', options: [
          { v: '1-5', label: '1–5' }, { v: '6-20', label: '6–20' },
          { v: '21-50', label: '21–50' }, { v: '50+', label: 'Más de 50' },
        ] },
        { key: 'Lugar y plazo', question: '¿Dónde y para cuándo?', options: [
          { v: 'pilne', label: 'Urgente — esta semana' },
          { v: 'miesiac', label: 'En un mes' },
          { v: 'planujemy', label: 'Más adelante' },
        ], free: { label: 'Lugar de trabajo', placeholder: 'p. ej. Wrocław, planta cerca de Poznań' } },
        { key: 'Condiciones', question: '¿Qué sabes ya de las condiciones?', hint: 'Tarifa, turnos, alojamiento — cuanto más nos cuentes, antes respondemos.', free: { label: 'Condiciones de empleo', placeholder: 'p. ej. 30 PLN/h bruto, 3 turnos, alojamiento y transporte incluidos', long: true } },
      ],
    },
  ],
};

export const formCopy: Record<Lang, FormCopy> = { pl, en, es };
