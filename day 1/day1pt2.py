def findnum(line):
    x = -1
    if    ("one") in line: x = 1  
    elif   ("two")in line: x= 2  
    elif  ("three")in line:x= 3  
    elif  ("four")in line: x= 4 
    elif  ("five")in line: x= 5  
    elif  ("six")in line: x= 6 
    elif  ("seven")in line: x= 7 
    elif  ("eight")in line: x= 8 
    elif  ("nine")in line: x= 9

    return x
       
def calculate_calibration_sum(calibration_text):
    calibration_sum = 0
    # Split the calibration text into lines
    lines = calibration_text.splitlines()
    # Iterate through each line
    for line in lines:
        concatenated_number = ""
        word = ""
        for char in line:
            if char.isdigit():
                concatenated_number += char
            else:
                word += char
                if findnum(word) != -1:
                    concatenated_number += str(findnum(word))
        
        #print(int(concatenated_number[0]) * 10 + int(concatenated_number[-1]))
        # If there is a concatenated number, add the sum of the first and last digits to the calibration sum
      
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
