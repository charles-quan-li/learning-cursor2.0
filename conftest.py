"""Pytest configuration to suppress langsmith/pydantic warnings."""
import warnings
import sys

# Suppress all UserWarnings early (before langsmith imports)
# This prevents the Pydantic V1 compatibility warning with Python 3.14+
if sys.version_info >= (3, 14):
    warnings.filterwarnings("ignore", category=UserWarning)

