/** Dane kontaktowe i ustawienia serwisu — jedyne miejsce do zmiany. */
export const site = {
  /** Adres, na który trafiają wiadomości z formularza (także jako mailto: awaryjnie). */
  email: 'biuro@etatowcy.pl',
  /** Numer WhatsApp w formacie międzynarodowym; pusty = nie pokazuj. Telefonu nie podajemy. */
  whatsapp: '+48 791 969 995',
  /**
   * Endpoint formularza (np. Formspree: https://formspree.io/f/xxxxxxx — darmowe konto, 50 wiadomości/mies.).
   * Pusty = formularz otwiera program pocztowy (mailto).
   */
  formEndpoint: import.meta.env.PUBLIC_FORM_ENDPOINT ?? '',
  /** Nazwa firmy do stopki i polityki prywatności. */
  legalName: 'Etatowcy',
};
