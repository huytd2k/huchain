from pychain.core.chain import Block, Chain, Transaction
from unittest import TestCase


class TestChain(TestCase):
    def test_init(self):
        chain = Chain()

        assert len(chain) == 1
        assert chain.current_transactions == []

    def test_new_block(self):
        chain = Chain()
        init_len = len(chain)
        chain.current_transactions = ["tx1", "tx2", "tx3"]

        block = chain.new_block(prove=2, previous_hash="abc")

        assert len(chain) == init_len + 1
        assert chain.chain[-1] == block
        assert block.transactions == ["tx1", "tx2", "tx3"]
        assert chain.current_transactions == []

    def test_new_transaction(self):
        chain = Chain()
        block_index = chain.new_transaction("abc", "def", 100)
        actual_tx = chain.current_transactions[-1]

        assert block_index == chain.last_block.index + 1
        assert actual_tx.sender == "abc"
        assert actual_tx.recipient == "def"
        assert actual_tx.amount == 100

    def test_prove_of_work(self):
        proof = Chain.prove_of_work(100)

        assert Chain.valid_proof(100, proof)

    def test_valid_prove(self):
        assert Chain.valid_proof(1, 72608)
        assert Chain.valid_proof(2, 69926)
        assert Chain.valid_proof(3, 31733)


class TestBlock(TestCase):
    def test_hash(self):
        block = Block(
            index=1,
            timestamp=1000,
            transactions=[
                Transaction("abc", "cde", 1000),
                Transaction("bcd", "efg", 1000),
            ],
            prove=1000,
            previous_hash="abc",
        )
        block2 = Block(
            index=1,
            timestamp=1000,
            transactions=[
                Transaction("abc", "cde", 1000),
                Transaction("bcd", "efg", 1000),
            ],
            prove=1000,
            previous_hash="abc",
        )
        assert block.hash == block2.hash
