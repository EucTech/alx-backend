#!/usr/bin/env python3
"""Create a class BasicCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Basecache class"""
    def put(self, key, item):
        """put function"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """get function"""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
