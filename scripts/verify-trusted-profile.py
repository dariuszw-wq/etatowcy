"""Verify built pages against every source record, links and SEO metadata."""
import json
from pathlib import Path
from urllib.parse import urlsplit
from bs4 import BeautifulSoup

data = json.loads(Path('src/data/trusted-profile-points.json').read_text(encoding='utf-8'))
points = {p['id']: p for p in data['points']}
assert len(points) == 2293
routes = {
    'pl': ('rynek-pracy', 'punkty-potwierdzajace-profil-zaufany'),
    'en': ('labour-market', 'trusted-profile-confirmation-points'),
    'es': ('mercado-laboral', 'puntos-confirmacion-perfil-confianza'),
}
sitemap = Path('dist/sitemap-0.xml').read_text(encoding='utf-8')
for lang, (news, directory) in routes.items():
    urls = [f'/{lang}/{directory}/', f'/{lang}/{news}/profil-zaufany-jak-zalozyc/']
    for url in urls:
        soup = BeautifulSoup(Path('dist' + url + 'index.html').read_text(encoding='utf-8'), 'html.parser')
        canonical = 'https://etatowcy.pl' + url
        assert soup.select_one('link[rel=canonical]')['href'] == canonical
        assert canonical in sitemap
        assert soup.html['lang'] == lang
        assert len(soup.select('h1')) == 1
        assert len(soup.select('link[hreflang]')) == 4
        assert not soup.select_one('meta[name=robots][content*=noindex]')
        assert len(soup.select_one('meta[name=description]')['content']) <= 155
        for node in soup.select('script[type="application/ld+json"]'):
            json.loads(node.string)
        for a in soup.select('a[href]'):
            href = a['href']
            if href.startswith('/') and not href.startswith('//'):
                path = Path('dist' + urlsplit(href).path)
                assert path.exists(), (url, href)
        if directory in url:
            nodes = soup.select('.point')
            assert len(nodes) == 2293
            assert {n['data-point-id'] for n in nodes} == set(points)
            for node in nodes:
                point = points[node['data-point-id']]
                assert node.h2.get_text() == point['name']
                assert node.select_one('.address').get_text() == point['address']
                comment = node.select_one('.comment')
                assert (comment.get_text() if comment else '') == point['comment']
                assert [(a['data-action'], a['href']) for a in node.select('.point-links a')] == [(a['action'], a['url']) for a in point['links']]
            assert len(soup.select('.province')) == 16
            assert len(soup.select('.comment')) == 922
            assert len(soup.select('[data-action=map]')) == 2293
            assert len(soup.select('[data-action=book]')) == 399
        print(f'PASS {url}: complete data, links, metadata and sitemap')
    for url in [f'/{lang}/', f'/{lang}/{news}/']:
        soup = BeautifulSoup(Path('dist' + url + 'index.html').read_text(encoding='utf-8'), 'html.parser')
        for target in urls:
            assert soup.select_one(f'main a[href="{target}"]')
            assert soup.select_one(f'footer a[href="{target}"]')
print('PASS all 6 pages and permanent links in 3 languages')
