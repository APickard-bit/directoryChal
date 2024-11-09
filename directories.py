# Python program to demonstrate
# main() function

directoriesFromRoot = {}

# Defining main function
def main():
    create("fruit", {})
    create("vegetables", {})
    create("fruit/apples", {})
    create("vegetables/squash/acorns", {})
    create("vegetables/squash", {})
    create("vegetables/squash/acorns", {})
    delete("vegetables/squash/acorns")
    list()

# Create a Directory if it doesn't exist already
def create(targetPath, contents):
    dirNames = targetPath.split("/")
    currentLoc, trail = checkIfTrailIsReal(dirNames)
    
    if currentLoc is None:
        print("Cannot create " + targetPath + " - " + trail + " doesn't exist")
        return

    targetDirName = dirNames[len(dirNames) - 1]
    if currentLoc.get(targetDirName, None) is None:
        currentLoc[targetDirName] = contents


# Check the preceeding path trail directories to make sure all the parent directories exist
# currentLoc will act as the 'pointer' here. Returns the currentLoc dictionary and a string representing it's current trail
def checkIfTrailIsReal(dirNames): 
    currentLoc = directoriesFromRoot
    index = 1

    trail = "."
    for dirName in dirNames[0: len(dirNames) - 1: 1]:
        trail  = trail + "/" + dirName        
        # If one of the parent dirs doesn't exist then print error and cancel
        currentLoc = currentLoc.get(dirName, None)
        if currentLoc is None:
            return currentLoc, trail

        index = index + 1

    return currentLoc, trail

# List all directories and subdirectories within them. Kicks off listRecur() from the "root" position
def list():
    output = listRecur(directoriesFromRoot, "", 0)
    print(output)

# Recursively print all directories and subdirectories within them
def listRecur(currentDir, output, prefix):
    for dirName in currentDir:
        
        for x in range(prefix):
            output = output + " "

        output = output + str(dirName) + "\n" 
        output = listRecur(currentDir.get(dirName), output, prefix + 2)
    
    return output

# def move(original, targetPath):

def delete(targetPath):
    dirNames = targetPath.split("/")
    currentLoc, trail = checkIfTrailIsReal(dirNames)

    if currentLoc is None:
        print("Cannot delete " + targetPath + " - " + trail + " doesn't exist")
        return

    targetDirName = dirNames[len(dirNames) - 1]
    if currentLoc.get(targetDirName, None) is not None:
        del currentLoc[targetDirName]


# Using the special variable 
# __name__
if __name__=="__main__":
    main()