def grade_calculator(student, score):
    
    print("Student:", student)
    print("Score:", score) 

    if score > 100 or score < 0:
        print("Invalid score")
    else:
        if score >= 90:
            print("Grade A")
        elif score >= 80:
            print("Grade B")
        elif score >= 70:
            print("Grade C")
        elif score >= 60:
            print("Grade D")
        else :
            print("F") 

student = input("Enter your name:")
grade = int(input("Enter your grade:"))
grade_calculator(student, grade)  
