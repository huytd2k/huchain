from pychain.core.chain import Chain
from typing import Optional

from fastapi import FastAPI
from uuid import uuid4

app = FastAPI()

# Generate the node ID
node_id = str(uuid4()).replace("-", "")
# Create blockchain
chain = Chain()


@app.get("/mine")
def mine():
    return "Mining..."


@app.post("/transactions")
def new_trx(sender: str, recipient: str, amount: float):
    block_index = chain.new_transaction(sender, recipient, amount)
    return {"result": f"This transactions will be added to block {block_index}"}


@app.get("/chain")
def get_chain():
    return {"chain": chain.chain, "length": len(chain)}
