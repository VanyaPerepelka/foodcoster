import scrapers
import utils
from csv_parsing import csv_parser
import data_handlers

utils.delete_all_previous_data(".csv")

raw_stats = data_handlers.scraped_result
clean_stats = data_handlers.cleaned_stats
costs = scrapers.scraped_costs
final_report = data_handlers.final_map

