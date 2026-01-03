# Input is a decimal number
# Output is a char
# if the grade is 90 or above then the letter should be an A
# if the grade is 80 and below 89 then the letter should be B
# if the grade is 70 and below 79 then the letter should be C
# if the grade is 60 and below 69 then the letter should be D
# if the grade is 0 and below 59 then the letter should be F

def gradeCalculator():
    grade = float(input("What is your grade in math beta?"))
    if 90 <= grade <= 115:
        print("A")
        print("Good boy")
    elif 80 <= grade <= 89:
        print("B")
        print("Dissapointment")
    elif 70 <= grade <= 79:
        print("C")
        print("CHINTO GET MY SLIPPER!")
    elif 60 <= grade <= 69:
        print("C")
        print("Actually, get my belt")
    elif 50 <= grade <= 59:
        print("D")
        print ("Beta !!!!!!")
    elif 0 <= grade <= 49:
        print("F")
        print("YOU SHALL WISH YOU WERE NEVER BORN!")
    else:
        print("fake grade please try again press the play button again to try again")
        

while True:
    gradeCalculator()
    restart = input("Do you want to calculate another grade? (yes/no): ").strip().lower()
    if restart != 'yes':
        break
