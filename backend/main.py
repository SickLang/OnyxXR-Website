from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

app = FastAPI()

# Enable CORS so Unity (Quest 3) can POST from different origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Data Models ---
class SieveResultData(BaseModel):
    patientNumber: int
    expectedTag: int
    actualTag: int

class SortResultData(BaseModel):
    patientNumber: int
    sortTagExpected: int
    sortTagActual: int
    gcsExpected: int
    rrExpected: int
    bpExpected: int
    gcsActual: int
    rrActual: int
    bpActual: int

class SieveWrapper(BaseModel):
    items: List[SieveResultData]

class SortWrapper(BaseModel):
    items: List[SortResultData]

# --- Data Storage ---
sieve_results = []
sort_results = []

# --- Endpoints ---
@app.post("/submit-sieve/")
async def submit_sieve(data: SieveWrapper):
    print("\n--- SIEVE RESULTS ---")
    for item in data.items:
        sieve_results.append(item.dict())
    return {"status": "ok", "received": len(data.items)}

@app.post("/submit-sort/")
async def submit_sort(data: SortWrapper):
    print("\n--- SORT RESULTS ---")
    for item in data.items:
        sort_results.append(item.dict())
    return {"status": "ok", "received": len(data.items)}

# --- GET Endpoints for Frontend ---
@app.get("/sieve-results")
async def get_sieve_results():
    return sieve_results

@app.get("/sort-results")
async def get_sort_results():
    return sort_results

# --- Test root ---
@app.get("/")
def root():
    return {"message": "FastAPI up and running for XR training!"}


if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port=8000)
