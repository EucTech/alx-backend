#!/usr/bin/env python3
"""Create a class LIFOCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCahe class"""
    def __init__(self):
        """instantce"""
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        """get function"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
