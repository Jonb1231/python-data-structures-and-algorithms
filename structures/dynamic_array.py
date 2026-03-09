
from collections.abc import Iterator
from random import randint
from typing import Any


class DynamicArray:
    """A lightweight dynamic array with amortized O(1) append."""

    def __init__(self) -> None:
        self._data = [None] * 128
        self._size = 0
        self._capacity = 128
        self.reversed = False

    def __str__(self) -> str:
        return str(self.to_list())

    def __repr__(self) -> str:
        return self.__str__()

    def __iter__(self) -> Iterator[Any]:
        for i in range(self._size):
            yield self.get_at(i)

    def __len__(self) -> int:
        return self._size

    def __resize(self) -> None:
        self._capacity *= 2
        new_list = [None] * self._capacity
        for i in range(self._size):
            new_list[i] = self._data[i]
        self._data = new_list

    def build_from_list(self, inlist: list) -> None:
        self._data = list(inlist)
        self._capacity = len(inlist)
        self._size = len(inlist)

    def allocate(self, elements_desired: int, default_val: Any = None) -> None:
        self._data = [default_val] * elements_desired
        self._size = elements_desired
        self._capacity = elements_desired

    def get_at(self, index: int) -> Any | None:
        if 0 <= index < self._size:
            return self._data[index] if not self.reversed else self._data[self._size - index - 1]
        return None

    def __getitem__(self, index: int) -> Any | None:
        return self.get_at(index)

    def set_at(self, index: int, element: Any) -> None:
        if 0 <= index < self._size:
            real_index = index if not self.reversed else self._size - index - 1
            self._data[real_index] = element

    def __setitem__(self, index: int, element: Any) -> None:
        self.set_at(index, element)

    def append(self, element: Any) -> None:
        if self._size == self._capacity:
            self.__resize()
        self._data[self._size] = element
        self._size += 1

    def remove(self, element: Any) -> None:
        for idx in range(self._size):
            if self._data[idx] == element:
                self.remove_at(idx)
                return

    def remove_at(self, index: int) -> Any | None:
        elem = None
        if 0 <= index < self._size:
            elem = self._data[index]
            for i in range(index, self._size - 1):
                self._data[i] = self._data[i + 1]
            self._size -= 1
            self._data[self._size] = None
        return elem

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def get_size(self) -> int:
        return self._size

    def get_capacity(self) -> int:
        return self._capacity

    def to_list(self) -> list[Any]:
        return [self.get_at(i) for i in range(self._size)]

    def sort(self) -> None:
        if self._size > 1:
            self.__qsort(0, self._size - 1)

    def __qsort(self, lo: int, hi: int) -> None:
        if lo >= hi:
            return
        pivot = self.__random_pivot(lo, hi)
        self.__qsort(lo, pivot)
        self.__qsort(pivot + 1, hi)

    def __random_pivot(self, lo: int, hi: int) -> int:
        pidx = randint(lo, hi)
        pivot = self._data[pidx]
        left = lo - 1
        right = hi + 1
        while True:
            left += 1
            while self._data[left] < pivot:
                left += 1
            right -= 1
            while self._data[right] > pivot:
                right -= 1
            if left >= right:
                return right
            self._data[left], self._data[right] = self._data[right], self._data[left]

    def reverse(self) -> None:
        self.reversed = not self.reversed
