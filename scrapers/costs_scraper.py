import time
import utils

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from config import webdriver as driver
from config import login_url
from config import costs_url


def scrape_costs(items_map):
    """
    Scrape cost data from the web page and populate the items_map with the data.

    :param items_map: A dictionary to store cost data
    """
    time.sleep(3)  # Wait for the page to load

    # Check if the current URL is the login page and perform login if necessary
    if driver.current_url == login_url:
        print("[INFO]     Met login page!")
        utils.login()  # Call the login function from utils
        time.sleep(5)  # Wait for the login to complete

    # Find elements on the page with specific data attributes
    elems = driver.find_elements(By.XPATH, "//td["
                                           "contains(@data-e2e, 'product_name') or "
                                           "contains(@data-e2e, 'cost_per_unit') or "
                                           "contains(@data-e2e, 'price_with_tax')"
                                           "]")

    current_key = ""  # Initialize the current key for item mapping
    row = []  # Initialize a list to store row values
    index = 0  # Initialize an index to keep track of elements within a row

    # Iterate through the found elements
    for i, web_element in enumerate(elems):
        current_value = web_element.get_attribute("title")  # Get the value of the element's title attribute

        if index == 0:  # First element in a set of three represents the product name
            current_key = utils.clean_item_from_mods(current_value)  # Clean the product name
        else:  # Second and third elements represent cost and price respectively
            row.append(current_value)  # Append the current value to the row list

        if index == 2 or i == len(elems) - 1:  # After every set of three elements, update the items_map
            items_map[current_key] = row  # Map the cleaned product name to the row values
            current_key = ""  # Reset the current key for the next item
            index = 0  # Reset the index for the next set of elements
            row = []  # Reset the row list for the next set of values
        else:
            index += 1  # Increment the index for the next element in the current row

    # Try to find the 'next' button to navigate to the next page
    next_page = driver.find_element(By.XPATH, '//li[@class="next"]')

    try:
        next_page.click()  # Click the 'next' button to go to the next page
        # print("[INFO]     goto next page")
        scrape_costs(items_map)  # Recursively scrape the next page
    except NoSuchElementException:
        return  # If no 'next' button is found, end the recursion


def find_costs():
    """
    Navigate to the costs page and start scraping cost data.

    :return: A dictionary with the scraped cost data
    """
    driver.get(costs_url)  # Navigate to the costs page URL
    costs_map = dict()  # Initialize a dictionary to store cost data

    print(f"[INFO]     Met costs page! [{costs_url}]")
    scrape_costs(costs_map)  # Start scraping the cost data

    return costs_map  # Return the dictionary with the scraped cost data
