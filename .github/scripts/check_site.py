from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag in ("a", "link") and "href" in attrs:
            self.links.append(attrs["href"])
        if tag in ("img", "script") and "src" in attrs:
            self.links.append(attrs["src"])


site = Path("site").resolve()
prefix = "/Terraform-Overview/"
pages = {}
for path in site.rglob("*.html"):
    parser = Page()
    parser.feed(path.read_text(encoding="utf-8"))
    pages[path.resolve()] = parser
if not pages:
    raise SystemExit("Missing built website.")
errors = []
for source, parser in pages.items():
    for link in parser.links:
        parts = urlsplit(link)
        if parts.scheme or parts.netloc:
            continue
        path = unquote(parts.path)
        if not path:
            target = source
        elif path.startswith(prefix):
            target = site / path[len(prefix):]
        elif path.startswith("/"):
            errors.append(f"{source.name}: link escapes site: {link}")
            continue
        else:
            target = source.parent / path
        if target.is_dir():
            target /= "index.html"
        target = target.resolve()
        if not target.is_file():
            errors.append(f"{source.name}: missing {link}")
        elif parts.fragment and target in pages and unquote(parts.fragment) not in pages[target].ids:
            errors.append(f"{source.name}: missing anchor {link}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Verified links, anchors, and assets across {len(pages)} HTML pages.")
