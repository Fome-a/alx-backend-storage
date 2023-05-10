#!/usr/bin/env python3
""
import uuid
import redis

class Cache:
    def __init__(self,redis):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        key = str(uuid.uuid4())
        self._redis.set(key, data)

