# interactive_roundup.py

from roundup import RoundUpSaver

def main():
    print("=== RUMS Interactive Demo ===")

    threshold = int(input("Enter transfer threshold in cents (e.g. 100): "))
    granularity = int(input("Enter rounding granularity in cents (e.g. 100): "))
    saver = RoundUpSaver(threshold_cents=threshold, granularity=granularity)

    print("\nType amounts like 3.47, or 'q' to quit.\n")
    while True:
        amt = input("Amount > ")
        if amt.lower() in ("q", "quit"):
            break
        try:
            cents = int(float(amt) * 100)
        except ValueError:
            print("  ❗ Please enter a number like 2.99 or 'q' to quit.")
            continue

        saver.record_transaction(cents)
        st = saver.status()
        print(f"  • Pool:    ${st['pool']/100:.2f}")
        print(f"  • Savings: ${st['savings']/100:.2f}\n")

    print("Final status:", saver.status())

if __name__ == "__main__":
    main()
