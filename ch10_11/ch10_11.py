# Exercises 10.1, 10.8, 10.13, (11.1)
# Chapters 10 and 11 Exercises
# Carlos Rodriguez Escamilla
# 11/05/2022

# 10.1 Assign Grades

def gradeScore(score, bestScore):
    grade = None
    if score >= bestScore - 10:
        grade = "A"
    elif score >= bestScore - 20:
        grade = "B"
    elif score >= bestScore - 30:
        grade = "C"
    elif score >= bestScore - 40:
        grade = "D"
    else:
        grade = "F"
    
    return grade
    
def main():
    # scores = input("Enter scores:")
    # studentScores = [eval(x) for x in scores.split()]
    studentScores = [40, 55, 70, 58]
    bestScore = max(studentScores)
    for i in range(len(studentScores)):
        grade = gradeScore(studentScores[i], bestScore)
        print(f"Student {i} score is {studentScores[i]} and grade is {grade}")

main()
