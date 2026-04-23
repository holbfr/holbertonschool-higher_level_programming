#!/usr/bin/env python3
"""
Simple python module for task validation
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """Writes JSON data to data.json file"""
    with open(csv_filename, ) as csv_file:
        reader = csv.DictReader(csv_file)
        with open('data.json', mode='w', encoding='utf-8') as json_file:
            for row in reader:
                # json_file.write(json.dumps(row))
                json.dump(row, json_file)
