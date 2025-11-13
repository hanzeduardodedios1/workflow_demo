def add_two_numbers(a, b):
    """
    Takes two numbers, a and b, and returns their sum.
    """
    return a + b

def calculate_discount(price, rate=0.10):
    """
    Calculates the final price after applying a discount.
    
    This function contains a known bug: it currently only applies a 1% 
    discount regardless of the 'rate' argument.
    """
    # BUG: This calculation uses a fixed 0.01 (1%) instead of the variable 'rate'.
    discount_amount = price * 0.01  
    return price - discount_amount

if __name__ == "__main__":
    print(f"5 + 3 = {add_two_numbers(5, 3)}")
    print(f"Discount on $100 (10% expected): {calculate_discount(100)}")