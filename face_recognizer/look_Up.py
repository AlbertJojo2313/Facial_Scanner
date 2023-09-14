from pathlib import Path
import os
import shutil
from google_images_download import google_images_download

def option():
    print("Looks up picture")
    print("1. Puts images for training")
    print("2. Copies the trained images to validate")
    print("3. Test the model")

    choice = int(input("Enter choice based on options: "))

    while (choice <= 3 and choice >= 1):
        if choice == 1:
            # Call a function to look up pictures and download them, then place them in the training folder
            name = input("Enter the name of subject")
            images = int(input("Enter the number of images to download"))
            download_and_place_in_training(name, images)
            break
        elif choice == 2:
            # Call a function to copy the training images to the validation folder
            source_directory = "/Face_Scanner/face_recognizer/training"  # Replace with the path to your source directory
            destination_directory = "/Face_Scanner/face_recognizer/validation"    # Replace with the path to your "validation" folder
            copy_training_to_validation(source_directory, destination_directory)
            break
            
        elif choice == 3:
            # Call a function to copy the training images to the test folder
            copy_training_to_test()
            break
        
        else:
            print("Invalid choice. Please choose a valid option.")
            break

def download_and_place_in_training(name, num_images):
    # Create a directory for the subject if it doesn't exist
    if not os.path.exists(name):
        os.makedirs(name)

    # Set up the download parameters
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": name,
        "limit": num_images,
        "print_urls": True,
        "no_directory": True,
        "output_directory": "/Face_Scanner/face_recognizer/training/",
        "image_directory": name,
        "format": "jpg"
    }
    # Download the images
    paths = response.download(arguments)
    print(f"Downloaded {len(paths[0][name])} images to /training/{name}")


def copy_training_to_validation(source_diretory, destination_directory):
    # Implement the logic to copy the training images to the validation folder
    # Copies all sub-directories that are present in training folder to the validation folder.
    # If the sub-directory is not present in the validation folder then create it.
    # If the sub-directory is present in the validation folder then just copy the images to the sub-directory.
    # If the sub-directory is present in the validation folder and has images then copy the images to the sub-directory.
    # If the sub-directory is present in the validation folder and has no images then copy the images to the sub-directory.
    # If the sub-directory is not present in the validation folder and has no images then create the sub-directory and copy the images to the sub-directory.
    # If the sub-directory is not present in the validation folder and has images then create the sub-directory and copy the images to the sub-directory.
    # If the sub-directory is not present in the validation folder and has images then create the sub-directory and copy the images to the sub-directory.
    try:
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
        shutil.copytree(source_diretory, destination_directory)
    except Exception as e:
        print(f"Error occurred: {str(e)}")
    else:
        print(f"Successfully copied {source_diretory} to {destination_directory}")

#def copy_training_to_test():
    
    # Implement the logic to copy the training images to the test folder
    # Up to consideration.
"""      try:
        # Check if the source directory exists
        if not os.path.exists(training_dir):
            print(f"Training directory '{training_dir}' does not exist.")
            return

        # Check if the destination directory exists; create it if not
        if not os.path.exists(test_dir):
            os.makedirs(test_dir)

        # List all files in the training directory
        training_files = os.listdir(training_dir)

        # Copy each file from training to test
        for file_name in training_files:
            src_path = os.path.join(training_dir, file_name)
            dest_path = os.path.join(test_dir, file_name)
            shutil.copy(src_path, dest_path)

        print(f"Copied {len(training_files)} files from '{training_dir}' to '{test_dir}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}") """
 

if __name__ == "__main__":
    option()
    
