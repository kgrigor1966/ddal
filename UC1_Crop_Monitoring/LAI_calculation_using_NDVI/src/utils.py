"""
utils.py - Utility Functions

This module contains a collection of utility functions for common tasks in the project.
These functions include  configuration loading.

Functions:
- `load_config`: Load configuration settings from a YAML file.


Usage:
    import utils

    # Example usage of load_config function:
    config = util.load_config("config.yaml")
"""

import yaml

def load_config(config_file):
    """Load configuration from a YAML file.
    Args:
        config_file (str): The path to the YAML configuration file.

    Returns:
        dict: A dictionary containing the configuration settings.
    """

    # Open the YAML configuration file in read mode
    with open(config_file, "r") as f:
        # Parse the YAML content and load it into a dictionary
        config = yaml.load(f, Loader=yaml.FullLoader)

    print("_____Current configuration_____")
    
    # Iterate through the configuration dictionary and print key-value pairs
    for key, value in config.items():
        print(key + ": " + str(value))
    
    # Return the loaded configuration as a dictionary
    return config