import re
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

def mul_part1(input_data):
    """Extract valid `mul(X,Y)` instructions and calculate their total sum."""
    # Regular expression to match valid mul(X,Y) instructions
    pattern = r"mul\((\d+),(\d+)\)"

    total_sum = 0

    # Find all matches for valid mul(X,Y) instructions
    matches = re.findall(pattern, input_data)
    for x, y in matches:
        total_sum += int(x) * int(y)

    return total_sum

def mul_part2(input_data):
    """Extract valid `mul(X,Y)` instructions considering `do()` and `don't()` instructions."""
    # Regular expression to match valid mul(X,Y) instructions
    mul_pattern = r"mul\((\d+),(\d+)\)"

    total_sum = 0
    enabled = True  

    # Split the input into tokens for processing
    tokens = re.split(r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))', input_data)

    for token in tokens:
        if not token.strip():
            continue

        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False

        elif "mul(" in token and enabled:
            match = re.match(mul_pattern, token)
            if match:
                x, y = match.groups()
                total_sum += int(x) * int(y)

    return total_sum

if __name__ == "__main__":
    year = 2024
    day = 3

    # Fetch the puzzle input
    input_data = get_input(year, day)

    total_sum_part1 = mul_part1(input_data)
    print("Part 1 - Total Sum of Valid mul Instructions:", total_sum_part1)

    total_sum_part2 = mul_part2(input_data)
    print("Part 2 - Total Sum of Valid mul Instructions (with conditions):", total_sum_part2)
