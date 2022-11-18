#!/usr/bin/python3
""" class student """


class Student:
    """ define function"""
    def __init__(self, first_name, last_name, age):
        """
        :param self:
        :param first_name:
        :param last_name:
        :param age:
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__

        return ({key: value for key, value in self.__dict__.items()
                 if key in attrs})

    def reload_from_json(self, json):
        """
        replace all attr of the
        student instance
        """
        self.__dict__.update(json)
