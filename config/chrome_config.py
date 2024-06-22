from config import args_parser
from selenium import webdriver
import chromedriver_autoinstaller

chromedriver_autoinstaller.install()

options = webdriver.ChromeOptions()

# CHANGE TO TRUE TO KEEP CHROME PAGE OPEN AFTER PROCESSING THE SCRIPT
options.add_experimental_option("detach", False)

# COMMENT TO RUN WITH UI CHROME PAGE
options.add_argument('--headless')

driver = webdriver.Chrome(options)

link_prefix = args_parser.link_prefix

login_page_url = f'{link_prefix}/manage/login'
stat_link_prefix_url = f'{link_prefix}/manage/dash/products/'
costs_link_prefix_url = f'{link_prefix}/manage/dishes'
