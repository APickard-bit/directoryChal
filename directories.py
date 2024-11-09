# Directories code challenge for Endpoint
# Andrew Pickard
# 11/9/2024

# Each directory will be a dictionary, so the structure at the end would ideally 
# be a dictionary of dictionaries (That can contain more sub-dictionaries)
directoriesFromRoot = {}

# Defining main function
def main():
    command = ""
    while command != "exit":
        command = input("Input command here: ")
        enterCommand(command)

    create("fruits", {})
    create("vegetables", {})
    create("grains", {})
    create("fruits/apples", {})
    create("fruits/apples/fuji", {})
    list()
    create("grains/squash", {})
    move("grains/squash", "vegetables")
    create("foods", {})
    move("grains", "foods")
    move("fruits", "foods")
    move("vegetables", "foods")
    list()
    delete("fruits/apples")
    delete("foods/fruits/apples")
    list()

def enterCommand(commandStr):
    command = commandStr.strip()
    print(command)
    keyWords = commandStr.split(" ")
    if keyWords[0] == "CREATE":
        if keyWords[1] is not None:
            create(keyWords[1], {})
    elif keyWords[0] == "LIST":
        list()
    elif keyWords[0] == "MOVE":
        if keyWords[1] is not None and keyWords[2] is not None:
            move(keyWords[1], keyWords[2])
    elif keyWords[0] == "DELETE":
        if keyWords[1] is not None:
            delete(keyWords[1])    
    else:
        print("Command not recognized")


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
    else: 
        print("Cannot create " + targetPath + " - " + targetPath + " already exists")


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
    for dirName in sorted(currentDir):
        
        for x in range(prefix):
            output = output + " "

        output = output + str(dirName) + "\n" 
        output = listRecur(currentDir.get(dirName), output, prefix + 2)
    
    return output

# Move an existing directory to a new location, if the target path exists
def move(original, targetPath):
    targetDirNames = targetPath.split("/")
    
    # Check if the target path exists
    targetLoc, trail = checkIfTrailIsReal(targetDirNames)
    if targetLoc is None:
        print("Cannot move " + original + " to " + targetPath + " - " + trail + " doesn't exist")
        return
    
    # Check if the original exists
    originalDirNames = original.split("/")
    originalLoc, trail = checkIfTrailIsReal(originalDirNames)
    originalDirName = originalDirNames[len(originalDirNames) - 1]
    originalDir = originalLoc.get(originalDirName, None)
    if originalDir is None:
        print("Cannot move " + original + " to " + targetPath + " - " + trail + "/" + originalDirName + " doesn't exist")
        return

    create(targetPath + "/" + originalDirName, originalDir.copy())
    delete(original)


# Deletes a directory if it exists
def delete(targetPath):
    dirNames = targetPath.split("/")
    currentLoc, trail = checkIfTrailIsReal(dirNames)

    if currentLoc is None:
        print("Cannot delete " + targetPath + " - " + trail + " doesn't exist")
        return

    targetDirName = dirNames[len(dirNames) - 1]
    if currentLoc.get(targetDirName, None) is not None:
        del currentLoc[targetDirName]
    else:
        print("Cannot delete " + targetPath + " - " + targetPath + " doesn't exist")


# Using the special variable 
# __name__
if __name__=="__main__":
    main()