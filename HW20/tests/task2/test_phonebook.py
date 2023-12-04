from unittest.mock import patch

import phone_book as pb
import pytest
import os
import json

@pytest.fixture
def setup_temporary_directory():
    with open("dir1.json", "w"):
        yield
    os.remove("dir1.json")

def test_available_dir(setup_temporary_directory):
    assert pb.available_dir() == "dir1"


def test_add_new_entries(setup_temporary_directory):
    args = "dir1"
    first_name = "Maxim"
    last_name = "Lastov"
    number = 123456789
    city_or_state = "ExampleCity"
    pb.add_new_entries(args, first_name, last_name, number, city_or_state)
    with open(args + ".json", "r") as jfile:
        data = json.load(jfile)
        assert data[0]["first_name"] == first_name
        assert data[0]["last_name"] == last_name
        assert data[0]["full_name"] == f"{first_name} {last_name}"
        assert data[0]["number"] == str(number)
        assert data[0]["city_or_state"] == city_or_state

def test_search_not_empty(setup_temporary_directory, capsys):
    args="dir1"
    pb.add_new_entries(args, "Maxim", "Lastov", 123456789, "ExampleCity")
    search_data="Maxim"
    with open(args + ".json", "r") as jfile:
        data = json.load(jfile)
        pb.search(args, search_data)
        captured = capsys.readouterr()
        assert search_data in captured.out
def test_delete_telephone_number(setup_temporary_directory):
    args = "dir1"
    pb.add_new_entries(args, "Maxim", "Lastov", 123456789, "ExampleCity")
    search_data = 123456789
    pb.delete_telephone_number(args, search_data)
    with open(args + ".json", "r") as jfile:
        data = json.load(jfile)
        assert search_data not in data

def test_update_telephone_number(setup_temporary_directory):
    args = "dir1"
    pb.add_new_entries(args, "Maxim", "Lastov", 123456789, "ExampleCity")
    search_data = "123456789"
    with patch("builtins.input") as my_patch:
        my_patch.return_value="Max"
        pb.update_telephone_number(args, search_data, 1)
    with open(args + ".json", "r") as jfile:
        data = json.load(jfile)
        assert data[0]["first_name"] == "max"
