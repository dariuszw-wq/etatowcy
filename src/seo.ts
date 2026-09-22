import { t, href, type Lang, type RouteKey } from './i18n/ui';

/**
 * Ścieżka nawigacyjna dla Google: strona główna → dział → bieżąca strona.
 * Pokazuje się w wynikach zamiast surowego adresu.
 */
export function breadcrumb(site: string, lang: Lang, route: RouteKey, navKey: string, title: string, slug: string) {
  const items = [
    { name: 'Etatowcy', item: site + href(lang) },
    { name: t(lang)(navKey), item: site + href(lang, route) },
    { name: title, item: site + href(lang, route, slug) },
  ];
  return {
    '@context': 'https://schema.org',
    '@type': 'BreadcrumbList',
    itemListElement: items.map((x, i) => ({ '@type': 'ListItem', position: i + 1, name: x.name, item: x.item })),
  };
}
