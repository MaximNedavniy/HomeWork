import os
import pytest
from ..task1 import MyContextManager


def test_1():
    path="HW21/tests/testfile.json"
    if os.path.exists(path):
        with MyContextManager(path, "r") as file:
            result = file.read()
        assert result == "Hello"
    else:
        with pytest.raises(FileNotFoundError):
            print("FileNotFoundError")
            with MyContextManager(path, "r") as file:
                result = file.read()

