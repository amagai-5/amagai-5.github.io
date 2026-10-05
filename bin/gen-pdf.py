# pip install playwright && playwright install chromium
from pathlib import Path
from playwright.sync_api import sync_playwright

# 公開後のURLでも、手元のファイルでもOK(どちらか一方を使う)
URL = Path("index.html").resolve().as_uri()      # 手元で確認する場合
# URL = "https://<あなたのユーザー名>.github.io/"  # 公開後(プロジェクトページなら末尾に <repo>/ を付ける)

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.emulate_media(color_scheme="light")      # ダークモードの影響を避ける
    page.goto(URL, wait_until="networkidle")      # Webフォントの読み込みを待つ
    page.pdf(
        path="my_portfolio.pdf",
        format="A4",
        print_background=True,
        prefer_css_page_size=True,                # print.css の @page を優先
    )
    browser.close()
