#!/usr/bin/env python3
"""
Simple calculator program that provides add, subtract, multiply, and divide functionalities.
"""

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers (a - b)."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Returns the division of two numbers (a / b).
    Raises ValueError if divisor is zero.
    """
    if b == 0:
        raise ValueError("Error: Division by zero is not allowed.")
    return a / b

def main():
    """Main execution function demonstrating the calculator sub-functions."""
    print("=== Simple Python Calculator ===")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Run automatic tests/examples")
    print("6. Exit")

    while True:
        try:
            choice = input("\nEnter choice (1-6): ").strip()
            if choice == '6':
                print("Exiting calculator. Goodbye!")
                break
            
            if choice == '5':
                print("\n--- Running Automatic Examples ---")
                x, y = 10, 5
                print(f"Numbers: a = {x}, b = {y}")
                print(f"Add (add): {add(x, y)}")
                print(f"Subtract (subtract): {subtract(x, y)}")
                print(f"Multiply (multiply): {multiply(x, y)}")
                print(f"Divide (divide): {divide(x, y)}")
                
                # Test division by zero exception handling
                try:
                    divide(x, 0)
                except ValueError as e:
                    print(f"Division by zero test: Passed ({e})")
                continue

            if choice not in ('1', '2', '3', '4'):
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"Result: {num1} / {num2} = {result}")
                except ValueError as e:
                    print(e)

        except (KeyboardInterrupt, EOFError):
            print("\nExiting calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()
