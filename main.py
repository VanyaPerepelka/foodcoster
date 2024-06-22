import time

import data_handlers as dh
from csv_parsing import csv_parser
import utils
import config


final_costs = dh.costs
raw_stats = dh.scraped_result
final_stats = dh.cleaned_stats
final_report_dict = dh.final_map

final_report_csv = csv_parser.to_csv(final_report_dict, f"final_report_{config.days_ago}.csv")

end = time.time()

print(f'EXEC TIME: [{end - utils.start}] SECONDS')
# UNCOMMENT FOR FORMING FULL CSV REPORT BY SCRAPER AND DATA HANDLER #

# raw_stats_csv = csv_parser.to_csv(final_stats, "cleaned_items.csv")
# clean_stats_csv = csv_parser.to_csv(raw_stats, "raw_items.csv")
#
# costs_csv = csv_parser.to_csv(final_costs, "costs.csv")
