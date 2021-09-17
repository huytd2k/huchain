from __future__ import annotations
from typing import List, Union
from dataclasses import dataclass


@dataclass
class Chain:
    chain: List[Block]
    current_transactions: List[Transaction]

    def new_block(self) -> Block:
        pass

    def new_transaction(self, sender: str, recipient: str, amount: float) -> int:
        """New transaction to be process in next block

        Args:
            sender (str): sender address
            recipient (str): recipien address
            amount (float): amount to send

        Returns:
            int: index of next block will include this transaction
        """
        tx = Transaction(sender, recipient, amount)
        self.current_transactions.append(tx)
        return self.last_block["index"] + 1

    @staticmethod
    def hash(self, block: Block) -> int:
        pass

    @property
    def last_block(self) -> int:
        pass


@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]

    def __hash__(self) -> int:
        pass


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    prove: Union[int, None] = None
