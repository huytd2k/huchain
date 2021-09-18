from __future__ import annotations
from typing import List, Union
from time import time
from dataclasses import dataclass, field
import hashlib
import json


@dataclass
class Chain:
    chain: List[Block] = field(default_factory=list)
    current_transactions: List[Transaction] = field(default_factory=list)

    def __len__(self):
        return len(self.chain)

    def __post_init__(self):
        self.new_block(previous_hash=1, prove=100)

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
        return self.last_block.index + 1

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    @classmethod
    def prove_of_work(cls, last_proof: int):
        cur_proof = 0
        while cls.valid_proof(last_proof, cur_proof) is False:
            cur_proof += 1
        return cur_proof

    @classmethod
    def valid_proof(cls, last_proof: int, proof):
        guess = f"{last_proof}{proof}".encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"


@dataclass
class Block:
    index: int
    timestamp: float
    transactions: List[Transaction]
    prove: int
    previous_hash: str

    @property
    def hash(self) -> int:
        return hashlib.sha256(self.toJSON()).hexdigest()

    def toJSON(self):
        return json.dumps(self, default=lambda b: b.__dict__, sort_keys=True).encode()


@dataclass
class Transaction:
    sender: str
    recipient: str
    amount: float
    prove: Union[int, None] = None
