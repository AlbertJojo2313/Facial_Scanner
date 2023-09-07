Key Features:

    Training: The project allows you to train the facial recognition model on a dataset of known faces. You can specify whether to use the "hog" or "cnn" model for training, where "hog" is CPU-based, and "cnn" is GPU-based for better performance.

    Validation: After training, you can validate the accuracy of the trained model using a separate dataset. The validation process displays recognized faces in the validation images and helps assess the model's performance.

    Testing: You can also use the trained model to recognize faces in unknown images. Simply provide the path to an image with unknown faces, and the system will identify and label the recognized faces in the image.

    Customizable Output: Recognized faces are highlighted with bounding boxes in blue, and their names are displayed in white text on a blue background. This makes it easy to visualize and identify the recognized faces.

Usage:

    To train the model, use the --train flag and specify the model type with the -m flag ("hog" or "cnn"). The trained encodings will be saved in a file.

    To validate the model, use the --validate flag and specify the model type with the -m flag. This will display recognized faces in validation images.

    To test the model with an unknown image, use the --test flag and provide the path to the image with unknown faces using the -f flag.

Dependencies:

    face_recognition: Used for face detection and recognition.
    Pillow: Used for image processing and drawing bounding boxes.
    pickle: Used for serializing and deserializing data.
    argparse: Used for command-line argument parsing.
