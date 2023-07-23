import csv

f = open("STUDENTDATA.TXT")  # open file for reading

contents = f.read()  # read file
f.close()  # close the file

list = contents.split("\n")  # split the contents of the file into a list
# print(list)  # print the list
# use len and index to parse out txt file
for i in range(len(list)):
    list[i] = list[i].split(",")
# print(list)  # print the list


def print_menu():
    print("Action Menu:")
    print("   1) Average grade for all students")
    print("   2) Average grade for each program")
    print("   3) Highest grade")
    print("   4) Lowest grade")
    print("   5) Students in MSIT")
    print("   6) Students in MSCM")
    print("   7) Students sorted by ID")
    print("   8) Show invalid records")
    print("   9) Create invalid record file")
    print("   10) Exit program\n")
    print("Enter your choice: ", end="")
    choice = int(input())
    return choice


def msit_grade(avg_msit_grade):
    if avg_msit_grade > 90 and avg_msit_grade < 100:
        grade_ltr = "A"
    elif avg_msit_grade > 80 and avg_msit_grade < 90:
        grade_ltr = "B"
    elif avg_msit_grade > 70 and avg_msit_grade < 80:
        grade_ltr = "C"
    elif avg_msit_grade > 60 and avg_msit_grade < 70:
        grade_ltr = "D"
    elif avg_msit_grade < 60:
        grade_ltr = "F"

    print("Average grade for MSIT program", grade_ltr)


def mscm_grade(avg_mscm_grade):
    if avg_mscm_grade > 90 and avg_mscm_grade < 100:
        grade_ltr = "A"
    elif avg_mscm_grade > 80 and avg_mscm_grade < 90:
        grade_ltr = "B"
    elif avg_mscm_grade > 70 and avg_mscm_grade < 80:
        grade_ltr = "C"
    elif avg_mscm_grade > 60 and avg_mscm_grade < 70:
        grade_ltr = "D"
    elif avg_mscm_grade < 60:
        grade_ltr = "F"

    print("Average grade for MSCM program", grade_ltr)


def choice1():
    total_grades = 0.0
    for student in range(len(list)):
        # student_id = list[index][0]
        avg_grade = list[student][3]
        avg_grade = float(avg_grade)
        total_grades += avg_grade
        avg_grade = total_grades / len(list)

        if avg_grade > 90 and avg_grade < 100:
            grade_ltr = "A"
        elif avg_grade > 80 and avg_grade < 89:
            grade_ltr = "B"
        elif avg_grade > 70 and avg_grade < 79:
            grade_ltr = "C"
        elif avg_grade > 60 and avg_grade < 69:
            grade_ltr = "D"
        elif avg_grade < 60:
            grade_ltr = "F"
    print("Average avg_grade for all students:", grade_ltr)


def choice2():
    total_msit_grades = 0.0
    total_mscm_grades = 0.0
    program_msit = 0
    program_mscm = 0
    for student in range(len(list)):
        program = list[student][4]
        grade = list[student][3]
        grade = float(grade)

        if program == "MSIT":
            program_msit += 1
            total_msit_grades += grade
            avg_msit_grade = total_msit_grades / program_msit
        elif program == "MSCM":
            program_mscm += 1
            total_mscm_grades += grade
            avg_mscm_grade = total_mscm_grades / program_mscm

    msit_grade(avg_msit_grade)
    mscm_grade(avg_mscm_grade)


def choice3():
    for student in range(len(list)):
        avg_grade = list[student][3]
        high_grade = max(avg_grade)
        high_grade = float(max(high_grade))
        if high_grade > 90 and high_grade < 100:
            grade_ltr = "A"
        elif high_grade > 80 and high_grade < 89:
            grade_ltr = "B"
        elif high_grade > 70 and high_grade < 79:
            grade_ltr = "C"
        elif high_grade > 60 and high_grade < 69:
            grade_ltr = "D"
        elif high_grade < 60:
            grade_ltr = "F"
    print("Highest Grade:", grade_ltr, "at", high_grade, "%")


def choice4():
    print("Lowest avg_grade")
    # re-use code from choice 3 but I am stuck


def choice5():
    print("Students in MSIT:")
    for student in range(len(list)):
        program = list[student][4]
        first_name = list[student][1]
        last_name = list[student][2]
        if program == "MSIT":
            print(first_name, last_name)


def choice6():
    print("Students in MSCM:")
    for student in range(len(list)):
        program = list[student][4]
        first_name = list[student][1]
        last_name = list[student][2]
        if program == "MSCM":
            print(first_name, last_name)


def choice7():
    print("Students sorted by ID:")
    for student in range(len(list)):
        student_id = list[student][0]
        student_id_split = student_id.split("\n")
        # student_id_split = int(student_id_split)
        # student_id.sort()
        sorted_student_ID = sorted(student_id_split)
        print(sorted_student_ID)


# program = list[student][4]
# first_name = list[student][1]
# last_name = list[student][2]
# if program == "MSCM":
# print(first_name, last_name)


def choice8():
    print("Show invalid records:")
    for student in range(len(list)):
        student_id = list[student][0]
        grade = list[student][3]
        grade = float(grade)
        program = list[student][4]
        first_name = list[student][1]
        last_name = list[student][2]
        if program == "":
            print("invalid record")  # need to indicate which record is invalid...
        elif first_name == "":
            print("invalid record")
        elif last_name == "":
            print("invaid record")
        elif student_id == "":
            print("invaid record")
        elif grade == "":
            print("invaid record")
        elif grade > 100 or grade < 0:
            print("invaid record")
        # elif program != "MIST" or "MSCM"
        # print("invaid record")
        # There should be 4 total invaild records 1 misnamed program, 1 grade over 100, 1 missing first name, and 1 missing last name


def choice9():
    print("Create invalid record file")


quit_program = False

while not quit_program:
    choice = print_menu()
    if choice == 10:
        quit_program = True
        print("Goodbye!")
        exit()
    else:
        if choice == 1:
            choice1()
        elif choice == 2:
            choice2()
        elif choice == 3:
            choice3()
        elif choice == 4:
            choice4()
        elif choice == 5:
            choice5()
        elif choice == 6:
            choice6()
        elif choice == 7:
            choice7()
        elif choice == 8:
            choice8()
        elif choice == 9:
            choice9()
        else:
            print("Invalid choice")
