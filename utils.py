import re
import time
from datetime import datetime as DT, timedelta
from selenium.webdriver.common.by import By

import os
import config

# Define the date format to be used throughout the script
date_format = '%Y-%m-%d'

# Record the start time for performance measurement
start = time.time()


def set_up_timescope(stat_link_prefix_url, days_ago):
    """
    Set up the time scope for statistical data retrieval.

    :param stat_link_prefix_url: The prefix URL for the statistics link
    :param days_ago: The number of days ago to start the time scope from
    :return: A formatted link with the date range
    """
    # Default to 8 days ago if days_ago is not provided
    days_ago = int(days_ago) if days_ago is not None else 8

    if days_ago is None:
        print(f"[INFO]     There is no provided start-range date so week ago was accepted as default")

    # Calculate the start date and end date (last closed shift was yesterday)
    date_from = (DT.today() - timedelta(days=days_ago)).strftime(date_format)
    print(f"[INFO]     Date-from point was formed({date_from})")

    last_closed_shift = (DT.today() - timedelta(days=1)).strftime(date_format)
    print(f"[INFO]     All stats will be counted to {last_closed_shift} cuz there was last closed shift")

    # Form the complete link with the date range
    formed_link = f"{stat_link_prefix_url}{date_from}/{last_closed_shift}"
    return formed_link


def clean_item_from_mods(item_name):
    """
    Clean the item name by removing modifications (text within parentheses).

    :param item_name: The name of the item
    :return: The cleaned item name
    """
    separator = "("
    return item_name.split(separator)[0].strip()


def html_property_to_number(html_property):
    """
    Convert an HTML property string to a float number.

    :param html_property: The HTML property string
    :return: The converted float number
    """
    # Remove non-numeric characters, replace comma with dot, and strip extra dots
    cleaned_property = re.sub('[^\\d,.-]', '', html_property).replace(",", ".").strip(".")

    # Convert to float and round to 2 decimal places
    result = f"{float(cleaned_property):.2f}"
    return float(result)


def login():
    """
    Perform login using the credentials from the config.
    """
    # Find the email input field and enter the email
    email_input = config.webdriver.find_element(By.ID, 'email')
    email_input.send_keys(config.login)

    # Find the password input field and enter the password
    password_input = config.webdriver.find_element(By.ID, 'password')
    password_input.send_keys(config.password)

    # Find and click the login button
    login_button = config.webdriver.find_element(By.XPATH, "//input[@value='Увійти']")
    login_button.click()
    print(f"[INFO]     Logged in with provided pass: [{config.password}] [{config.login}]")


def delete_all_previous_data(end_with):
    """
    Delete all files in the current directory that end with the specified extension.

    :param end_with: The file extension to match
    """
    current_dir_path = os.getcwd()

    # List all files with the specified extension
    filelist = [f for f in os.listdir(current_dir_path) if f.endswith(end_with)]

    # Remove each file in the list
    for f in filelist:
        os.remove(os.path.join(current_dir_path, f))
    print(f"[INFO]     List of files with previous data was deleted! [{str(filelist)}]")


def calc_expected_food_cost(unit_cost, unit_price):
    """
    Calculate the expected food cost as a percentage of the unit price.

    :param unit_cost: The cost per unit
    :param unit_price: The selling price per unit
    :return: The expected food cost percentage as a string
    """
    unit_cost = float(unit_cost)
    unit_price = float(unit_price)

    # Check if unit_price or unit_cost is zero to avoid division by zero
    if unit_price == 0 or unit_cost == 0:
        return "0.00 %"
    else:
        # Calculate the result and round it to 2 decimal places
        result = (unit_cost / unit_price) * 100
        return f"{result:.2f} %"


def calculate_natural_food_cost(unit_price, weight_count, product_sum, profit):
    """
    Calculate the natural food cost as a percentage.

    :param unit_price: The cost per unit
    :param weight_count: The total weight count
    :param product_sum: The sum of the product values
    :param profit: The profit made
    :return: The natural food cost percentage as a string
    """
    unit_price = float(unit_price)
    weight_count = float(weight_count)
    product_sum = float(product_sum)
    profit = float(profit)

    # Check if any inputs are zero to avoid division by zero
    if unit_price == 0 or weight_count == 0 or product_sum == 0:
        return "0.00 %"
    else:
        # Calculate the result and round it to 2 decimal places
        result = (weight_count - profit) / product_sum / unit_price * 100
        return f"{result:.2f} %"
