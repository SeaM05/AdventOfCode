import subprocess
import sys
from functools import cmp_to_key

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

def comp(x, y):
    """Comparison function based on the ordering rules."""
    if x == y:
        return 0
    if x in order and y in order[x]:
        return -1
    if y in order and x in order[y]:
        return 1
    return 0

def is_correct(update):
    """Check if the update is in the correct order based on the rules."""
    return update == sorted(update, key=cmp_to_key(comp))

def main():
    input_data = get_input(year=2024, day=5)

    inputParts = input_data.split("\n\n")
    rules = inputParts[0].split("\n")
    global order
    order = {}

    for rule in rules:
        key, value = rule.split("|")
        order.setdefault(key, []).append(value)

    updates = [update.split(",") for update in inputParts[1].split("\n")]

    # Part 1: Sum of middle page numbers from correctly ordered updates
    correctMidEntries = [update[len(update) // 2] for update in updates if is_correct(update)]
    sum1 = sum(int(x) for x in correctMidEntries)
    print("Part 1 - Total middle pages:",sum1)

    # Part 2: Sum of middle page numbers from sorted incorrectly ordered updates
    sortedIncorrectUpdates = [sorted(update, key=cmp_to_key(comp)) for update in updates if not is_correct(update)]
    incorrectMiddleEntries = [update[len(update) // 2] for update in sortedIncorrectUpdates]
    sum2 = sum(int(x) for x in incorrectMiddleEntries)
    print("Part 2 - Fixed middle pages:",sum2)

if __name__ == "__main__":
    main()
