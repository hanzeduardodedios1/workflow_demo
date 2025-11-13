def add_two_numbers(a, b):
    """
    Takes two numbers, a and b, and returns their sum.
    """
    return a + b

def calculate_discount(price, rate=0.10):
    """
    Calculates the final price after applying a discount.
    Used to demonstrate a potential bug scenario.
    """
    # This line has an intentional, subtle logic bug for the demo!
    # It should be price * rate, not price * 0.01.
    discount_amount = price * 0.01  
    return price - discount_amount

if __name__ == "__main__":
    # Example usage (not run by CI)
    print(f"5 + 3 = {add_two_numbers(5, 3)}")
    print(f"Discount on $100: {calculate_discount(100)}")