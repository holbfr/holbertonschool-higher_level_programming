#!/usr/bin/env python3
"""
Simple module for task validation
"""
import pickle


class CustomObject():
    """CustomObject class definition"""

    def __init__(self, name, age, is_student):
        """CustomObject class constructor"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display instance information to stdout"""
        print("Name: {}\nAge: {}\nIs Student: {}".format(
            self.name, self.age, self.is_student))

    def serialize(self, filename):
        """Serializes the instance and saves it to file"""
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """Deserializes data from file (filename) into a python object"""
        try:
            with open(filename, 'rb') as file:
                loaded_data = pickle.load(file)
            return loaded_data
        except:
            return None
