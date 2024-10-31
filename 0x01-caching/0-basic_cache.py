#!/usr/bin/python3
""" BasicCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    an extension to the original BaseCaching system that has
    a constant `key: value` pairs number to be cached
    """
    def __init__(self):
        """
        intiating the original __init__() function of
        BaseCaching
        """
        super().__init__()

    def put(self, key, item):
        """
        adding a new key:value pair into our dictionary
        """
        if key and item:
            self.cache_data.update({key: item})
        else:
            return None

    def get(self, key):
        """
        getting the corrosponding value of the key if exists
        or None if there's no value for that key
        """
        return self.cache_data.get(key)
