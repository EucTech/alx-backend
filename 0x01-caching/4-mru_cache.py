#!/usr/bin/env python3
"""Create a class MRUCache that inherits from BaseCaching
and is a caching system"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache class"""
    cal = {}

    def __init__(self):
        """class instance"""
        super().__init__()
        self.cal = {}

    def put(self, key, item):
        """put function"""
        if not key or not item:
            return
        if self.cal:
            MRU_key = min(self.cal, key=self.cal.get)

        self.cache_data[key] = item
        self.cal[key] = 0

        if key in self.cache_data:
            for k, v in self.cal.items():
                if k != key:
                    self.cal[k] += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print('DISCARD:', MRU_key)
            del self.cache_data[MRU_key]
            del self.cal[MRU_key]

    def get(self, key):
        """get function"""
        if not key or key not in self.cache_data:
            return None

        self.cal[key] = 0
        for k, v in self.cal.items():
            if k != key:
                self.cal[k] += 1
        return self.cache_data[key]
