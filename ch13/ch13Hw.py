# Exercises 13.3, 13.5, 13.11
# Chapter 13
# Carlos Rodriguez Escamilla
# 11/21/2022

# 13.3 Process scores in a text file

def main():
    userFile = input("Enter a filename: ")
    infile = open(userFile, "r")
    s = infile.read()
    scoresArr = [eval(num) for num in s.split()]
    total = 0

    for num in scoresArr:
        total+=num
    
    average = round((total / len(scoresArr)), 2)
    
    infile.close()
    
    print(f"There are {len(scoresArr)} scores")
    print(f"The total is {total}")
    print(f"The average is {average}")

main()

