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


# Write a program BMI.py that performs the following,
#  Define a function called getBMI that takes weight and height as parameters and 
# calculates and returns the BMI. (bmi = weight*703/(height*height))
#  Ask user to input a person’s height, use function getBMI to print the BMI chart with 
# weight from 100 lbs to 200 lbs in increments of 10 lbs.
#  Challenge: add a third column Interpretation to the output.
# BMI Interpretation
# Below 18.5 Underweight
# 18.5–24.9 Normal
# 25.0–29.9 Overweight
# Above 30.0 Obese

def getBMI(weight, height):
    """
        takes in weight and height as parameters and converts 
        them into the users BMI
    """
    bmi = round(weight * 703 / (height * height), 1)
    return bmi

def getBmiInterpretation(bmi):
    """
        Determining if the person is overweight, obese, normal,
        or underweight
    """
    bmiInterpretation = ""
    if bmi < 18.5:
        bmiInterpretation = "Underweight"
    elif bmi > 18.5 and bmi < 24.9:
        bmiInterpretation = "Normal"
    elif bmi > 25.0 and bmi < 29.9:
        bmiInterpretation = "Overweight"
    else:
          bmiInterpretation = "Obese"
    
    return bmiInterpretation

# Get the height of the user
userHeight = eval(input("Enter person's height: "))

# Create BMI Chart
print("Your BMI Chart:")
print(f"Height: {userHeight} inches")

print(f"{'Weight':<10}{' BMI':<10}{'Interpretation':<10}")
# looping through weight
for weight in range(100, 201, 10):
    bmi = getBMI(weight, userHeight)
    bmiInterpretation = getBmiInterpretation(bmi)
    print(f"{weight:<10} {bmi:<10} {bmiInterpretation:<10}")
    


