This project is a Python-based facial recognition system that allows you to train a model on a dataset of known faces, validate the model's accuracy, and recognize faces in unknown images. It uses the face_recognition library and provides command-line options for training, validation, and testing the model. The recognized faces are highlighted with bounding boxes and labeled with their names in a graphical user interface.

Facial recognition is a popular and widely used technology with applications in security, surveillance, and various other fields. This project provides a Python-based implementation of a facial recognition system that can be used for training, validation, and recognition tasks.

Key Features:

    Training: The project allows you to train the facial recognition model on a dataset of known faces. You can specify whether to use the "hog" or "cnn" model for training, where "hog" is CPU-based, and "cnn" is GPU-based for better performance.

    Validation: After training, you can validate the accuracy of the trained model using a separate dataset. The validation process displays recognized faces in the validation images and helps assess the model's performance.

    Testing: You can also use the trained model to recognize faces in unknown images. Simply provide the path to an image with unknown faces, and the system will identify and label the recognized faces in the image.

    Customizable Output: Recognized faces are highlighted with bounding boxes in blue, and their names are displayed in white text on a blue background. This makes it easy to visualize and identify the recognized faces.
