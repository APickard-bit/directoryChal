# Python program to demonstrate
# main() function

directoriesFromRoot = {}

# Defining main function
def main():
    create("fruit")
    create("vegetables")
    create("fruit/apples")
    create("vegetables/squash/acorns")
    print(str(directoriesFromRoot))

# Create a Directory if it doesn't exist already
def create(targetPath):
    dirNames = targetPath.split("/")
    currentLoc = directoriesFromRoot
    index = 1

    # Check the preceeding path trail directories to make sure all the parent directories exist
    # currentLoc will act as the 'pointer' here

    trail = "."
    for dirName in dirNames[0: len(dirNames) - 1: 1]:
        trail  = trail + "/" + dirName        
        # If one of the parent dirs doesn't exist then print error and cancel
        currentLoc = currentLoc.get(dirName, None)
        if currentLoc is None:
            print("Cannot create " + targetPath + " - " + trail + " doesn't exist")
            return

        index = index + 1

    if currentLoc.get(targetPath, None) is None:
        currentLoc[dirNames[len(dirNames) - 1]] = {}

# def list():

# def move(original, targetPath):

# def delete(targetPath):

# Using the special variable 
# __name__
if __name__=="__main__":
    main()