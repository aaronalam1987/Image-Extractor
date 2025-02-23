from art import text2art # ASCII art library.
import os 
import imageExtraction # Image extraction module.

# OpenCV supported image extensions.
supported_extensions = (".bpm", ".dib", ".gif", ".jpeg", ".jpg", ".jp2", ".png", ".webp", ".avif", ".pbm", ".pgm", ".pxm", ".pnm", ".pfm", ".sr", ".ras", ".tiff", ".tif", ".exr", ".hdr", ".pic")

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    os.system('cls||clear')
    welcomeText = text2art("Image Extraction Tool")
    print(welcomeText)
    user_input = input("Scan Directories (y/n)?: ").lower()
    if(user_input == "y"):
        scanDirs()
    else:
        print("Goodbye!")
        exit()

def scanDirs():
    print("\tSelect image source folder:")
    # List all directories in the current directory.
    availableDirs = [f for f in os.listdir('.\\') if os.path.isdir(os.path.join('.\\', f))]

    # No directories found, return to home screen.
    if(len(availableDirs) == 0):
        input("No directories found in the current directory.\nPress any key to return home.")
        intro() # return to home here.
    else:
        # Print available directories.
        for i in range(len(availableDirs)):
            print(f"\t {i+1}. {availableDirs[i]}")
        selectDir(availableDirs, len(availableDirs))

def selectDir(availableDirs, totalDirs):
    # Prompt user to select source directory.
    selectedDir = int(input("\tSelect directory: "))
    if(selectedDir > totalDirs or selectedDir < 1):
        input("Invalid selection.\nPress any key to return home.")
        intro() # return to home here.
    else:
        clearScreen()
        # Print selected directory.
        print(f"\tYou selected directory: {availableDirs[selectedDir-1]}\n")
        # List all image files in the selected directory.
        files_file = [x for x in os.listdir(f'.\\{availableDirs[selectedDir-1]}') if x.endswith(supported_extensions)]

        # No image files found, return to home screen.
        if(len(files_file) == 0):
            input("No image files found in the selected directory.\nPress any key to return home.")
            intro() # return to home here.        
        else:
            # Print all image files in the selected directory.
            for i in range(len(files_file)):
                print(f"\t {i+1} {files_file[i]}")
            
            selectedFile = int(input("\t\nSelect image file (enter * to batch process all available images): "))
            if(selectedFile > len(files_file) or selectedFile < 1):
                input("Invalid selection.\nPress any key to return home.")
                intro() # return to home here.
            else:
                print(f"\nYou selected {files_file[int(selectedFile)-1]}\n")
                facial_recognition(f'.\\{availableDirs[selectedDir-1]}\\{files_file[int(selectedFile)-1]}')
                #imageExtraction.process_image(f'.\\{availableDirs[selectedDir-1]}\\{files_file[int(selectedFile)-1]}')

def facial_recognition(file):
    user_input = input("Do you wish to seperate images with faces? (y/n): ").lower()
    if(user_input == "y"):
        print("Facial recognition enabled.")
        imageExtraction.process_image(file, True)
        return True
    else:
        print("Facial recognition disabled.")
        imageExtraction.process_image(file, False)
        return False

intro()