def loadStudentData(fileName="grades.txt"):
    students = {}
    with open(fileName, "r") as file:
        for student in file:
            parts = student.strip().split()
            name = parts[0]  # key : Student name
            grades = list(map(int, parts[1:]))  # Value: A list of grades
            students[name] = grades
    return students


def viewGrades(students):
    print("\nStudent and their grades:")
    for name, grades in students.items():
        print(f"{name}: {', '.join(map(str, grades))}")


def studentAverage(students, sName):
    if sName in students:
        average = sum(students[sName]) / 3
        print(f"Average grade for {sName}: {average:.2f}")
    else:
        print(f"Student '{sName}' not found.")


def classStatistics(students):
    if not students:
        print("No data available.")
        return

    listOfGrades = []
    for grades in students.values():
        listOfGrades.append(sum(grades) / 3)

    overall = sum(listOfGrades) / len(listOfGrades)
    averages = {name: sum(grades) / len(grades) for name, grades in students.items()}
    highest = max(averages, key=averages.get)
    lowest = min(averages, key=averages.get)
    print(f"Class average: {overall:.2f}")
    print(
        f"Highest average: {highest} ({sum(students[highest]) / len(students[highest]):.2f})"
    )
    print(
        f"Lowest average: {lowest} ({sum(students[lowest]) / len(students[lowest]):.2f})"
    )


def saveData(students, file_name="grades.txt"):
    with open(file_name, "w") as file:
        for name, grades in students.items():
            file.write(f"{name} {' '.join(map(str, grades))}\n")


def main():
    students = loadStudentData()
    while True:
        print("\nWelcome to the Student Grades Management System")
        print("1. View all grades")
        print("2. Calculate average for a student ")
        print("3. View class statistics")
        print("4. Exit\n")

        choice = input("Enter your choice : ")
        if choice == "1":
            viewGrades(students)
        elif choice == "2":
            sName = input("Enter the student's name: ")
            studentAverage(students, sName)
        elif choice == "3":
            classStatistics(students)
        elif choice == "4":
            saveData(students)
            print(
                "Saving data to grades.txt...\nThank you for using the Student Grades Management System. Goodbye!"
            )
            break
        else:
            print("Invalid choice! Please try again.")


main()
