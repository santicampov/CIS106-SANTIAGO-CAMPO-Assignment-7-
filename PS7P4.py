#INPUT PHASE
sumgp = 0
nemployee = 0
print("Do you want to do this program?")
answer = input()

#PROCESS AND OUTPUT PHASE
while answer == "Yes":
    print("Please enter your last name.")
    name = input()
    print("Enter how many hours you have worked.")
    hours = float(input())
    print("Please enter your pay rate.")
    rate = float(input())
    if hours > 40:
        extra = hours - 40
        gp = 40 * rate + extra * (rate * 1.5)
    else:
        gp = hours * rate
    print("Employee " + name + ", your gross pay is:   $" + str(gp))
    sumgp = sumgp + gp
    nemployee = nemployee + 1
    print("Do you want to do this program?")
    answer = input()
avggp = sumgp / nemployee
print("The sum of all the gross pays is:   $" + str(sumgp))
print("The number of employees is:  " + str(nemployee))
print("The average gross pay is:   $" + str(avggp))