# File for unit tests. We use the standard 'pytest' framework.

from app import add_two_numbers, calculate_discount

# --- Tests for the simple 'add_two_numbers' function (Expected to Pass) ---

def test_addition_positive():
    # Test case 1: Positive numbers
    assert add_two_numbers(5, 3) == 8

def test_addition_negative():
    # Test case 2: Negative numbers
    assert add_two_numbers(-10, 2) == -8

# --- Test for the 'calculate_discount' function (Expected to FAIL due to bug) ---

def test_discount_calculation_failure_demo():
    """
    Checks if a 10% discount is correctly applied to $100.
    This test currently fails due to the bug in app.py.
    """
    # Expected result for 10% discount on $100.
    expected_result = 90.00
    
    # Actual result from the buggy function (it applies 1% -> returns 99.00)
    actual_result = calculate_discount(100) 
    
    # This assertion will fail: 99.00 != 90.00
    assert actual_result == expected_result