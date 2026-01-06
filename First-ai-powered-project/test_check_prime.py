import pytest
import importlib.util
import sys

# Import module with hyphen in filename
spec = importlib.util.spec_from_file_location("check_prime", "check-prime.py")
check_prime = importlib.util.module_from_spec(spec)
sys.modules["check_prime"] = check_prime
spec.loader.exec_module(check_prime)

is_prime = check_prime.is_prime


class TestIsPrime:
    """Test cases for the is_prime function."""

    def test_small_prime_numbers(self):
        """Test small prime numbers."""
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True
        assert is_prime(17) is True
        assert is_prime(19) is True
        assert is_prime(23) is True

    def test_small_non_prime_numbers(self):
        """Test small non-prime numbers."""
        assert is_prime(1) is False
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False
        assert is_prime(12) is False
        assert is_prime(14) is False
        assert is_prime(15) is False
        assert is_prime(16) is False

    def test_edge_cases(self):
        """Test edge cases."""
        assert is_prime(0) is False
        assert is_prime(-1) is False
        assert is_prime(-5) is False

    def test_larger_prime_numbers(self):
        """Test larger prime numbers."""
        assert is_prime(29) is True
        assert is_prime(31) is True
        assert is_prime(37) is True
        assert is_prime(41) is True
        assert is_prime(97) is True
        assert is_prime(101) is True

    def test_larger_non_prime_numbers(self):
        """Test larger non-prime numbers."""
        assert is_prime(25) is False  # 5 * 5
        assert is_prime(27) is False  # 3 * 9
        assert is_prime(49) is False  # 7 * 7
        assert is_prime(100) is False  # 10 * 10
        assert is_prime(121) is False  # 11 * 11

    def test_perfect_squares(self):
        """Test perfect squares (should not be prime)."""
        assert is_prime(4) is False  # 2^2
        assert is_prime(9) is False  # 3^2
        assert is_prime(16) is False  # 4^2
        assert is_prime(25) is False  # 5^2
        assert is_prime(36) is False  # 6^2

    def test_very_large_numbers(self):
        """Test very large numbers to verify optimization works correctly."""
        # Large primes
        assert is_prime(99991) is True
        assert is_prime(999983) is True
        # Large non-primes
        assert is_prime(99990) is False  # Even number
        assert is_prime(999981) is False  # Divisible by 3
        assert is_prime(1000000) is False  # Even number

