import sys, json, argparse
ap = argparse.ArgumentParser(description="Scrapling fetch: print links/text/JSON from a page")
ap.add_argument("url"); ap.add_argument("css", nargs="?", default=None, help="CSS selector (default: all links)")
ap.add_argument("--stealth", action="store_true", help="headless stealth browser (for JS / anti-bot pages)")
ap.add_argument("--json", action="store_true")
a = ap.parse_args()
if a.stealth:
    from scrapling.fetchers import StealthyFetcher as F; page = F.fetch(a.url, headless=True)
else:
    from scrapling.fetchers import Fetcher as F; page = F.get(a.url)
sel = a.css or "a"
rows = []
for el in page.css(sel):
    t = " ".join(el.get_all_text(strip=True).split()) if hasattr(el, "get_all_text") else str(el.text)
    rows.append({"text": t, "href": el.attrib.get("href")})
if a.json: print(json.dumps({"status": page.status, "url": a.url, "items": rows}, indent=1))
else:
    print(f"# {page.status} {a.url} ({len(rows)} items for '{sel}')", file=sys.stderr)
    for r in rows: print(r["text"] + (f"\t{r['href']}" if r["href"] else ""))
