"""Bloom filter implementation built on top of BitVector."""

from typing import Any

from structures.bit_vector import BitVector
from structures.util import object_to_byte_array


class BloomFilter:
    """Static Bloom filter for approximate membership tests."""

    def __init__(self, max_keys: int) -> None:
        self._data = BitVector()
        self.capacity = max(1, max_keys * 15)
        self._data.allocate(self.capacity)
        self.size = 0

    def __str__(self) -> str:
        return f"BloomFilter(size={self.size}, capacity={self.capacity})"

    def hash_func1(self, value: int | str) -> int:
        if isinstance(value, str):
            value = int.from_bytes(object_to_byte_array(value), byteorder='big')
        return (value * 31 ^ (value >> 3)) % self.capacity

    def hash_func2(self, value: int | str) -> int:
        if isinstance(value, str):
            value = int.from_bytes(object_to_byte_array(value), byteorder='big')
        return (value * 37 ^ (value << 5) ^ (value >> 5)) % self.capacity

    def hash_func3(self, value: int | str) -> int:
        if isinstance(value, str):
            value = int.from_bytes(object_to_byte_array(value), byteorder='big')
        return (value * 41 ^ (value << 7) ^ (value >> 7)) % self.capacity

    def hash_func4(self, value: int | str) -> int:
        if isinstance(value, str):
            value = int.from_bytes(object_to_byte_array(value), byteorder='big')
        return (value * 43 ^ (value >> 5) ^ (value << 11)) % self.capacity

    def hash_func5(self, value: int | str) -> int:
        if isinstance(value, str):
            value = int.from_bytes(object_to_byte_array(value), byteorder='big')
        return (value * 47 ^ (value << 6) ^ (value >> 13)) % self.capacity

    def final_hash1(self, value: int | str) -> int:
        return (self.hash_func1(value) ^ self.hash_func3(value) ^ self.hash_func5(value)) % self.capacity

    def final_hash2(self, value: int | str) -> int:
        h1, h2, h3 = self.hash_func5(value), self.hash_func2(value), self.hash_func4(value)
        return (h3 ^ (h1 + h2)) % self.capacity

    def final_hash3(self, value: int | str) -> int:
        h1, h2, h3 = self.hash_func3(value), self.hash_func1(value), self.hash_func2(value)
        return ((h2 << 3) ^ h1 ^ (h3 >> 2)) % self.capacity

    def insert(self, key: Any) -> None:
        for bit in (self.final_hash1(key), self.final_hash2(key), self.final_hash3(key)):
            self._data.set_at(bit)
        self.size += 1

    def contains(self, key: Any) -> bool:
        bits = [
            self._data.get_at(self.final_hash1(key)),
            self._data.get_at(self.final_hash2(key)),
            self._data.get_at(self.final_hash3(key)),
        ]
        return all(bit == 1 for bit in bits)

    def __contains__(self, key: Any) -> bool:
        return self.contains(key)

    def is_empty(self) -> bool:
        return self.size == 0

    def get_capacity(self) -> int:
        return self.capacity
