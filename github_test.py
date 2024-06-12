import logging
import sys
from playwright.sync_api import sync_playwright

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    with (sync_playwright() as playwright):
        browser = playwright.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        #1
        logger.info(" Open Github home-page")
        page.goto("https://github.com")
    
        #2
        logger.info(" Validate the user is logged out")
        assert page.query_selector("text ='Sign up for GitHub'").is_visible(), "The user is not logged out!"
    
        #3
        logger.info(" Search the repo: 'org:microsoft typescript'")
        search_box = page.locator('[placeholder = "Search or jump to..."]')
        search_box.click()
        search = page.locator('[id = "query-builder-test"]')
        search.fill("org:microsoft typescript")
        search_box.press('Enter')
    
        #4
        logger.info(" Nevigate to 'TypeScript-Handbook' page")
        page.click('a[href="/microsoft/TypeScript-Handbook"]')

        #5
        logger.info(" Validate the repo page shows the 'is now read-only' message")
        page.wait_for_selector("text ='This repository has been archived by the owner on Oct 12, 2022. It is now read-only.'")
        assert page.query_selector("text ='This repository has been archived by the owner on Oct 12, 2022. It is now read-only.'").is_visible(), "'is now read-only' message not found"

        #6
        logger.info(" Validate that there are 38 branches")
        branches_text = page.locator('a[href="/microsoft/TypeScript-Handbook/branches"] strong').text_content()
        assert branches_text == "38", f"Expected 38 branches, found {branches_text}"

        #7
        logger.info(" Validate that there are more than 150 watchers")
        element = page.query_selector('a[href="/microsoft/TypeScript-Handbook/watchers"]')
        assert int(element.inner_text().split()[0])>150, f"Expected more than 150 watchers, found {int(element.inner_text().split()[0])}"

        #8
        logger.info(" Validate that there is at least one contributor coming from Huddersfield")
        page.locator("a.Link--primary.no-underline.Link.d-flex.flex-items-center[href='/microsoft/TypeScript-Handbook/graphs/contributors']").click()
        page.wait_for_selector('.contrib-person')
        contributors = page.locator("a[data-hovercard-type='user']")
        found_huddersfield = False
        for i in range(contributors.count()):
            contributor = contributors.nth(i)
            contributor.hover()
            page.wait_for_selector(".Popover-message")
            details = page.locator(".Popover-message").text_content()
            if "Huddersfield" in details:
                found_huddersfield = True
                break
        assert found_huddersfield, "No contributors from Huddersfield found"

        logger.info("All validations passed")
        browser.close()
        sys.exit(0)
      
    

except AssertionError as e:
    logger.error(f"Assertion failed: {e}")
    sys.exit(1)
except Exception as e:
    logger.error(f"An error occurred: {e}")
    sys.exit(1)
