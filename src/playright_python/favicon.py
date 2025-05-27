from playwright.sync_api import sync_playwright
from urllib.parse import quote, urlparse

def test_favicon_is_loaded():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        page = browser.new_page()

        # 1. Go to your site
        page.goto("https://calgentik.com", wait_until="networkidle")

        # 2. Grab the favicon URL from the <link> tag
        favicon_href = page.eval_on_selector(
            'link[rel~="icon"]',                 # matches rel="icon" or rel="shortcut icon"
            'el => el.href'
        )
        assert favicon_href, "No <link rel='icon'> found in the page."

        # 3. Check if it's a data URL or HTTP URL and verify accordingly
        parsed_url = urlparse(favicon_href)
        if parsed_url.scheme == 'data':
            # For data URLs, verify it's a valid base64 image
            assert favicon_href.startswith('data:image/'), "Favicon data URL is not a valid image"
            # Extract the base64 part after the comma
            base64_data = favicon_href.split(',')[1]
            assert base64_data, "Favicon data URL is empty"
        else:
            # For HTTP URLs, make a request to verify it loads
            encoded_url = quote(favicon_href, safe=':/?=&')
            response = page.request.get(encoded_url)
            assert response.ok, f"Favicon failed to load: {response.status} {response.status_text}"

        browser.close()

test_favicon_is_loaded()