from __future__ import annotations
from typing import List, Union
from time import time
from dataclasses import dataclass
import hashlib
import json


@dataclass
class Chain:
    chain: List[Block] = []
    current_transactions: List[Transaction] = []

    # def __post_init__(self):
    #     self.new_block(previos_hash=1, prove=100)

    def new_block(self, prove: int, previous_hash: str = None) -> Block:
        """Add new block to the chain. It will add current queued transactions
        into this block

        Args:
            prove (int): nonce or prove of legit block
            previous_hash (str, optional): the hash of previous block. Defaults to None.

        Returns:
            Block: added block
        """
        block = Block(
            index=len(self.chain) + 1,
            timestamp=time(),
            prove=prove,
            transactions=self.current_transactions.copy(),
            previous_hash=previous_hash,
        )
        self.current_transactions.clear()
        self.chain.append(block)
        return block

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
    def hash(block: Block) -> int:
        serialized_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(serialized_block).hexdigest()

    @property
    def last_block(self) -> int:
        pass


@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    prove: int
    previous_hash: str

    def __hash__(self) -> int:
        return Chain.hash(self)


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    prove: Union[int, None] = None
