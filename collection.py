#This program code prompts user for student name, a list of student grades
# and displays the student's name, calculated average grade, and letter grade
student = input("Enter the name of the student: ")
grades = input("Enter the grades separated by a space: ")

# function to determine grade average
def calculate_grade_average(grades):
    grades = grades.split()
    grades = [int(grade) for grade in grades]
    if not grades: # raise alert and return 0
      return 0
    return (sum(grades) / len(grades))


# call to function that calculates average grade
stu_average = (calculate_grade_average(grades))

# function to determine equivalent letter grade
def assign_letter_grade(stu_average):
  if stu_average >= 90:
    return "A"
  elif stu_average >= 80:
    return "B"
  elif stu_average >= 70:
    return "C"
  elif stu_average >= 60:
    return "D"
  else:
    return "F"

# call to function that determines the equivalent letter grade
Letter_Grade = (assign_letter_grade(stu_average))

# section that displays student name, calculated average to one decimal place
# and equivalent letter grade
print("Student:", student)
print(f"Student Average: {stu_average:.1f}")
print("Letter Grade:", Letter_Grade)