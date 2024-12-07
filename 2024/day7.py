import subprocess
import sys
from functools import lru_cache
import math

def get_input(year, day):
    """Fetch the puzzle input from the get_input.py script."""
    try:
        result = subprocess.check_output(
            [sys.executable, "get_input.py", "--year", str(year), "--day", str(day)],
            text=True,
        )
        return result.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error fetching input: {e}", file=sys.stderr)
        sys.exit(1)

@lru_cache
def recursive_evaluator(result, current, numbers, part1=True):
    # check result
    if len(numbers) == 0:
        return result == current

    # early false
    if current > result:
        return False

    # Precompute digits for mathematical concatenation
    digits = math.ceil(math.log10(numbers[0] + 1)) if numbers[0] > 0 and not part1 else 1

    return (recursive_evaluator(result, current + numbers[0], numbers[1:], part1) or  # summation
            recursive_evaluator(result, current * numbers[0], numbers[1:], part1) or  # multiplication
            (not part1 and recursive_evaluator(result, current * (10 ** digits) + numbers[0], numbers[1:], part1)))  # concatenation

def main():
    year = 2024
    day = 7
    data = get_input(year, day)
    lines = data.splitlines()
    calibration = [(int(x.split(': ')[0]), tuple(map(int, x.split(': ')[1].split()))) for x in lines]

    # Part 1
    total = 0
    for res, numbers in calibration:
        if recursive_evaluator(res, numbers[0], numbers[1:]):
            total += res
    print("Part 1 - Evaluated result:", total)

    # Part 2
    total = 0
    for res, numbers in calibration:
        if recursive_evaluator(res, numbers[0], numbers[1:], False):
            total += res
    print("Part 2 - Evaluated result:", total)

if __name__ == "__main__":
    main()
