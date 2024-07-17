#!/usr/bin/env python3
"""Module: Class Cache
"""

import redis
import uuid
from typing import Union, Callable, Optional


class Cache:
    """Class Cache
    """

    def __init__(self):
        """Intialize class Cache
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Sets a data to a key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float, None]:
        """Reads from Redis
        """
        data = self._redis.get(key)
        if data is None:
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Recovers original type
        """
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Recovers original type
        """
        return self.get(key, lambda x: int(x))
