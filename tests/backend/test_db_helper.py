import pytest
from backend import db_helper

def test_fetch_expenses_for_date():

    expenses = db_helper.fetch_expenses_for_date("2024-009-03")

    assert len(expenses) == 4
