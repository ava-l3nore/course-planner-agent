import os, hashlib

from playwright.sync_api import sync_playwright

def fetch(URL):
    CACHE = "cache/cs_bs.html"

    os.makedirs("cache", exist_ok=True)

    if os.path.exists(CACHE) and os.path.getsize(CACHE) > 0:
        html = open(CACHE, encoding="utf-8").read()
    else:
        with sync_playwright() as p:
            b = p.chromium.launch(headless=True)
            page = b.new_page()
            page.goto(URL, wait_until="networkidle")
            html = page.content()
            print(len(html))
            print("acalog-course" in html)
            b.close()

        if len(html) > 50_000 or "acalog-course" not in html:
            raise RuntimeError(f"bad fetch: {len(html)} chars")

        open(CACHE, "w", encoding="utf-8").write(html)
        print("saved", len(html), hashlib.sha256(html.encode()).hexdigest()[:12])

    return html



