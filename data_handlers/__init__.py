
from data_handlers import raw_data_handler
import scrapers


scraped_result = scrapers.scraped_stats

cleaned_stats = raw_data_handler.clean_raw_stats_dict(scraped_result)
costs = scrapers.scraped_costs

final_map = raw_data_handler.calc_food_costs_and_merge(costs, cleaned_stats)

