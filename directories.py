# Directories code challenge for Endpoint
# 11/9/2024

# Each directory will be a dictionary, so the structure at the end would ideally 
# be a dictionary of dictionaries (That can contain more sub-dictionaries)
directoriesFromRoot = {}

# Main function, process text input for commands.
# Use 'exit' to finish
def main():
    command = ""
    while command.lower() != "exit":
        command = input("Input command here: ")
        enterCommand(command)

# Enter and process a command
# - $commandStr = inputted command String
# NOTE: This can probably be simplified to something other than a conditional stack
# NOTE: HELP command would also be ideal to document/list each command and their parameters
def enterCommand(commandStr):
    command = commandStr.strip()
    print(command)
    keyWords = commandStr.split(" ")

    if keyWords[0].upper() == "CREATE":
        try:
            if keyWords[1] is not None:
                create(keyWords[1], {})
        except IndexError:
            print("CREATE [targetPath] requires 1 parameter")

    elif keyWords[0].upper() == "LIST":
        list()
    
    elif keyWords[0].upper() == "MOVE":
        try:
            if keyWords[1] is not None and keyWords[2] is not None:
                move(keyWords[1], keyWords[2])
        except IndexError:
            print("MOVE [original] [targetPath] requires 2 parameters")
    
    elif keyWords[0].upper() == "DELETE":
        try:
            if keyWords[1] is not None:
                delete(keyWords[1])    
        except IndexError:
            print("DELETE [targetPath] requires 1 parameter")
    
    else:
        print("Command not recognized")

# Create a Directory if it doesn't exist already
# - $targetPath = Path of where to create a new directory
# - $contents = Contents of new directory, if any (empty dictionary by default)
def create(targetPath, contents):
    dirNames = targetPath.split("/")
    parentDir, trail = checkIfTrailIsReal(dirNames)
    
    if parentDir is None:
        print("Cannot create {} - {} doesn't exist".format(targetPath, trail))
        return

    targetDirName = dirNames[len(dirNames) - 1]
    if parentDir.get(targetDirName, None) is None:
        parentDir[targetDirName] = contents
    else: 
        print("Cannot create {} - {} already exists".format(targetPath, targetPath))


# Check the preceeding path trail directories to make sure all the parent directories exist
# parentDir will act as the 'pointer' here (current location in the path traversal). 
# Returns the dictionary of the current location and a string representing it's current trail
# - $dirNames = List of directories to traverse and check if the path is real
def checkIfTrailIsReal(dirNames): 
    parentDir = directoriesFromRoot
    index = 1
    trail = ""

    # We shouldn't check if the last dir in the path exits, just the previous ones
    for dirName in dirNames[0: len(dirNames) - 1: 1]:
        trail = trail + "/" + dirName        
        # If one of the parent dirs doesn't exist then print error and cancel
        parentDir = parentDir.get(dirName, None)
        if parentDir is None:
            return parentDir, trail[1:]

        index = index + 1

    return parentDir, trail[1:]

# List all directories and subdirectories within them. Kicks off listRecur() from the "root" position
def list():
    output = listRecur(directoriesFromRoot, "", 0)
    # Trim the last newline here
    print(output[:-1])

# Recursively print all directories and subdirectories within them
# - $currentDir = current location in the path traversal
# - $output = Current output String (Output is appended for every directory travelled)
# - $prefix = # of spaces to add before each directory name in the ouput
def listRecur(currentDir, output, prefix):
    for dirName in sorted(currentDir):
        
        # NOTE: Can probably do something other than a for loop here
        for x in range(prefix):
            output = output + " "

        # Recursively append the output for all subdirectories, return once finished
        output = output + str(dirName) + "\n" 
        output = listRecur(currentDir.get(dirName), output, prefix + 2)
    
    return output

# Move an existing directory to a new location, if the target path exists
# - $original = Original directory location
# - $targetPath = File path of where to move the orginal to 
def move(original, targetPath):
    targetDirNames = targetPath.split("/")
    
    # Check if the target path exists
    targetParentDir, trail = checkIfTrailIsReal(targetDirNames)
    if targetParentDir is None:
        print("Cannot move {} to {} - {} doesn't exist".format(original, targetPath, trail))
        return
    
    # Check if the original exists
    originalDirNames = original.split("/")
    originalParentDir, trail = checkIfTrailIsReal(originalDirNames)
    originalDirName = originalDirNames[len(originalDirNames) - 1]
    originalDir = originalParentDir.get(originalDirName, None)
    if originalDir is None:
        print("Cannot move {} to {} - {}/{} doesn't exist".format(original, targetPath, trail, originalDirName))
        return

    # Create copy of the original directory and then put it in the target location
    # Then delete the orignal
    create(targetPath + "/" + originalDirName, originalDir.copy())
    delete(original)


# Deletes a directory if it exists
# - $targetPath = Path of directory to delete
def delete(targetPath):
    dirNames = targetPath.split("/")
    parentDir, trail = checkIfTrailIsReal(dirNames)

    if parentDir is None:
        print("Cannot delete {} - {} doesn't exist".format(targetPath, trail))
        return

    targetDirName = dirNames[len(dirNames) - 1]
    if parentDir.get(targetDirName, None) is not None:
        del parentDir[targetDirName]
    else:
        print("Cannot delete {} - {} doesn't exist".format(targetPath, targetPath))


# Typical Python "main" function kickoff
if __name__=="__main__":
    main()