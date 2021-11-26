import pytest

def sum(x):
    return x + 10

def test_sum_01():
    assert sum(3) == 13