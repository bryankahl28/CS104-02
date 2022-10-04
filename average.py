average = 0
total = 0
howManyEntered = 0
print("How many test scores would you like me to average?")
howMany = int(input(' '))
print("Enter test score:")
testScore = int(input(' '))
total = total + testScore
howManyEntered = howManyEntered + 1
while howManyEntered < howMany:
    print("Enter test score:")
    testScore = int(input(' '))
    howManyEntered = howManyEntered + 1
    total = total + testScore
average = total / howManyEntered
print("The average for the test scores you entered is:")
print(average)
