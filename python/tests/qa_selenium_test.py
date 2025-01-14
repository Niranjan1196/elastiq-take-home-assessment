import pytest
from page_object.helper.driver_factory import DriverFactory
from page_object.actions.search_page_action import SearchPageAction
from page_object.helper.assertion_helper import AssertionHelper
from page_object.helper.driver_factory import DriverFactory

# Test data
browser = "chrome"  # Default is "chrome", or pass "firefox" for Firefox
page_url = "https://www.lambdatest.com/selenium-playground/table-sort-search-demo"
data_to_search = "New York"
expected_pagination_info = "Showing 1 to 5 of 5 entries (filtered from 24 total entries)"


# Fixture to initialize and manage WebDriver
@pytest.fixture(scope="function")
def driver():
    # Initialize the WebDriver
    driver = DriverFactory.get_driver(browser)

    # Ensure the driver is properly closed after the test
    yield driver
    driver.quit()


def test_search_functionality_and_validate_the_search_result(driver):
    # Navigate to the Selenium Playground Table Search Demo page
    driver.get(page_url)
    print(f"Navigated to '{page_url}' page url successfully.")

    # Object Initialize
    search_page = SearchPageAction(driver)
    assertion_helper = AssertionHelper()

    # Wait for the page to load and the search field to be visible
    search_page.verify_visibility_of_search_box()

    # Perform search
    search_page.enter_data_in_search_box(data_to_search)

    # Wait for search results to load
    search_page.wait_for_table_to_load_and_verify_visibility_of_rows()

    # Get filtered data rows
    data_of_all_rows = search_page.get_all_data_from_rows()

    # Assert that the number of entries is 5
    assert len(data_of_all_rows) == 5, f"Expected 5 entries, but found {len(data_of_all_rows)} entries."

    # print all filtered rows records
    print(f"Found {len(data_of_all_rows)} entries matching with '{data_to_search}'")
    for row in data_of_all_rows:
        print(row.text)

    # Get the pagination info from
    actual_pagination_info = search_page.get_pagination_text()
    print(f"Pagination Info: {actual_pagination_info}")

    # verify the expected and actual pagination info
    assertion_helper.verify_strings_equal(expected_pagination_info, actual_pagination_info)
