from __future__ import annotations
from typing import List
from dataclasses import dataclass


@dataclass
class Chain:
    chain: List[Block]

    def new_block(self) -> Block:
        pass

    def new_transaction(self) -> Transaction:
        pass

    @staticmethod
    def hash(self) -> int:
        pass

    @property
    def last_block(self) -> int:
        pass


@dataclass
class Block:
    transactions: List[Transaction]
    pass


@dataclass
class Transaction:
    pass


@dataclass
class Address:
    pass
