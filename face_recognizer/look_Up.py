import os
import shutil
from google_images_download import google_images_download


# Function to download images and place them in the training folder
def download_and_place_in_training(name, num_images):
    # Create a directory for the subject if it doesn't exist
    if not os.path.exists("training"):
        os.makedirs("training")

    # Set up the download parameters
    response = google_images_download.googleimagesdownload()
    arguments = {
        "keywords": name,
        "limit": num_images,
        "print_urls": True,
        "output_directory": "training",
        "image_directory": name,
        "format": "jpg"
    }

    # Download the images
    paths = response.download(arguments)
    print(f"Downloaded {len(paths[0][name])} images to /training/{name}")


# Function to copy the training images to the validation folder
def copy_training_to_validation(source_directory, destination_directory):
    try:
        # Check if the destination directory exists; create it if not
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # List all subdirectories in the source directory (each subdirectory represents a subject)
        subjects = os.listdir(source_directory)

        # Copy each subject's images to the corresponding subdirectory in the destination (validation) folder
        for subject in subjects:
            src_subject_dir = os.path.join(source_directory, subject)
            dest_subject_dir = os.path.join(destination_directory, subject)

            # Check if the subject's directory exists in the destination; create it if not
            if not os.path.exists(dest_subject_dir):
                os.makedirs(dest_subject_dir)

            # Copy images from source to destination
            for image_file in os.listdir(src_subject_dir):
                src_image_path = os.path.join(src_subject_dir, image_file)
                dest_image_path = os.path.join(dest_subject_dir, image_file)
                shutil.copy(src_image_path, dest_image_path)

        print(f"Successfully copied training images to validation folder: {destination_directory}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


def option():
    print("Looks up pictures")
    print("1. Puts images for training")
    print("2. Copies the trained images to validate")
    print("3. Test the model")

    choice = int(input("Enter choice based on options: "))

    if choice == 1:
        name = input("Enter the name of the subject: ")
        images = int(input("Enter the number of images to download: "))
        download_and_place_in_training(name, images)
    elif choice == 2:
        source_directory = "training"  # Replace with the path to your source directory
        destination_directory = "validation"  # Replace with the path to your "validation" folder
        copy_training_to_validation(source_directory, destination_directory)
    elif choice == 3:
        # Call a function to test the model (not implemented in your code)
        pass
    else:
        print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    option()
