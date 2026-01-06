#!/bin/bash
# Test runner script that suppresses langsmith/pydantic warnings
# Usage: ./run_tests.sh [pytest arguments]

export PYTHONWARNINGS="ignore::UserWarning"
python3 -m pytest "$@"

