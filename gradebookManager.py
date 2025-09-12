
#make dictionary (key = name, alue = list of grades)
    # min 3 students, min 3 grades per
# allow user to:
    # add/remove students
    # add/remove grades
    # view gradebook summary (view display)
# calculate average grade for each student
    # print student w/ highest grade (part of summary)
    # sort students by average grade
# display gradebook summary
    # show each student, grades, and average; display letter grades based on averages

grade_book = {"Billy":[90, 89, 95], "Bob":[69, 99, 86], "Joe":[100, 42, 98,]}
# grade_book_averages = {"Billy":(,), "Bob":(,), "Joe":(,)}
student_standings = ["Billy", "Bob", "Joe"]
grade_book_averages = [(), (), ()]
# //////////////////////////////////////////////////////////////////////////////////////need to fix, split into two lists to sort maybe?
LETTER_GRADES = ("A", "B", "C", "D", "F")
GRADE_MIN = 0
GRADE_MAX = 100

# choosing actions
def action_choice():
    valid_value = False
    while not valid_value:
        action = input("What would you like to do with the gradebook?\n   View\n   Edit\n   Exit\n").strip().lower()
        print("")
        if action == "exit":
            valid_value = True
            print("Goodbye")
            print("")
        elif action == "edit":
            valid_value = True
            edit_gradebook()
        elif action == "view":
            valid_value = True
            # display_summary()
            continue
        else:
            print("That is not a valid choice. Please spell your choice correctly.")
            print("")

# calculate average grades + assign letter grade
def calculate(student):
    global grade_book_averages
    grade_total = 0
    for i in grade_book[student]:
        grade_total += i
    num_grades = len(grade_book[student])
    grade_average = grade_total / num_grades
    if (grade_average <= GRADE_MAX) and (grade_average >= 90):
        grade_letter = LETTER_GRADES[0]
    elif grade_average >= 80:
        grade_letter = LETTER_GRADES[1]
    elif grade_average >= 70:
        grade_letter = LETTER_GRADES[2]
    elif grade_average >= 60:
        grade_letter = LETTER_GRADES[3]
    else:
        grade_letter = LETTER_GRADES[4]
    # grade_book_averages[student] = (grade_average, grade_letter)////////////////////////////////////////////////////////////////////////////////

# loop through and compare averages, sort?
def sort_grades():
    for student in grade_book.keys():
        calculate(student)
    

# show the gradebook summary
# def display_summary():

# add/remove students or grades
def edit_gradebook():
    global grade_book, grade_book_averages
    valid_value = False
    while not valid_value:
        action = input("What would you like to do?\n   Add Student\n   Remove Student\n   Add Grade\n   Remove Grade\n   Return\n").strip().lower()
        print("")
        if action == "add student":
            new_student = input("What is the new student's name?\n").strip()
            grade_book[new_student] = []
            # grade_book_averages[new_student] = (,)////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            print(f"{new_student} has been added to the gradebook.")
            print("")
        elif action == "remove student":
            student = input("Which student would you like to remove?\n").strip()
            if student in grade_book.keys():
                grade_book.pop(student)
                print(f"{student} and their grades have been removed from the gradebook.")
            else:
                print(f"{student} does not exist in the gradebook. Cancelling action.")
            print("")
        elif action == "add grade":
            which_student = input("Which student would you like to add grades to?\n").strip()
            if which_student in grade_book.keys():
                try:
                    grade_to_add = int(input("What is the grade that you would like to add?\n").strip())
                    if (grade_to_add >= GRADE_MIN) and (grade_to_add <= GRADE_MAX):
                        grade_book[which_student] = grade_to_add
                    else:
                        print(f"{grade_to_add} is outside of the valid range. Cancelling action.")
                except:
                    print("That value is not an integer. Cancelling action.")
            else:
                print(f"{which_student} is not in the gradebook. Cancelling action.")
            print("")
        elif action == "remove grade":
            oops_student = input("Which student would you like to remove grades from?\n").strip()
            if oops_student in grade_book.keys():
                grade_length = len(grade_book[oops_student])
                if grade_length != 0:
                    for i in range(grade_length):
                        print(f"{i}: {grade_book[oops_student][i]}")
                    try:
                        grade_index = int(input("Please input the index of the grade you would like to remove.\n"))
                        if (grade_index >= 0) and (grade_index <= grade_length -1):
                            grade_book[oops_student].pop(grade_index)
                        else:
                            print(f"{grade_index} is outside of the grade range. Cancelling action.")
                    except:
                        print("That value is not an integer. Cancelling action.")
                else:
                    print(f"{oops_student} doesn't have any grades yet. Cancelling action.")
            else:
                print(f"{oops_student} is not in the gradebook. Cancelling action.")
            print("")
        elif action == "return":
            valid_value = True
            print("")
            action_choice()
        else:
            print("That is not a valid choice. Please spell your choice correctly and use exactly one space in between the words.")
            print("")

# code that runs down below
action_choice()