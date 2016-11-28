#-------------------------------------
# Student: Javier Vazquez
# Student No.: X108457
# Project: 2
# Date: Nov 26, 2016
#-------------------------------------

# Write a text analyzer.
# It should be in a form of a function that takes a file name as an argument.
# It should read and analyze a text file and then print:
#         - the top 5 most frequently used words in the file
#         - the number of times the top 5 words are used
#         - should be sorted by most frequently used count
#         - the longest word in the document
#         - the average size of each word

import os, sys, re

class textAnalizer():
    """\tTakes as an argument the name of a file and then finds:
    - the top 5 most frequently used words in the file
    - the number of times the top 5 words are used
    - sorted by most frequently used count
    - the longest word in the document
    - the average size of each word"""

    def __init__(self):
        self.__sortedWordList = []
        self.__listLines = []

    def readFile(self, fileName):
        path = os.getcwd()
        if os.path.exists(path) is True:
            if os.path.isfile(os.path.join(path, fileName)) is True:
                try:
                    sourceFile = open(os.path.join(path, fileName), "r")
                    self.__listLines = sourceFile.readlines()
                    sourceFile.close()
                    return True, "File exist!!"
                except FileNotFoundError:
                    sys.exit("File does not exist 1")
            else:
                return False, "File does not exist 2"
        else:
            return False

    def countWord(self):
        freqWords = {}
        wordRegex = re.compile(r"\b\w+\b")
        for line in self.__listLines:
            wordList = wordRegex.findall(line)
            for word in wordList:
                if word in freqWords:
                    freqWords[word] += 1
                else:
                    freqWords[word] = 1
        self.__sortedWordList = sorted(freqWords.items(), reverse = True, key=lambda x: x[1])


    def topN(self,n = 5):
        listHeader = ["Word", "Frequency"]
        print("\n{0:<10}{1:>5}".format(listHeader[0], listHeader[1]))
        for i in range(n):
            print("{0:<10}{1:>9}".format(self.__sortedWordList[i][0], self.__sortedWordList[i][1]))

    def longestWord(self):
        size = 0
        lWord = ""
        for word in self.__sortedWordList:
            if len(word[0]) > size:
                size = len(word[0])
                lWord = word[0]
        print("\nThe longest word is: "+lWord+"\nLength: "+str(size))

    def averageWord(self):
        size = 0
        for word in self.__sortedWordList:
            size += len(word[0])
        print("Average length of words: {s:.2f}".format(s = size/len(self.__sortedWordList)))

def main():
    print("Project 1")
    words = textAnalizer()
    print(words.__doc__)

    flag = False
    print("Current path: ", os.getcwd())
    print("Folders and files: ")
    for file in os.listdir():
        print(file)
    print("\n")
    while flag is False:
        file = input("File's name: ")
        flag , msg = words.readFile(file)
        print(msg)

    words.countWord()
    words.topN()
    words.longestWord()
    words.averageWord()


if __name__ == "__main__":
    main()

