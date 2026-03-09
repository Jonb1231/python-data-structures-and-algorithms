
from typing import Any

from structures.entry import Entry
from structures.linked_list import DoublyLinkedList


class Map:
    """Hash map backed by separate chaining with doubly linked lists."""

    def __init__(self) -> None:
        self._caps = [2**7 - 1, 2**13 - 1, 2**17 - 1, 2**19 - 1, 8388609, 2**31 - 1]
        self.capnum = 0
        self.capacity = self._caps[0]
        self.size = 0
        self.hash_table = [DoublyLinkedList() for _ in range(self.capacity)]
        self.keys = []

    def _load_factor(self) -> float:
        return self.size / self.capacity

    def rehash(self) -> None:
        if self.capnum + 1 >= len(self._caps):
            return
        old_table = self.hash_table
        old_cap = self.capacity
        self.capnum += 1
        self.capacity = self._caps[self.capnum]
        self.hash_table = [DoublyLinkedList() for _ in range(self.capacity)]
        for i in range(old_cap):
            cur = old_table[i].get_head_node()
            while cur is not None:
                entry = cur.get_data()
                hashval = Entry(entry.get_key(), entry.get_value()).get_hash(self.capacity)
                self.hash_table[hashval].insert_to_front(entry)
                cur = cur.get_next()

    def force_rehash(self) -> None:
        self.rehash()

    def insert_speedy(self, key: Any, value: Any) -> None:
        entry = Entry(key, value)
        hashval = entry.get_hash(self.capacity)
        self.hash_table[hashval].insert_to_front(entry)
        self.size += 1
        self.keys.append(key)
        if self._load_factor() >= 0.7:
            self.rehash()

    def insert(self, entry: Entry) -> Any | None:
        hashval = entry.get_hash(self.capacity)
        bucket = self.hash_table[hashval]
        current = bucket.get_head_node()
        while current is not None:
            if current.get_data().get_key() == entry.get_key():
                old_value = current.get_data().get_value()
                current.set_data(entry)
                return old_value
            current = current.get_next()
        self.keys.append(entry.get_key())
        bucket.insert_to_front(entry)
        self.size += 1
        if self._load_factor() >= 0.7:
            self.rehash()
        return None

    def get_keys(self):
        return self.keys

    def insert_kv(self, key: Any, value: Any) -> Any | None:
        return self.insert(Entry(key, value))

    def __setitem__(self, key: Any, value: Any) -> None:
        self.insert(Entry(key, value))

    def incr_value(self, key: Any) -> None:
        old = self.find(key)
        self.insert_kv(key, old + 1)

    def remove(self, key: Any) -> None:
        entry = Entry(key, None)
        hashval = entry.get_hash(self.capacity)
        bucket = self.hash_table[hashval]
        current = bucket.get_head_node()
        target = None
        while current is not None:
            if current.get_data().get_key() == key:
                target = current.get_data()
                break
            current = current.get_next()
        if target is not None:
            bucket.find_and_remove_element(target)
            self.size -= 1
            if key in self.keys:
                self.keys.remove(key)

    def find(self, key: Any) -> Any | None:
        entry = Entry(key, None)
        hashval = entry.get_hash(self.capacity)
        current = self.hash_table[hashval].get_head_node()
        while current is not None:
            if current.get_data().get_key() == key:
                return current.get_data().get_value()
            current = current.get_next()
        return None

    def __getitem__(self, key: Any) -> Any | None:
        return self.find(key)

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def get_bucket_size(self, index: int) -> int:
        return self.hash_table[index].get_size()
