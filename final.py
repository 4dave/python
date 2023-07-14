import csv

f = open("STUDENTDATA.TXT")  # open file for reading

contents = f.read()  # read file
f.close()  # close the file

list = contents.split("\n")  # split the contents of the file into a list
print(list)  # print the list
# use len and index to parse out txt file
for i in range(len(list)):
    list[i] = list[i].split(",")
print(list)  # print the list


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
    print("Highest avg_grade")


def choice4():
    print("Lowest avg_grade")


def choice5():
    print("Students in MSIT")
    # for student in range(len(list)):
    #     student_id = list[index][0]
    #     avg_grade = list[student][3]
    #     program = list[student][4]
    #     print("Students in MSIT")


def choice6():
    print("Students in MSCM")


def choice7():
    print("Students sorted by ID")


def choice8():
    print("Show invalid records")


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
