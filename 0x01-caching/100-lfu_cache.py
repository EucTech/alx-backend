#!/usr/bin/env python3
"""Create a class LFUCache that inherits from BaseCaching
and is a caching system"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class"""
    usage_count = {}

    def __init__(self):
        """class instance"""
        super().__init__()
        self.usage_count = {}

    def put(self, key, item):
        """get function"""
        if not key or not item:
            return
        self.cache_data[key] = item
        self.usage_count[key] = 0

        if key in self.cache_data:
            for k, v in self.usage_count.items():
                if k != key:
                    self.usage_count[k] += 1

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            LFU_key = max(self.usage_count, key=self.usage_count.get)
            print('DISCARD:', LFU_key)
            del self.cache_data[LFU_key]
            del self.usage_count[LFU_key]

    def get(self, key):
        """get function"""
        if not key or key not in self.cache_data:
            return None
        return self.cache_data[key]
