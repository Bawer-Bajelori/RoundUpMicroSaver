import pytest
from roundup import RoundUpSaver

def test_simple_pooling():
    # granularity = $1, threshold = $5
    saver = RoundUpSaver(threshold_cents=500, granularity=100)
    saver.record_transaction(250)   # $2.50 → delta = 50¢
    assert saver.status() == {'pool': 50, 'savings': 0}

def test_threshold_crossing():
    saver = RoundUpSaver(threshold_cents=200, granularity=100)
    # two purchases of $1.75 each: each → delta=25¢, pool 25→50, still below 200¢
    saver.record_transaction(175)
    saver.record_transaction(175)
    assert saver.status() == {'pool': 50, 'savings': 0}
    # third purchase: pool 50+25=75; still below
    saver.record_transaction(175)
    assert saver.status() == {'pool': 75, 'savings': 0}

def test_transfer_when_threshold_reached():
    saver = RoundUpSaver(threshold_cents=200, granularity=100)
    # four purchases of $1.75 each: deltas 25¢ each
    for _ in range(4):
        saver.record_transaction(175)
    # pool went 25→50→75→100; still below 200
    assert saver.status() == {'pool': 100, 'savings': 0}
    # next purchase pushes pool to 125
    saver.record_transaction(175)
    # still below
    assert saver.status() == {'pool': 125, 'savings': 0}
    # two more to cross 200
    saver.record_transaction(175)  # pool 150
    saver.record_transaction(175)  # pool 175
    assert saver.status() == {'pool': 175, 'savings': 0}
    # one more to hit 200
    saver.record_transaction(175)  # pool 200 ⇒ transfer 200 to savings
    assert saver.status() == {'pool': 0, 'savings': 200}

def test_granularity_larger_than_threshold():
    # granularity = $3, threshold = $2
    saver = RoundUpSaver(threshold_cents=200, granularity=300)
    saver.record_transaction(150)  # delta = 150 (to get up to 300)
    # pool = 150, threshold = 200 → no transfer
    assert saver.status() == {'pool': 150, 'savings': 0}
