from playwright.sync_api import sync_playwright, expect
import sys

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        try:
            # Go to the page
            page.goto("http://localhost:3000/")

            # Focus the skip link (first focusable element usually)
            page.keyboard.press("Tab")

            # Get the skip link
            skip_link = page.locator(".skip-link")

            # Verify it is focused
            expect(skip_link).to_be_focused()

            # Wait for transition to complete (0.2s)
            page.wait_for_timeout(300)

            # Take screenshot
            page.screenshot(path="verification/skip_link_visible.png")

            # Check bounding box
            box = skip_link.bounding_box()
            print(f"Skip link position: y={box['y']}")

            if box['y'] < 0:
                print("Error: Skip link is off-screen!")
                sys.exit(1)
            else:
                print("Success: Skip link is on-screen.")

        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)
        finally:
            browser.close()

if __name__ == "__main__":
    run()
