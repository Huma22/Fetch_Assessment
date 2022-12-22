import datetime
from sqlite3 import Timestamp
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

# Define request and response models
class TransactionRequest(BaseModel):
    payer: str = Field(..., example='DANNON')
    points: int = Field(..., example=300)
    timestamp: datetime.datetime = Field(..., example='2022-10-31T10:00:00Z')

class SpendRequest(BaseModel):
    points: int = Field(..., example=5000)

class PayerPoints(BaseModel):
    payer: str
    points: int


# Define in-memory storage for transactions
transactions = []
ls = []

# Define in-memory storage for spent points
spent_total = []

payer_totals = {}

# Define routes
@app.post("/add-transaction/")
def add_transaction(request: TransactionRequest):
    # Add the transaction to the system
    payer = request.payer
    points = request.points
    timestamp = request.timestamp
    transactions.append({"payer": payer, "points": points, "timestamp": timestamp})

@app.get("/get-transactions")
def get_transactions():
    return transactions

@app.post("/spend-points/")
def spend_points(request: SpendRequest):
    # Spend the points according to the rules specified in the problem statement
    points = request.points
    spent_points = []
    spent_points_by_payer = {}
    remaining_points = points
    # Sort the transactions by timestamp
    sorted_transactions = sorted(transactions, key=lambda t: t["timestamp"])
    # Iterate through the transactions and spend the points
    total_points = 0
    n = 0
    for transaction in sorted_transactions:
        total_points += transaction["points"]
        n += 1
        if total_points >= points:
            break

    for transaction in sorted_transactions[:n]:
        payer = transaction["payer"]
        points = transaction["points"]
        if payer not in payer_totals:
            payer_totals[payer] = 0
        payer_totals[payer] += points
    for key in payer_totals:
        ls.append({"payer": key, "points": payer_totals[key]})
    # TODO: NEED to find a way to add all the values in the dict based on the user name or anyother unique id
    for transaction in ls:
        payer = transaction["payer"]
        payer_points = transaction["points"]
        if payer not in spent_points_by_payer:
            spent_points_by_payer[payer] = 0
        if payer_points < 0:
            # Skip payer if they are negative balance 
            continue
        elif payer_points > 0:
            # Spend the points from this payer if there are any remaining and the payer's balance is positive
            spent_points = min(remaining_points, payer_points)
            remaining_points -= spent_points
            spent_points_by_payer[payer] += spent_points
            transaction["points"] -= spent_points
        if remaining_points == 0:
            break
    spent_total = [{"payer": payer, "points": -1 * spent_points} for payer, spent_points in spent_points_by_payer.items()]
    
    return spent_total

@app.get("/points-balance/")
def points_balance():
    return ls

