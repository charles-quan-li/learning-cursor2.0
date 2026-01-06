"""Performance benchmark comparing original and optimized is_prime functions."""
import time
import math


def is_prime_original(n):
    """Original implementation."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime_optimized(n):
    """Optimized implementation."""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


def benchmark_function(func, test_numbers, iterations=1000):
    """Benchmark a function with given test numbers."""
    start = time.perf_counter()
    for _ in range(iterations):
        for num in test_numbers:
            func(num)
    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    # Test numbers of varying sizes
    test_numbers = [
        # Small numbers
        2, 3, 5, 7, 11, 13, 17, 19, 23,
        # Medium numbers
        97, 101, 997, 1009, 9973,
        # Larger numbers
        99991, 999983, 9999991,
        # Non-primes (should be fast to reject)
        4, 6, 8, 9, 10, 15, 21, 25, 27, 49, 100, 121,
    ]
    
    iterations = 10000
    
    print("=" * 60)
    print("Prime Number Checker Performance Benchmark")
    print("=" * 60)
    print(f"Testing {len(test_numbers)} numbers, {iterations} iterations each")
    print()
    
    # Benchmark original
    original_time = benchmark_function(is_prime_original, test_numbers, iterations)
    print(f"Original implementation: {original_time:.4f} seconds")
    
    # Benchmark optimized
    optimized_time = benchmark_function(is_prime_optimized, test_numbers, iterations)
    print(f"Optimized implementation: {optimized_time:.4f} seconds")
    
    # Calculate improvement
    speedup = original_time / optimized_time
    improvement = ((original_time - optimized_time) / original_time) * 100
    
    print()
    print("=" * 60)
    print(f"Speedup: {speedup:.2f}x faster")
    print(f"Improvement: {improvement:.1f}% faster")
    print("=" * 60)
    
    # Verify both implementations give same results
    print("\nVerifying correctness...")
    all_match = True
    for num in test_numbers:
        orig_result = is_prime_original(num)
        opt_result = is_prime_optimized(num)
        if orig_result != opt_result:
            print(f"ERROR: Mismatch for {num}: original={orig_result}, optimized={opt_result}")
            all_match = False
    
    if all_match:
        print("✓ All results match - optimization is correct!")

