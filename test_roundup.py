# tests/test_roundup.py
import pytest
from roundup import RoundUpSaver

@pytest.mark.parametrize("threshold, txs, expected", [
    # Case 1: single small tx, no transfer
    (500, [347], {'pool': 53, 'savings': 0}),
    # Case 2: two txs cross one threshold
    (100, [347, 120], {'pool':  33, 'savings': 100}),
    # Case 3: multiple blocks in one go
    (50, [23, 49, 51], {'pool': 27, 'savings': 150}),
])
def test_round_up_saver(threshold, txs, expected):
    saver = RoundUpSaver(threshold_cents=threshold)
    for amt in txs:
        saver.record_transaction(amt)
    assert saver.status() == expected
