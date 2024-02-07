# Creating gradebook for students

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
            print(average)
    return -1


print("----- Gradebook for Pdeu Students -----")
printGradeBook(gradebook)

print("Enter the student name: ")
name = input()
avg = calculateAverage(name)

if avg != -1:
    print(f"The average grade of {name} is {avg}")
else:
    print(f"Record not found!")
