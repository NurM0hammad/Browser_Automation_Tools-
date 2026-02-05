import asyncio
from pyppeteer import launch

async def main():
    browser = await launch(headless=False)
    page = await browser.newPage()
    await page.goto('https://example.com')
    await page.type('input[name="q"]', 'Python automation')
    await page.click('button[type="submit"]')
    await browser.close()

asyncio.get_event_loop().run_until_complete(main())