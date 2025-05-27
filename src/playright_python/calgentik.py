from playwright.sync_api import sync_playwright

print("Calgentik.com")
with sync_playwright() as playwright:
    print("Playwright Started.")
    # Launch a Browser
    # browser = playwright.chromium.launch(headless=False, slow_mo=500)
    browser = playwright.chromium.launch()
    # Create a new Page
    page = browser.new_page()
    # Visit the Playwright Website
    page.goto("https://calgentik.com")
    # Visit another Playwright Website Page
    page.goto("https://calgentik.com")
    # Locate a link element with 'Services' as the name
    services_link = page.get_by_role("link", name="Services")
    # Click on the Services link
    services_link.click()
    # Get the URL
    url = page.url
    print("Services:", url)
    # Close the Browser
    browser.close()
print("Calgentick.com Test Completed.")
