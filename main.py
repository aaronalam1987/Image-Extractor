from art import text2art # ASCII art library.
import os 
import imageExtraction # Image extraction module.

# OpenCV supported image extensions.
supported_extensions = (".bpm", ".dib", ".gif", ".jpeg", ".jpg", ".jp2", ".png", ".webp",
                        ".avif", ".pbm", ".pgm", ".pxm", ".pnm", ".pfm", ".sr", ".ras", 
                        ".tiff", ".tif", ".exr", ".hdr", ".pic")

def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clearScreen()
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
    availableDirs = [d for d in os.listdir() if os.path.isdir(d)]

    # No directories found, return to home screen.
    if not availableDirs:
        input("No directories found in the current directory.\nPress any key to return home.")
        intro() # return to home here.

    else:
        # Print available directories.
        for i, directory in enumerate(availableDirs, start=1):
            print(f"\t {i}. {directory}")

        selectDir(availableDirs)

def selectDir(availableDirs):
    # Prompt user to select source directory.
    try:
        selectedDir = int(input("\tSelect directory: "))
        totalDirs = len(availableDirs)

        # Ensure user input is within the range of available directories.
        if selectedDir > totalDirs or selectedDir < 1:
            input("Invalid selection.\nPress any key to return home.")
            intro() # return to home here.

        else:
            clearScreen()

            # Print selected directory.
            print(f"\tYou selected directory: {availableDirs[selectedDir-1]}\n")

            # List all image files in the selected directory.
            files_file = [x for x in os.listdir(f'.\\{availableDirs[selectedDir-1]}') if x.endswith(supported_extensions)]

            # No image files found, return to home screen.
            if not files_file:
                input("No image files found in the selected directory.\nPress any key to return home.")
                intro() # return to home here.

            else:
                # Print all image files in the selected directory.
                for i in range(len(files_file)):
                    print(f"\t {i+1} {files_file[i]}")
                
                selectedFile = int(input("\t\nSelect image file (enter * to batch process all available images): "))
                # Batch process not implemented yet.
                if(selectedFile > len(files_file) or selectedFile < 1):
                        input("Invalid selection.\nPress any key to return home.")
                        intro() # return to home here.

                else:
                    print(f"\nYou selected {files_file[int(selectedFile)-1]}\n")
                    facial_recognition(f'.\\{availableDirs[selectedDir-1]}\\{files_file[int(selectedFile)-1]}')

    except ValueError:
        # Input is not an int.
        input("Invalid selection.\nPress any key to return home.")
        intro() # return to home here.

def facial_recognition(file):
    user_input = input("Do you wish to seperate images with faces? (y/n): ").lower()
    enable_facial_recognition = user_input == "y"

    if(enable_facial_recognition):
        print("Facial recognition enabled.")
    else:
        print("Facial recognition disabled.")

    imageExtraction.process_image(file, enable_facial_recognition)

intro()