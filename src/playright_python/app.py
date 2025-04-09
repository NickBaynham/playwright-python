from playwright.sync_api import sync_playwright

print("Playwright Automation Framework")
with sync_playwright() as playwright:
    print("Playwright Started.")
    # Launch a Browser
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # Create a new Page
    page = browser.new_page()
    # Visit the Playwright Website
    page.goto("https://playwright.dev")
    # Visit another Playwright Website Page
    page.goto("https://playwright.dev/python")
    # Close the Browser
    browser.close()
print("Playwright Completed.")
