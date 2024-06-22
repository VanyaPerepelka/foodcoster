from config import chrome_config
from config import args_parser

login = args_parser.login
password = args_parser.password
project_name = args_parser.project_name
days_ago = args_parser.days_ago

args_parser.parse_arguments()
webdriver = chrome_config.driver

link_prefix = chrome_config.link_prefix
login_url = chrome_config.login_page_url
stats_url = chrome_config.stat_link_prefix_url
costs_url = chrome_config.costs_link_prefix_url


