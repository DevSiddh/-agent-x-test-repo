# main.py
import random

def process_transaction(amount):
    # Logic: Only apply a high-value flag if the amount is over 100
    if amount > 100:
        is_high_value = True
        print(f"Processing large amount: {amount}")
    
    # This will fail if amount <= 100 because 'is_high_value' was never defined
    if is_high_value:
        return amount * 0.95  # Apply 5% discount
    
    return amount

if __name__ == "__main__":
    # Test case that works
    print(f"Result 1: {process_transaction(150)}")
    
    # Test case that triggers the Runtime Error
    print(f"Result 2: {process_transaction(50)}")
