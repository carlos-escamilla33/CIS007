#Exercise 14.8
#Chapter 14 Exercises
#Carlos Rodriguez Escamilla
#12/05/2022

# 14.8
import re

def main():
    userFile = input("Enter a filename: ")
    infile = open(userFile, "r")
    s = infile.read()
    newS = re.sub(r"[^\w\s]", "", s)
    wordsArr = [word.lower() for word in newS.split()]
    nonDuplicateWords = sorted(set(wordsArr))

    infile.close()

    for word in nonDuplicateWords:
        print(word)

main()