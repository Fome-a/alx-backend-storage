#!/usr/bin/env python3
""
import uuid
import redis
from typing import Union

class Cache:
    """Cache class"""
    def __init__(self)-> None:
        """Cahce Instance"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, float, int]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return(key, data)

