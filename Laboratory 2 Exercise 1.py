# Initialization of final grade and equivalent grade.
final_grade = 0
equivalent_grade = 0
student_name = ""

# Accepting inputs for student name, final quizzes, final research/assignment, final project, and final exam ratings
student_name = str(input("\n Enter the student's name: "))
final_quizzes = float(input("\n Enter the student's final quizzes grade: "))
final_research_assignment = float(input("\nEnter the student's final research/assignment grade: "))
final_project = float(input("\nEnter the student's final project grade: "))
final_exam = float(input("\nEnter the student's final exam grade: "))

# Setting a formula for the calculation of final grade
final_grade = (0.30 * final_quizzes) + (0.10 * final_research_assignment) + (0.40 * final_exam) + (0.20 * final_project)

# Setting the equivalent grade obtained from the final grade:
if 98 <= final_grade <= 100:
    equivalent_grade = 4.00
elif 95 <= final_grade < 98:
    equivalent_grade = 3.75
elif 92 <= final_grade < 95:
    equivalent_grade = 3.50
elif 89 <= final_grade < 92:
    equivalent_grade = 3.25
elif 86 <= final_grade < 89:
    equivalent_grade = 3.00
elif 83 <= final_grade < 86:
    equivalent_grade = 2.75
elif 80 <= final_grade < 83:
    equivalent_grade = 2.50
elif 77 <= final_grade < 80:
    equivalent_grade = 2.25
elif 74 <= final_grade < 77:
    equivalent_grade = 2.00
elif 71 <= final_grade < 74:
    equivalent_grade = 1.75
elif 68 <= final_grade < 71:
    equivalent_grade = 1.50
elif 64 <= final_grade < 68:
    equivalent_grade = 1.25
elif 60 <= final_grade < 64:
    equivalent_grade = 1.00
elif 0 <= final_grade < 60:
    equivalent_grade = 0.00
else:
    print("Invalid Input. Please Try Again.")
    exit()


# Displaying the student name, final quizzes, final research/assignment, final project, final grade, and the
# equivalent grade.
print("\nStudent Name: ", student_name)
print("\nFinal Quizzes Grade: ", round(final_quizzes, 2))
print("\nFinal Research/Assignment Grade: ", round(final_research_assignment, 2))
print("\nFinal Project Grade: ", round(final_project, 2))
print("\nFinal Grade: ", round(final_grade, 2))
print("\n Equivalent Grade: ", equivalent_grade)

# Preventing the program from closing immediately
input("\nPress Enter To Exit.")