
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
LETTER_GRADES = ("A", "B", "C", "D", "F")

# choosing actions
def action_choice():
    valid_value = False
    while not valid_value:
        action = input("What would you like to do with the gradebook?\n   View\n   Edit\n   Exit\n").strip().lower()
        if action == "view":
            valid_value = True
            print("")
            # display_summary()
            continue
        elif action == "edit":
            valid_value = True
            print("")
            edit_gradebook()
        elif action == "exit":
            valid_value = True
            print("")

# calculate average grades + assign letter grade

# show the gradebook summary

# add/remove students or grades
def edit_gradebook():
    global grade_book
    valid_value = False
    while not valid_value:
        action = input("What would you like to do?\n   Add Student\n   Remove Student\n   Add Grade\n   Remove Grade\n   Return\n").strip().lower()
        if action == "add student":
            new_student = input("What is the new student's name?\n").strip()
            grade_book[new_student] = []
            print(f"{new_student} has been added to the gradebook.")
            print("")
        elif action == "remove student":
            student = input("Which student would you like to remove?\n").strip()
            if student in grade_book.keys():
                grade_book.pop(student)
                print(f"{student} and their grades have been removed from the gradebook.")
            else:
                print(f"{student} does not exist in the gradebook.")
            print("")
        elif action == "add grade":
            continue
        elif action == "remove grade":
            continue
        elif action == "return":
            print("")
            action_choice()
        else:
            print("That is not a valid choice. Please spell your choice correctly and use exactly one space in between the words.")
            print("")


action_choice()