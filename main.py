from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {
        "message": "GBT backend is running",
        "token": "GBT",
        "native": True,
        "gas_policy": "Free only for GBT launch",
        "mining": "Proof-of-Work"
    }

@app.get("/token-logic")
def token_logic():
    return {
        "name": "GoldBarTether",
        "symbol": "GBT",
        "initialMint": "999 sextillion",
        "gasFreeLaunch": True,
        "infiniteSupply": True,
        "mining": "PoW",
        "gasToken": "GBT"
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=10000)

