import random, time
from roundup import RoundUpSaver

def benchmark(n=10**6, threshold=500):
    saver = RoundUpSaver(threshold_cents=threshold)
    t0 = time.perf_counter()
    for _ in range(n):
        amt = random.randint(1, 10_000_00)  # up to $10,000.00
        saver.record_transaction(amt)
    t1 = time.perf_counter()
    print(f"{n/(t1-t0):.0f} tx/sec")

if __name__ == "__main__":
    benchmark()
