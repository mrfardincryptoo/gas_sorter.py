# Sort pending simulated transactions by their offering gas price
pending_txs = [
    {"id": 101, "gas_price": 18},
    {"id": 102, "gas_price": 45},
    {"id": 103, "gas_price": 32}
]

# Sort transactions in descending order based on gas_price
optimized_queue = sorted(pending_txs, key=lambda tx: tx["gas_price"], reverse=True)

print("Optimized Tx Execution Queue:")
for tx in optimized_queue:
    print(f"Tx ID: {tx['id']} | Priority Gas: {tx['gas_price']} Gwei")
