"""Import the supplied COSC snapshot without fetching/rebuilding the official directory.

Usage: python scripts/import-trusted-profile.py SOURCE_HTML
Requires beautifulsoup4. All source record fields and links are preserved.
"""
import hashlib
import json
import sys
from pathlib import Path
from bs4 import BeautifulSoup

source = Path(sys.argv[1])
soup = BeautifulSoup(source.read_text(encoding='utf-8'), 'html.parser')
points = []
for node in soup.select('section.point'):
    address = node.find('p', recursive=False)
    comment = node.select_one('.comment')
    points.append({
        'id': node['data-point-id'],
        'province': node['data-province'],
        'city': node['data-city'],
        'name': node.h3.get_text(),
        'address': address.get_text('\n'),
        'comment': comment.get_text() if comment else '',
        'links': [{'action': a.get('data-action', ''), 'label': a.get_text(), 'url': a['href']} for a in node.select('a[href]')],
    })
assert len(points) == len({p['id'] for p in points}) == 2293
assert len({p['province'] for p in points}) == 16
assert sum(bool(p['comment']) for p in points) == 922
assert sum(a['action'] == 'map' for p in points for a in p['links']) == 2293
assert sum(a['action'] == 'book' for p in points for a in p['links']) == 399
assert all(a['url'].startswith(('https://', 'http://')) for p in points for a in p['links'])
data = {
    'source': 'https://cosc.org.pl/punkty-potwierdzajace-profil-zaufany.html',
    'originalSource': 'https://pz.gov.pl/ui/au/find-cp',
    'sourceDate': '2026-11-05',
    'sourceSha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'points': points,
}
target = Path('src/data/trusted-profile-points.json')
target.parent.mkdir(parents=True, exist_ok=True)
target.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(f'Imported {len(points)} points, 922 comments, 2293 maps, 399 bookings; source 2026-11-05')
