import os
from playwright.sync_api import sync_playwright, expect

def run(playwright):
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()

    # Get the absolute path to the HTML file
    file_path = os.path.abspath('index.html')

    # Navigate to the local HTML file
    page.goto(f'file://{file_path}')

    # Scroll to the bottom of the page to trigger all animations
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    # Wait for the footer to become visible
    page.wait_for_selector('footer.visible')

    # Take a screenshot
    page.screenshot(path="jules-scratch/verification/verification.png")

    browser.close()

with sync_playwright() as playwright:
    run(playwright)