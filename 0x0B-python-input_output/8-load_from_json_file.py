#!/usr/bin/python3
import json
"""
function that creates object from JSON file
"""


def load_from_json_file(filename):
    """
    creates object from JSON file
    """
    with open(filename) as f:
        return json.load(f)
