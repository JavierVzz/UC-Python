#-------------------------------------
# Student: Javier Vazquez
# Student No.: X108457
# Project: 1
# Date: Nov 26, 2016
#-------------------------------------

# A file with a name like picture.jpg is said to have an extension
# of "jpg"; i.e. the extension of a file is the part of the file
# after the final period in its name. Write a program that takes
# as an argument the name of a directory (folder) and then finds
# the extension of each file. Then, for each extension found,
# it prints the number of files with that extension and the minimum,
# average, and maximum size for files with that extension in the
# selected directory.

import os, re, copy

class fileStats:
    """\tTakes as an argument the name of a directory (folder) and then finds
    the extension of each file. Then, for each extension found,
    it prints the number of files with that extension and the minimum,
    average, and maximum size for files with that extension in the
    selected directory.\n"""

    def __init__(self):
        self.__path = os.getcwd()
        self.__extDict = {}
        self.__avgDict = {}
        self.__minimumDict = {}
        self.__maximumDict = {}
        self.__listFiles = []

    def verifyPath(self, path):
        if os.name == "nt":
            path = path.replace("\\", "\\\\")
        if os.path.exists(path):
            self.__path = path
            return self.__path
        else:
            return False

    def getDirectory(self):
        return self.__path

    def countFiles(self):
        """\tcountFiles() method ist"""
        extRegex = re.compile(r"\.\w+$")
        self.__listFiles = os.listdir(self.__path)
        for i in self.__listFiles:
            ext = extRegex.search(i)
            if ext is not None:
                if i[ext.start()+1:] in self.__extDict.keys():
                    self.__extDict[i[ext.start()+1:]] += 1
                else:
                    self.__extDict[i[ext.start()+1:]] = 1
        return self.__extDict

    def averagePerExt(self):
        averageList = list(self.__extDict.keys())
        self.__avgDict = copy.deepcopy(self.__extDict)
        for ext in averageList:
            i = 0
            extRegex = re.compile(r".+\."+ext+r"$")
            for file in self.__listFiles:
                extension = extRegex.search(file)
                if extension is not None:
                    if i == 0:
                        self.__avgDict[ext] = os.path.getsize(os.path.join(self.__path, extension.group()))
                    else:
                        self.__avgDict[ext] += os.path.getsize(os.path.join(self.__path, extension.group()))
                    i += 1
            self.__avgDict[ext] /= i
        return self.__avgDict

    def minimumPerExt(self):
        minimumList = list(self.__extDict.keys())
        self.__minimumDict = copy.deepcopy(self.__extDict)
        for ext in minimumList:
            i = 0
            extRegex = re.compile(r".+\."+ext+r"$")
            for file in self.__listFiles:
                extension = extRegex.search(file)
                if extension is not None:
                    if i == 0:
                        self.__minimumDict[ext] = os.path.getsize(os.path.join(self.__path, extension.group()))
                    else:
                        if self.__minimumDict[ext] > os.path.getsize(os.path.join(self.__path, extension.group())):
                            self.__minimumDict[ext] = os.path.getsize(os.path.join(self.__path, extension.group()))
                    i += 1
        return self.__minimumDict

    def maximumPerExt(self):
        maximumList = list(self.__extDict.keys())
        self.__maximumDict = copy.deepcopy(self.__extDict)
        for ext in maximumList:
            i = 0
            extRegex = re.compile(r".+\."+ext+r"$")
            for file in self.__listFiles:
                extension = extRegex.search(file)
                if extension is not None:
                    if i == 0:
                        self.__maximumDict[ext] = os.path.getsize(os.path.join(self.__path, extension.group()))
                    else:
                        if self.__maximumDict[ext] < os.path.getsize(os.path.join(self.__path, extension.group())):
                            self.__maximumDict[ext] = os.path.getsize(os.path.join(self.__path, extension.group()))
                    i += 1
        return self.__maximumDict

    def stats(self):
        totalFiles = 0
        self.countFiles()
        self.minimumPerExt()
        self.averagePerExt()
        self.maximumPerExt()
        listHeader = ["Extension", "Files", "Minimum", "Average", "Maximum"]
        print("\n{0:<10}{1:>5}{2:>10}{3:>10}{4:>10}"
                .format(listHeader[0], listHeader[1],
                listHeader[2], listHeader[3], listHeader[4]))
        for ext in list(self.__extDict.keys()):
            totalFiles += self.__extDict[ext]
            print("{0:<10}{1:>5}{2:>10.2f}{3:>10.2f}{4:>10.2f}"
                .format(ext, str(self.__extDict[ext]),
                self.__minimumDict[ext]/1024,
                self.__avgDict[ext]/1024,
                self.__maximumDict[ext]/1024))
        print("\nTotal Files: ", totalFiles)
        print("Sizes in Kb")

def main():
    #Test branch!!!!
    print("Project 1")
    stats = fileStats()
    print(stats.__doc__)
    print("""Type and absolute path, if there is no path or wrong path the
    program will marked as false and will use the current path\n""")
    print("Current path: ", stats.getDirectory())
    path = input("Path: ")
    verifiedPath = stats.verifyPath(path)
    print("Verified path: ", verifiedPath)
    stats.stats()
    return None

if __name__ == "__main__":
    main()
