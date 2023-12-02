def calculate_calibration_sum(calibration_text):
    calibration_sum = 0
    # Split the calibration text into lines
    lines = calibration_text.splitlines()

    # Iterate through each line
    for line in lines:
        # Extract all numbers from the line and concatenate them
        concatenated_number = ''.join(char for char in line if char.isdigit())

        # If there is a concatenated number, add the sum of the first and last digits to the calibration sum
        if concatenated_number:
            calibration_sum += int(concatenated_number[0]) * 10 + int(concatenated_number[-1])
            print(int(concatenated_number[0]) * 10 + int(concatenated_number[-1]))
    return calibration_sum

# Open the file and read its content
with open("day 1\input.txt", "r") as f:
    # Read the content of the file
    calibration_text = f.read()

# Get calibration sum
result = calculate_calibration_sum(calibration_text)

# Display the result
print(f"The sum of all calibration values is: {result}")
