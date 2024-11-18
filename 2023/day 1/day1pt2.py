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
  
    lines = calibration_text.splitlines()
   
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
        
      
        calibration_sum += int(concatenated_number[0]) * 10 + int(concatenated_number[-1])
        print(int(concatenated_number[0]) * 10 + int(concatenated_number[-1]))
            
    return calibration_sum


with open("day 1\input.txt", "r") as f:
   
    calibration_text = f.read()

result = calculate_calibration_sum(calibration_text)

print(f"The sum of all calibration values is: {result}")
