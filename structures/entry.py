"""Entry and helper record types used by map and algorithm modules."""

from typing import Any

from structures.util import Hashable, object_to_byte_array


class Entry(Hashable):
    def __init__(self, key: Any, value: Any) -> None:
        self._key = key
        self._value = value
        self._randa = 31
        self._randb = 7
        self._prime = 2**31 - 1

    def get_key(self) -> Any:
        return self._key

    def get_value(self) -> Any:
        return self._value

    def update_key(self, nk: Any) -> None:
        self._key = nk

    def update_value(self, nv: Any) -> None:
        self._value = nv

    def __eq__(self, other) -> bool:
        return self.get_key() == other.get_key()

    def __lt__(self, other) -> bool:
        return self.get_key() < other.get_key()

    def get_hash(self, map_size: int | None = None) -> int:
        if isinstance(self._key, int):
            key_as_int = self._key
        else:
            key_as_int = int.from_bytes(object_to_byte_array(self._key), 'big')
        hashed_value = (self._randa * key_as_int + self._randb) % self._prime
        return hashed_value if map_size is None else hashed_value % map_size


class Compound:
    def __init__(self, x: int, y: int, r: float, cid: int) -> None:
        self._x = x
        self._y = y
        self._r = r
        self._cid = cid

    def get_coordinates(self) -> tuple[int, int]:
        return self._x, self._y

    def get_radius(self) -> float:
        return self._r

    def get_compound_id(self) -> int:
        return self._cid

    def __str__(self) -> str:
        return f"x = {self._x}, y = {self._y}, r = {self._r}, cid = {self._cid}"


class Offer:
    def __init__(self, n: int, m: int, k: int, cost: int, oid: int) -> None:
        self._n = n
        self._m = m
        self._k = k
        self._cost = cost
        self._oid = oid

    def get_n(self) -> int:
        return self._n

    def get_m(self) -> int:
        return self._m

    def get_k(self) -> int:
        return self._k

    def get_num_nodes(self) -> int:
        return self._n

    def get_num_edges(self) -> int:
        return self._m

    def get_diameter(self) -> int:
        return self._k

    def get_cost(self) -> int:
        return self._cost

    def get_offer_id(self) -> int:
        return self._oid

    def __str__(self) -> str:
        return f"n = {self._n}, m = {self._m}, k = {self._k}, cost = {self._cost}, oid = {self._oid}"
