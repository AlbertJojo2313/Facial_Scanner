from pathlib import Path

def option():
    print("Looks up picture")
    print("1. Puts images for training")
    print("2. Copies the trained images to validate")
    print("3. Test the model")

    choice = int(input("Enter choice based on options: "))

    while (choice <= 3 && choice >= 1):
        if choice == 1:
            # Call a function to look up pictures and download them, then place them in the training folder
            download_and_place_in_training()
        elif choice == 2:
            # Call a function to copy the training images to the validation folder
            copy_training_to_validation()
        elif choice == 3:
            # Call a function to copy the training images to the test folder
            copy_training_to_test()
        else:
            print("Invalid choice. Please choose a valid option.")
        

def download_and_place_in_training():
    # Implement the logic to download and place pictures in the training folder
    # Also asks on how many pictures to download.
    # Should be linked to google images.
    # Check if folder with that name exists in the directory.
    # -- If yes then just place the pictures in the subdirectory.
    #  --- Else create a folder with the name of the subject then places the pictures in the directory.
    # Saves all downloaded pictures as jpeg.
    pass

def copy_training_to_validation():
    # Implement the logic to copy the training images to the validation folder
    # Copies all sub-directories that are present in training folder to the validation folder.
    pass

def copy_training_to_test():
    # Implement the logic to copy the training images to the test folder
    # Up to consideration.
    pass

if __name__ == "__main__":
    main()

