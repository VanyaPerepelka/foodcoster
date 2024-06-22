import argparse

# Initialize global variables for storing parsed arguments
login = ''
password = ''
project_name = ''
days_ago = ''
link_prefix = ''


def create_parser():
    """
    Create an argument parser for the script.

    :return: An ArgumentParser object
    """
    parser = argparse.ArgumentParser(description="Script to process Poster admin-panel arguments.")
    parser.add_argument("-l", "--login", required=True, help="Provide login for user of Poster admin-panel")
    parser.add_argument("-p", "--password", required=True, help="Provide password associated with Poster login")
    parser.add_argument("-n", "--name", required=True, help="Provide name of your project in Poster network")
    parser.add_argument("-d", "--days", help="How many days ago to start accounting?")
    return parser  # Return the configured ArgumentParser object


def parse_arguments():
    """
    Parse command-line arguments and store them in global variables.
    """
    global login, password, project_name, days_ago, link_prefix  # Declare global variables to store parsed arguments

    parser = create_parser()  # Create the argument parser
    args = parser.parse_args()  # Parse the command-line arguments

    # Assign the parsed arguments to global variables
    login = args.login
    password = args.password
    project_name = args.name
    link_prefix = f'https://{project_name}.joinposter.com'  # Construct the link prefix using the project name
    days_ago = args.days  # Optional argument, can be None if not provided


parse_arguments()  # Call the function to parse arguments and initialize global variables
