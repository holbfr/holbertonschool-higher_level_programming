#!/usr/bin/env python3
"""
Simple moodule documentation for a task validation
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a python dictionary into XML and saves it in a file"""
    root = ET.Element('data')
    for k, v in dictionary.items():
        element = ET.Element(k)
        element.text = str(v)
        root.append(element)

    with open(filename, mode='w', encoding='utf-8') as file:
        file.write(ET.tostring(root, encoding='utf8').decode('utf8'))

    return root


def deserialize_from_xml(filename):
    """Reads XML data from the give file and returns a python dictionary"""
    dict = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        dict[child.tag] = child.text
    return dict
