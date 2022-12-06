#Exercise 14.3
#Chapter 14 Exercises
#Carlos Rodriguez Escamilla
#12/05/2022

# 14.8

def main():
    userFile = input("Enter a filename: ")
    infile = open(userFile, "r")
    s = infile.read()
    wordsArr = [word for word in s.split()]
    nonDuplicateWords = set()

    infile.close()
main()