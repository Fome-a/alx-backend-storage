#!/usr/bin/env python3
""
import uuid
import redis
<<<<<<< HEAD
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
=======
from functools import wraps
import sys
from typing import Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """count number of calls made to a method"""
    key = method.__qualname__

    @wraps(method)
    def counter(self, *args, **kwargs):
        """decorator method"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return counter


def call_history(method: Callable) -> Callable:
    """store the history of inputs and outputs for a particular function"""
    @wraps(method)
    def history_wrapper(self, *args, **kwargs):
        """set list keys to a wrapped function"""
        in_list_key = method.__qualname__ + ":inputs"
        out_list_key = method.__qualname__ + ":outputs"
        self._redis.rpush(in_list_key, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(out_list_key, str(output))
        return output
    return history_wrapper


def replay(method: Callable) -> None:
    """function displays the history of calls of a particular function"""
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"
    server = method.__self__._redis
    count = server.get(key).decode("utf-8")
    print(f"{key} was called {count} times:")
    input_list = server.lrange(inputs, 0, -1)
    output_list = server.lrange(outputs, 0, -1)
    zipped = list(zip(input_list, output_list))
    for k, v in zipped:
        attr, result = k.decode("utf-8"), k.decode("utf-8")
        print(f"{key}(*{attr}) -> {result}")

class Cache:
    """Cache class"""
    def __init__(self,redis)-> None:
        """instantiating the cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes a data argument and returns a string """ 
        key = str(uuid.uuid4())
        self._redis.set(str(key), data)
        return str(key)
    def get(self, key: str, fn: Optional[Callable] = None) ->\
                Union[str, bytes, int, float]:
            """retieves value from server, convert it to desired format"""
            return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_int(self, data_bytes: bytes) -> int:
        """convert data bytes from server back to int"""
        return int.from_bytes(data_bytes, sys.byteorder)
>>>>>>> 6cee8a52d9f5f4a16f76cb5ce8b0ab54ebede642

    def get_str(self, data_bytes: bytes) -> str:
        """convert data bytes from server back into str"""
        return data_bytes.decode('utf-8')
