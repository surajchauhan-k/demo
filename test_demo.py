import pytest
import demo
def test_add_positive_integers():
    result = demo.add_2(2, 3)
    assert result == 5

def test_add_positive_integer_and_float():
    result = demo.add_2(2, 3.5)
    assert result == 5.5