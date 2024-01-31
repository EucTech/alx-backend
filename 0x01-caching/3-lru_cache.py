#!/usr/bin/env python3
"""Create a class LRUCache that inherits from BaseCaching
and is a caching system"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCach class"""
    def __init__(self):
        """class instance"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """put function"""
        if key and item:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(discarded[0]))

    def get(self, key):
        """get function"""
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
