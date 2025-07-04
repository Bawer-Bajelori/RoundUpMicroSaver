# smoketest.py

import time
from roundup import RoundUpSaver

def main():
    saver = RoundUpSaver(threshold_cents=100, granularity=100)
    N = 10_000_000
    start = time.time()
    for i in range(N):
        # simulate a variety of purchase amounts
        saver.record_transaction(i % 1000)
    elapsed = time.time() - start
    print(f"{N/elapsed:.0f} tx/sec")

if __name__ == "__main__":
    main()
