#!/usr/bin/python3
""" BasicCaching module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
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
        self.usage_order = []

    def put(self, key, item):
        """
        Add an item to the cache using LRU algorithm
        Args:
            key: The key to store the item under
            item: The item to store
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.usage_order.remove(key)

        self.usage_order.append(key)

        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:

            lru_key = self.usage_order.pop(-1)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

    def get(self, key):
        """
        Retrieve an item from the cache and update its usage status
        Args:
            key: The key to look up
        Returns:
            The value associated with the key, or None if not found
        """
        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
