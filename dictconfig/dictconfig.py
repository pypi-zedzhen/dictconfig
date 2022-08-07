from dataclasses import dataclass
from typing import Callable

from .error import ReadError, WriteError

__all__ = ['BaseDictConfig']


@dataclass(repr=False, eq=False)
class BaseDictConfig:
    filename: str
    func_read: Callable[[str], dict]
    func_write: Callable[[str, dict], None]

    def __post_init__(self):
        self.cnf = {}

    def read(self) -> bool:
        try:
            self.cnf = self.func_read(self.filename)
        except ReadError:
            return False
        return True

    def save(self) -> bool:
        try:
            self.func_write(self.filename, self.cnf)
        except WriteError:
            return False
        return True

    def __len__(self):
        return self.cnf.__len__()

    def __getitem__(self, key):
        return self.cnf.__getitem__(key)

    def __setitem__(self, key, value):
        return self.cnf.__setitem__(key, value)

    def __delitem__(self, key):
        return self.cnf.__delitem__(key)

    def __iter__(self):
        return self.cnf.__iter__()

    def __reversed__(self):
        return self.cnf.__reversed__()

    def __contains__(self, item):
        return self.cnf.__contains__(item)
