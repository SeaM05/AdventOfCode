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

def count_occurrences(grid, word="XMAS"):
    """Count all occurrences of the word in the grid in all directions."""
    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    rows, cols, word_len, count = len(grid), len(grid[0]), len(word), 0

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                if all(
                    is_valid(r + dr * k, c + dc * k) and grid[r + dr * k][c + dc * k] == word[k]
                    for k in range(word_len)
                ):
                    count += 1
    return count

def count_x_mas(grid):
    """Count all occurrences of X-MAS in the grid."""
    rows, cols = len(grid), len(grid[0])
    count = 0

    # Define the set of valid characters in the diagonals
    valid_chars = {"M", "S"}

    for r in range(1, rows - 1):
        for c in range(1, cols - 1):
            # Check if the current position is the center 'A' of an X-MAS
            if grid[r][c] == "A":
                # Check diagonals
                if (
                    {grid[r - 1][c - 1], grid[r + 1][c + 1]} == valid_chars and  # Top-left to bottom-right diagonal
                    {grid[r - 1][c + 1], grid[r + 1][c - 1]} == valid_chars    # Top-right to bottom-left diagonal
                ):
                    count += 1

    return count

if __name__ == "__main__":
    year, day = 2024, 4
    input_data = get_input(year, day)
    grid = input_data.splitlines()
    print("Part 1 - Total occurrences:", count_occurrences(grid))
    print("Part 2 - Total X-MAS occurrences:", count_x_mas(grid))