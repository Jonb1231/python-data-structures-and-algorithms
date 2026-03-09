"""Small utilities shared across the project."""

import pickle
from abc import ABC, abstractmethod
from typing import Any


class Hashable(ABC):
    @abstractmethod
    def get_hash(self) -> int:
        raise NotImplementedError


def object_to_byte_array(obj: Any) -> bytes:
    return pickle.dumps(obj)
