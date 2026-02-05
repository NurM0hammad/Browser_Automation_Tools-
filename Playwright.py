from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Launch browser
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    
    # Navigate and interact
    page.goto("https://quotes.toscrape.com/")
    page.fill("input[name='https://quotes.toscrape.com/']", "Python automation")
    page.click("button[type='submit']")
    
    # Take screenshot
    page.screenshot(path="screenshot.png")
    
    browser.close()