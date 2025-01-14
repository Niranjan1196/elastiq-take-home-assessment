from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_object.locators.search_page_locators import SearchPageLocators

class SearchPageAction:
    def __init__(self, driver):
        self.driver = driver

    # Action to enter and search the data
    def enter_data_in_search_box(self, search_value):
        search_box = self.driver.find_element(By.XPATH, SearchPageLocators.UI_ELEMENT_SEARCH_BOX)
        search_box.clear()
        print("Search box cleared successfully.")
        search_box.send_keys(search_value)
        print(f"Entered search value: '{search_value}' into the search box.")
        search_box.send_keys(Keys.RETURN)

    # Action verify visibility of search box
    def verify_visibility_of_search_box(self):
        WebDriverWait(self.driver, 100).until(
            EC.presence_of_all_elements_located((By.XPATH, SearchPageLocators.UI_ELEMENT_SEARCH_BOX))
        )
        print("Search box is visible on home page.")

    # Action to wait until the table rows are loaded and verify visibility of rows
    def wait_for_table_to_load_and_verify_visibility_of_rows(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, SearchPageLocators.UI_ELEMENT_TABLE_ROWS))
        )
        print("All records in the table is visible.")

    # Get all rows in the table excluding header rows
    def get_all_data_from_rows(self):
        all_rows = self.driver.find_elements(By.XPATH, SearchPageLocators.UI_ELEMENT_TABLE_ROWS)
        return [row for row in all_rows if len(row.find_elements(By.TAG_NAME, "td")) > 0]

    # Get the search result from pagination
    def get_pagination_text(self):
        # Wait until the pagination element is present
        pagination_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, SearchPageLocators.UI_ELEMENT_PAGINATION_RECORDS))
        )

        # Get the text of the pagination element
        pagination_text = pagination_element.text

        # Return the extracted text
        return pagination_text