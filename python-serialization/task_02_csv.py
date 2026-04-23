#!/usr/bin/env python3
"""
Simple python module for task validation
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Writes JSON data to data.json file"""
    try:
        with open(csv_filename, encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            rows = []
            for row in reader:
                rows.append(row)

        with open('data.json', mode='w', encoding='utf-8') as json_file:
            json.dump(rows, json_file, indent=4)
    except Exception as e:
        print(e)
        return False
    return True
