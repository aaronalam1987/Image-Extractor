import cv2 as cv
import os

def process_image(image_path, facial_recognition=False):
    # Get original filename/file extension.
    filename = os.path.splitext(os.path.basename(image_path))[0]
    extension = os.path.splitext(os.path.basename(image_path))[1]

    # Load image
    image = cv.imread(image_path)

    # Convert to grayscale
    gray = convert_to_grayscale(image)

    # Apply threshold
    thresholded = apply_threshold(gray)

    # Find contours
    contours = set_contours(thresholded)

    # Prompt user
    user_prompt(image, contours, filename, extension, facial_recognition)

def convert_to_grayscale(image):
    return cv.cvtColor(image, cv.COLOR_BGR2GRAY)

def apply_threshold(image):
    _, thresholded = cv.threshold(image, 240, 255, cv.THRESH_BINARY_INV)
    return thresholded  

def set_contours(image):
    contours, _ = cv.findContours(image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    return contours

def prompt_user(num_of_images):
    user_input = input(f"Found {num_of_images} images. Do you want to extract them? (y/n): ").lower()
    return user_input

def face_recognition(image):
    convert_to_grayscale(image)
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image, 1.3, 5)
    if len(faces) > 0:
        return True
    else:
        return False

def do_extract(image, contours, filename, extension, facial_recognition=False):
    output_dir = "output"

    # Ensure output directory exists.
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # If user has opted to seperate images with faces, create faces folder in output directory.
    if(facial_recognition):
        if not os.path.exists(f'{output_dir}/faces'):
            os.makedirs(f'{output_dir}/faces')

    # Save extracted objects.
    for i, contour in enumerate(contours):
        x, y, w, h = cv.boundingRect(contour)
        indv_image = image[y:y+h, x:x+w]  # Crop from original color image.
        
        # Save image to output directory, if facial recognition is enabled, save to faces folder.
        if(facial_recognition):
            if(face_recognition(indv_image)):
                cv.imwrite(f"{output_dir}/faces/{filename}_{i}.{extension}", indv_image)
                print(f"Image extracted to {output_dir}/faces/{filename}{i}{extension}")
            else:
                cv.imwrite(f"{output_dir}/{filename}_{i}.{extension}", indv_image)
                print(f"Image extracted to {output_dir}/{filename}{i}{extension}")      
        
def user_prompt(image, contours, filename, extension, facial_recognition):
    num_of_images = len(contours)

    if(prompt_user(num_of_images) == "y"):
        do_extract(image, contours, filename, extension, facial_recognition)   

    else:
        print("Extraction aborted.")