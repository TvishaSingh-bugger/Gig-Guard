import random

def process_payout():
    txn_id = "TXN" + str(random.randint(10000,99999))
    return f"₹500 credited | ID: {txn_id}"