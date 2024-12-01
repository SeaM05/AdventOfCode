import subprocess
import sys
from collections import Counter

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

def calculate_total_distance(input_data):
    """Calculate the total distance between the sorted left and right lists."""
    left_list, right_list = [], []
    for line in input_data.strip().split('\n'):
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    left_list.sort()
    right_list.sort()
    
    total_distance = sum(abs(l - r) for l, r in zip(left_list, right_list))
    return total_distance

def calculate_similarity_score(input_data):
    """Calculate the similarity score between the two lists."""
    left_list, right_list = [], []
    
    for line in input_data.strip().split('\n'):
        left, right = map(int, line.split())
        left_list.append(left)
        right_list.append(right)
    
    right_count = Counter(right_list)
    
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_count.get(num, 0)
    
    return similarity_score

if __name__ == "__main__":
    year = 2024
    day = 1

    input_data = get_input(year, day)

    # Part 1
    total_distance = calculate_total_distance(input_data)
    print("Total Distance:", total_distance)

    #Part 2
    similarity_score = calculate_similarity_score(input_data)
    print("Similarity Score:", similarity_score)
