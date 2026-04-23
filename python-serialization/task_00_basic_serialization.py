#!/usr/bin/env python3
"""
Simple python module for task validation
"""
import json


def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary (data) and puts it in the file (filename)"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Deserializes JSON file data (filename) into a python dictionary"""
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
