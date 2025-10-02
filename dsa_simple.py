#!/usr/bin/env python3
"""
Simple DSA comparison for MoMo assignment (Task #5)
Linear search vs Dictionary lookup
"""

import random
import time
import json

# Sample data generator
def generate_sample(n=200):
    txs = []
    for i in range(1, n+1):
        txs.append({
            'id': f"tx_{i}",
            'type': random.choice(['PAYMENT','P2P','AIRTIME']),
            'amount': round(random.uniform(1,1000),2),
            'sender': f"sender_{random.randint(1,50)}",
            'receiver': f"receiver_{random.randint(1,50)}",
            'timestamp': f"2025-01-01T00:{i%60:02d}:00"
        })
    return txs

# Linear search O(n)
def linear_search(tx_list, target_id):
    for tx in tx_list:
        if tx['id'] == target_id:
            return tx
    return None

# Dict lookup O(1)
def build_index(tx_list):
    return {tx['id']: tx for tx in tx_list}

def dict_lookup(tx_index, target_id):
    return tx_index.get(target_id)

# Timing utility
def time_search(fn, *args):
    t0 = time.perf_counter()
    fn(*args)
    t1 = time.perf_counter()
    return t1-t0

def main():
    tx_list = generate_sample(200)
    tx_index = build_index(tx_list)
    sample_ids = [f"tx_{i}" for i in random.sample(range(1,201), 20)]
    linear_times, dict_times = [], []

    for sid in sample_ids:
        linear_times.append(time_search(linear_search, tx_list, sid))
        dict_times.append(time_search(dict_lookup, tx_index, sid))

    avg_linear = sum(linear_times)/len(linear_times)
    avg_dict = sum(dict_times)/len(dict_times)

    print("\n--- DSA Comparison: Linear Search vs Dictionary Lookup ---")
    print(f"Average linear search time: {avg_linear*1e6:.3f} µs")
    print(f"Average dict lookup time:   {avg_dict*1e6:.3f} µs")
    speedup = avg_linear/avg_dict
    print(f"Dictionary lookup is ~{speedup:.1f}x faster on average\n")

    # Save JSON results
    with open("dsa_timing_results.json","w") as f:
        json.dump({
            "avg_linear": avg_linear,
            "avg_dict": avg_dict,
            "speedup": speedup
        }, f, indent=2)

if __name__ == "__main__": main()
