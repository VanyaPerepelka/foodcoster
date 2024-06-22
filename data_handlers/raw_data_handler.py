import utils


def clean_raw_stats_dict(dictionary):
    """
    Clean raw statistics dictionary by converting values to numerical types and aggregating them.

    :param dictionary: The raw statistics dictionary with item names as keys and raw stats as values
    :return: A cleaned dictionary with item names as keys and aggregated stats as values
    """
    clean_dict = {}  # Initialize an empty dictionary to store cleaned data

    for item_name, raw_stats in dictionary.items():
        # Initialize variables to accumulate the weight, sum, and profit
        updated_weight, updated_sum, updated_profit = float(0), float(0), float(0)

        # Iterate through each stat value for the current item
        for stat_value in raw_stats:
            # Convert and accumulate the weight, sum, and profit values using utility functions
            updated_weight += utils.html_property_to_number(stat_value[1])
            updated_sum += utils.html_property_to_number(stat_value[2])
            updated_profit += utils.html_property_to_number(stat_value[3])

        # Store the accumulated values in the clean dictionary
        clean_dict[item_name] = [updated_weight, updated_sum, updated_profit]

    return clean_dict  # Return the cleaned dictionary


def calc_food_costs_and_merge(costs_map, stats_map):
    """
    Calculate food costs and merge the data from costs and stats maps.

    :param costs_map: A dictionary containing cost information with item names as keys
    :param stats_map: A dictionary containing stats information with item names as keys
    :return: A dictionary with merged data including calculated food costs
    """
    result = {}  # Initialize an empty dictionary to store the merged results

    # Iterate through each item in the stats map
    for key in stats_map:
        if key in costs_map:  # Only process items that exist in both maps
            # Retrieve unit cost and unit price from the costs map
            unit_cost = costs_map[key][0]
            unit_price = costs_map[key][1]

            # Calculate the expected food cost using the utility function
            expected_food_cost = utils.calc_expected_food_cost(unit_cost, unit_price)

            # Retrieve stats values from the stats map
            unit_sum = stats_map[key][0]
            unit_weight_count = stats_map[key][1]
            unit_profit = stats_map[key][2]

            # Calculate the natural food cost using the utility function
            natural_food_cost = utils.calculate_natural_food_cost(unit_price, unit_weight_count, unit_sum, unit_profit)

            # Create a merged list with values from both maps and the calculated costs
            merged = costs_map[key] + [expected_food_cost] + stats_map[key] + [natural_food_cost]

            # Store the merged list in the result dictionary
            result[key] = merged

    return result  # Return the merged results dictionary
