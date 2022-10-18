# Write a program Scores.py that performs the following,
#  Ask user to enter the number of students, then loop for user to enter the student’s 
# scores.
#  Calculate the total, average and count how many students passed the test (score of 70 
# or more)

numOfStudents = eval(input("Enter the total number of students: "))
totalScore = 0
higestScore = 0
studentsPassed = 0

for i in range(numOfStudents):
    studentScore = eval(input("Enter student score:"))
    totalScore+=studentScore

    if studentScore > higestScore:
        higestScore = studentScore

    if studentScore >= 70:
        studentsPassed+=1
        
averageScore = (totalScore / numOfStudents)

print(f"Total score: {totalScore} Average score: {format(averageScore, '.2f')} Highest Score: {higestScore}")
print(f"Number of students passed: {studentsPassed} out of {numOfStudents}")


