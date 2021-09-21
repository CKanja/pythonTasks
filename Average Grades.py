no_of_students = int(input("Enter number of students in class: "))
sum=0
for i in range(no_of_students):
    grade = input("Enter student grade: ")

    if str(grade).isdigit():
        sum+=int(grade)
    else:
        print("Input numbers only")
        continue

average = sum/no_of_students

print("The class average is: ", average)

