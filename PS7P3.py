#input phase
counter = 0
print("Do you want to do this program? (Yes or No)")
answer = input()

#process and output phase
while answer == "Yes":
    counter = counter + 1
    print("Please enter your last name.")
    name = input()
    print("Enter exam score 1.")
    exam1 = float(input())
    print("Enter exam score 2.")
    exam2 = float(input())
    average = (exam1 + exam2) / 2
    print("Student " + name + ", your exam score average is: " + str(average))
    print("Do you want to do this program? (Yes or No)")
    answer = input()
print("Total number of students: " + str(counter))