# Selenium Search Functionality Test

## Project Overview

This project automates the testing of the search functionality on the **Selenium Playground Table Search Demo** page. The test ensures that:
1. The page is accessible.
2. A search for "New York" can be performed successfully.
3. The search returns exactly 5 matching entries out of a total of 24 entries.
4. The pagination information is correct.

### Key Features:
- Verifies the correct number of entries (5) for the search term "New York".
- Ensures the pagination info matches the expected format.
- Uses **Selenium WebDriver** for browser automation.
- Uses **pytest** for testing.

## Setup Instructions

### Prerequisites:
1. **Python 3.x** (Python 3.6 or higher recommended)
2. **Selenium WebDriver** for browser automation.
3. **WebDriver Manager** to handle browser driver installation (ChromeDriver or GeckoDriver).

## Getting Started
To install `elastiq-take-home-assessment`, follow these steps:

Clone the repo: https://github.com/Niranjan1196/elastiq-take-home-assessment

### Step 1: Install Dependencies
Install Pycharm

To install the required dependencies, use pip:

pip install pytest
pip install pytest-html
pip install selenium pytest webdriver-manager
pip install pytest selenium


## Run the Tests

To run tests, follow these steps:

1. `pytest tests/qa_selenium_test.py` #Without HTML Report
2. `pytest tests/qa_selenium_test.py  --html=../reports/report.html` #With HTML Report

Or Incase getting any issue can run directly using:
`Right Click > Ctrl + Shift + F10` or `Right Click > Run button`

## View/Access the Report
1. Go to reports.
2. Open report.html

## Contact

If you want to contact me you can reach me at `niranjansangale96@gmail.com`.
