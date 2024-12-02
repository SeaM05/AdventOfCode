import subprocess
import sys

def get_input(year, day):
    """Call get_input.py to fetch the puzzle input."""
    try:
        result = subprocess.check_output(
            [sys.executable, "get_input.py", "--year", str(year), "--day", str(day)],
            text=True,
        )
        return result.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error fetching input: {e}", file=sys.stderr)
        sys.exit(1)

def is_safe_report(levels):
    """
    Check if a report is safe.
    A report is safe if:
    1. Levels are either all increasing or all decreasing.
    2. Any two adjacent levels differ by at least 1 and at most 3.
    """
    differences = [levels[i + 1] - levels[i] for i in range(len(levels) - 1)]

    # Check if all differences are either positive or negative
    all_increasing = all(d > 0 for d in differences)
    all_decreasing = all(d < 0 for d in differences)

    # Check if differences are within the range [1, 3]
    within_range = all(1 <= abs(d) <= 3 for d in differences)

    return (all_increasing or all_decreasing) and within_range

def is_safe_with_dampener(levels):
    """
    Check if a report can be made safe by removing a single bad level.
    """
    for i in range(len(levels)):
        # Remove the i-th level and check if the remaining levels are safe
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe_report(modified_levels):
            return True
    return False

def analyze_reports(input_data):
    """
    Analyze reports to count the number of safe reports for both parts:
    - Part One: Directly safe reports
    - Part Two: Reports made safe by the Problem Dampener
    """
    safe_count_part_one = 0
    safe_count_part_two = 0

    for line in input_data.strip().split('\n'):
        levels = list(map(int, line.split()))

        # Check if the report is safe (Part One)
        if is_safe_report(levels):
            safe_count_part_one += 1
            safe_count_part_two += 1  # Inherently safe reports count for Part Two as well
        # Check if the report can be made safe with the dampener (Part Two)
        elif is_safe_with_dampener(levels):
            safe_count_part_two += 1

    return safe_count_part_one, safe_count_part_two

if __name__ == "__main__":
    year = 2024
    day = 2

    # Fetch input using get_input.py
    input_data = get_input(year, day)

    # Analyze reports
    safe_part_one, safe_part_two = analyze_reports(input_data)

    print("Number of Safe Reports (Part One):", safe_part_one)
    print("Number of Safe Reports (Part Two, with Problem Dampener):", safe_part_two)
