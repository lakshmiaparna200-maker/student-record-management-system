def add_student():
    file = open("students.txt", "a")
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")
    file.write(roll + "," + name + "," + branch + "," + marks + "\n")
    file.close()
    print("Student Record Added Successfully")
def view_students():
    try:
        file = open("students.txt", "r")
        data = file.readlines()
        if len(data)==0:
            print("students are not added..")
        else:
           print("\nStudent Records:\n")
           for line in data:
            student = line.strip().split(",")
            print("Roll No:", student[0])
            print("Name:", student[1])
            print("Branch:", student[2])
            print("Marks:", student[3])
            print("----------------------")
        file.close()
    except FileNotFoundError:
        print("No Records Found")
def search_student():
    roll_search = input("Enter Roll Number to Search: ")
    found = False
    try:
        file = open("students.txt", "r")
        for line in file:
            student = line.strip().split(",")
            if student[0] == roll_search:
                print("\nStudent Found")
                print("Name:", student[1])
                print("Branch:", student[2])
                print("Marks:", student[3])
                found = True
        file.close()
        if found == False:
            print("Student Not Found")
    except FileNotFoundError:
        print("No Records Found")
while True:
    print("\n--- Student Record Management System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")
    choice = input("Enter Choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        print("Thank You")
        break
    else:
        print("Invalid Choice")