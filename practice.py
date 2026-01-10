# Input is a decimal number
# Output is a char
# if the grade is 90 or above then the letter should be an A
# if the grade is 80 and below 89 then the letter should be B
# if the grade is 70 and below 79 then the letter should be C
# if the grade is 60 and below 69 then the letter should be D
# if the grade is 0 and below 59 then the letter should be F

def gradeCalculator():
    grade = float(input("What is your grade in math beta?"))
    if 97 <= grade <= 115:
        print("A+")
    elif 94 <= grade <= 96:
        print("A")
    elif 90 <= grade <= 93:
        print("A-")
        
    elif 87 <= grade <= 89:
        print("B+")
    elif 84 <= grade <= 86:
        print("B")
    elif 80 <= grade <= 83:
        print("B-")
        
    elif 77 <= grade <= 79:
        print("C+")
    elif 74 <= grade <= 76:
        print("C")
    elif 70 <= grade <= 73:
        print("C-")
       
    elif 67 <= grade <= 69:
        print("D+")
    elif 64 <= grade <= 66:
        print("D")
    elif 60 <= grade <= 63:
        print("D-")
        
    elif 0 <= grade <= 59:
        print("F")
    
        
    else:
        print("fake grade please try again press the play button again to try again")
        

while True:
    gradeCalculator()
    restart = input("Do you want to calculate another grade? (yes/no): ").strip().lower()
    if restart != 'yes':
        break
