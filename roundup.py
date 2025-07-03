# roundup.py
class RoundUpSaver:
    def __init__(self, threshold_cents: int, granularity: int = 100):
        self.threshold = threshold_cents       # e.g. 500
        self.g = granularity                   # typically 100 cents
        self.pool = 0                          # in cents
        self.savings = 0                       # in cents

    def record_transaction(self, amount_cents: int):
        # 1. Compute how many cents to next 'g' multiple:
        rem = amount_cents % self.g
        delta = (self.g - rem) if rem != 0 else 0

        # 2. Accumulate
        self.pool += delta

        # 3. Transfer every time pool >= threshold
        blocks = self.pool // self.threshold
        if blocks:
            self.savings += blocks * self.threshold
            self.pool    -= blocks * self.threshold

    def status(self):
        return {'pool': self.pool, 'savings': self.savings}
