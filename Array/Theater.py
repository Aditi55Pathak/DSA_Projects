# Creating gradebook for students
from colorama import Fore

gradebook = [
    ["Aditi", 91, 98, 90],
    ["Avani", 12, 45, 22],
    ["Puja", 56, 66, 89],
    ["Ishita", 99, 90, 78],
    ["Heli", 56, 89, 21],
    ["Pranjal", 89, 90, 12],
]


def printGradeBook(gradebook):
    for i in gradebook:
        print(i)


def calculateAverage(studentName):
    for i in gradebook:
        if i[0] == studentName:
            grades = i[1:]
            average = sum(grades) / len(grades)
            print(Fore.GREEN + f"The average grade of {name} is {average}")
            return
    print(Fore.RED + f"Record not found!")


print("----- Gradebook for Pdeu Students -----")
printGradeBook(gradebook)

print("Enter the student name: ")
name = input()
calculateAverage(name)
