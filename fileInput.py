# take in a file of grades and output the corresponding letter grades with comments


def gradeCalculator(grade):
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
        

x = input("Do you want to input grades via file or manually? (file/manual): ").strip().lower()
if x == 'manual':
    while True:
        try:
            grade = float(input("What is your grade in math beta? "))
            gradeCalculator(grade)
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")
        
        restart = input("Do you want to calculate another grade? (yes/no): ").strip().lower()
        if restart != 'yes':
            break
else:
    file = input("Enter the filename containing grades: ")
    try:
        with open(file, 'r') as f:
            grades = f.readlines()
            for line in grades:
                try:
                    grade = float(line.strip())
                    print(f"Grade: {grade}")
                    gradeCalculator(grade)
                except ValueError:
                    print(f"Invalid grade entry: {line.strip()}")
    except FileNotFoundError:
        print(f"File not found: {file}")
        
        