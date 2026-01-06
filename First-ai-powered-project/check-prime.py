"""
Prime Number Checker

This module provides an optimized function to check if a number is prime.
A prime number is a natural number greater than 1 that has no positive
divisors other than 1 and itself.

Example:
    >>> is_prime(17)
    True
    >>> is_prime(15)
    False
"""
import math
from typing import Union


def is_prime(n: Union[int, float]) -> bool:
    """
    Check if a number is prime using an optimized algorithm.
    
    This function uses several optimizations to efficiently determine
    if a number is prime:
    1. Early rejection of numbers < 2 (primes must be >= 2)
    2. Quick handling of the smallest primes (2 and 3)
    3. Early rejection of even numbers > 2
    4. Only checking odd divisors (reduces iterations by ~50%)
    5. Only checking divisors up to sqrt(n) (mathematical property)
    
    Args:
        n: The number to check. Can be int or float, but will be
           converted to int for checking.
    
    Returns:
        True if n is prime, False otherwise.
    
    Examples:
        >>> is_prime(2)
        True
        >>> is_prime(4)
        False
        >>> is_prime(97)
        True
        >>> is_prime(100)
        False
        >>> is_prime(0)
        False
        >>> is_prime(-5)
        False
    """
    # Convert to int if float (e.g., 7.0 -> 7)
    n = int(n)
    
    # Primes must be >= 2
    # Reject negative numbers, 0, and 1
    if n < 2:
        return False
    
    # Handle the smallest primes (2 and 3) as special cases
    # These are the only even prime and the smallest odd prime
    if n == 2 or n == 3:
        return True
    
    # All even numbers > 2 are composite (divisible by 2)
    # This early check eliminates half of all numbers immediately
    if n % 2 == 0:
        return False
    
    # For odd numbers > 3, check divisibility by odd divisors only
    # We only need to check up to sqrt(n) because:
    # - If n has a divisor > sqrt(n), it must also have one < sqrt(n)
    # - Example: 100 = 10 * 10, so checking up to 10 is sufficient
    sqrt_n = math.isqrt(n)  # Integer square root (faster than int(n**0.5))
    
    # Check odd divisors starting from 3, stepping by 2 to skip even numbers
    # This reduces the number of iterations by approximately 50%
    for divisor in range(3, sqrt_n + 1, 2):
        # If n is divisible by any divisor, it's not prime
        if n % divisor == 0:
            return False
    
    # If no divisors found, the number is prime
    return True


def get_user_input() -> int:
    """
    Prompt the user for a number and validate the input.
    
    Returns:
        A positive integer entered by the user.
    
    Raises:
        ValueError: If the input cannot be converted to an integer.
    """
    while True:
        try:
            user_input = input("Enter a number to check: ").strip()
            number = int(user_input)
            return number
        except ValueError:
            print(f"Error: '{user_input}' is not a valid integer. Please try again.")


def format_result(number: int, is_prime_result: bool) -> str:
    """
    Format the result of a prime number check for display.
    
    Args:
        number: The number that was checked.
        is_prime_result: The result from is_prime() function.
    
    Returns:
        A formatted string describing whether the number is prime.
    """
    if is_prime_result:
        return f"{number} is a prime number."
    else:
        return f"{number} is not a prime number."


def main() -> None:
    """
    Main function to run the prime number checker interactively.
    
    Prompts the user for a number and displays whether it is prime.
    """
    try:
        # Get and validate user input
        number = get_user_input()
        
        # Check if the number is prime
        result = is_prime(number)
        
        # Display the result
        print(format_result(number, result))
        
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        # Handle any unexpected errors
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()