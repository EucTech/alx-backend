#!/usr/bin/env python3
"""Create a class FIFOCache that inherits from
BaseCaching and is a caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Fifocahe class"""
    def __init__(self):
        """instantiation"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """get function"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
