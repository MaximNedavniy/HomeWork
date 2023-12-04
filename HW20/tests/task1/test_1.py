import pytest
from task2 import make_country
def test_func():
    assert make_country("Ukraine", "Kyiv")== {"Ukraine": "Kyiv"}


