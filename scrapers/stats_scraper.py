import time
import utils
import config

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from config import webdriver as driver
from config import login_url
from config import stats_url


def scrape_stat_page(items_map, table):
    """
    Scrape statistics from a page and populate the items_map and table with data.

    :param items_map: A dictionary to store item statistics
    :param table: A list to store the raw table data
    """
    current_key = ""  # Initialize the current key for item mapping
    time.sleep(3)  # Wait for the page to load

    # Check if the current URL is the login page and perform login if necessary
    if driver.current_url == login_url:
        print("[INFO]     Met login page!")
        utils.login()  # Call the login function from utils
        time.sleep(5)  # Wait for the login to complete

    # Find elements on the page with specific data attributes
    elems = driver.find_elements(By.XPATH, "//td["
                                           "contains(@data-e2e, 'product_full_name') or "
                                           "contains(@data-e2e, 'weight_count') or "
                                           "contains(@data-e2e, 'product_sum') or "
                                           "contains(@data-e2e, 'product_profit')"
                                           "]")

    raw = []  # Initialize a list to store raw values

    for index, web_element in enumerate(elems):
        current_value = web_element.get_attribute("title")  # Get the value of the element's title attribute
        raw.append(current_value)  # Append the current value to the raw list

        if index % 4 == 0:  # Every fourth element indicates a new item
            current_key = utils.clean_item_from_mods(current_value)  # Clean the item name

        if (index + 1) % 4 == 0:  # After every set of four elements, update the items_map
            if current_key not in items_map:
                items_map[current_key] = []  # Initialize the list for the new key

            items_map[current_key].append(raw)  # Append the raw data to the items_map
            table.append(raw)  # Append the raw data to the table
            raw = []  # Reset the raw list for the next set of data

    try:
        next_page = driver.find_element(By.XPATH, '//li[@class="next"]')  # Find the 'next' button
        next_page.click()  # Click the 'next' button to go to the next page
        # print("[INFO]     goto next page")
        scrape_stat_page(items_map, table)  # Recursively scrape the next page
    except NoSuchElementException:
        return  # If no 'next' button is found, end the recursion


def find_statistics():
    """
    Set up the time scope and start scraping statistics.

    :return: A dictionary with the scraped statistics
    """
    link_to_scrape = utils.set_up_timescope(stats_url, config.days_ago)  # Form the link to scrape
    print(f"[INFO]     Link formed: [{link_to_scrape}]")

    driver.get(link_to_scrape)  # Navigate to the formed link
    print(f"[INFO]     Met stats page! [{link_to_scrape}]")

    table = []  # Initialize a list to store the raw table data
    items_map = dict()  # Initialize a dictionary to store item statistics

    scrape_stat_page(items_map, table)  # Start scraping the statistics
    return items_map  # Return the items_map with the scraped data
