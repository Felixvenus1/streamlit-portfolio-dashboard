"""Capture a screenshot of each dashboard page (ARTEFACT 10-B companion).

Assumes the Streamlit app is already running locally. Pass the base URL as the
first argument (default http://localhost:8501).

Prerequisites:
    pip install playwright
    playwright install chromium

Usage:
    streamlit run app.py --server.headless true --server.port 8501
    python docs/capture_screenshots.py http://localhost:8501
"""

from __future__ import annotations

import sys
from pathlib import Path

PAGES = {
    "": "home.png",
    "uk_open_data": "page_uk_open_data.png",
    "steam_trends": "page_steam_trends.png",
    "football_analytics": "page_football_analytics.png",
    "about": "page_about.png",
}


def main() -> None:
    from playwright.sync_api import sync_playwright

    base = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8501"
    out = Path(__file__).resolve().parent
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1400, "height": 1000})
        for slug, fname in PAGES.items():
            page.goto(f"{base}/{slug}", wait_until="networkidle")
            # Wait for Streamlit to finish running (spinner gone).
            page.wait_for_timeout(4000)
            page.screenshot(path=str(out / fname), full_page=True)
            print(f"  captured {fname}")
        browser.close()


if __name__ == "__main__":
    main()
