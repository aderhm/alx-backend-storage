#!/usr/bin/env python3
"""Module: Class Cache
"""

import redis
import uuid


class Cache:
    """Class Cache
    """

    def __init__(self):
        """Intialize class Cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Sets a data to a key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
