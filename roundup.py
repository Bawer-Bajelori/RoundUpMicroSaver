# roundup.py

class RoundUpSaver:
    def __init__(self, threshold_cents: int, granularity: int = 100):
        self.threshold = threshold_cents  # e.g. 500
        self.g = granularity              # e.g. 100¢
        self.pool = 0
        self.savings = 0

    def record_transaction(self, amount_cents: int):
        # delta = how much to round up to the next multiple of g
        self.pool += (-amount_cents) % self.g

        # transfer out every full threshold in pool
        transferred = (self.pool // self.threshold) * self.threshold
        self.savings += transferred
        self.pool -= transferred

    def status(self):
        return {'pool': self.pool, 'savings': self.savings}
