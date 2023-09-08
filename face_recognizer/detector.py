from pathlib import Path
from collections import Counter
from PIL import Image, ImageDraw
import face_recognition
import pickle
import argparse

DEFAULT_ENCODINGS_PATH = Path("output/encodings.pkl")
BOUNDING_BOX_COLOR = "blue"
TEXT_COLOR = "white"

parser = argparse.ArgumentParser(description="Recognize faces in an image")
parser.add_argument("--train", action="store_true", help="Train on input data")
parser.add_argument("--validate", action="store_true", help="Validate trained model")
parser.add_argument("--test", action="store_true", help="Test the model with an unknown image")
parser.add_argument("m", action="store", default="hog", choices=["hog", "cnn"], help="which model to use for training: hog (CPU), cnn (GPU)")
parser.add_argument("-f", action="store", help="Path to an image with an unknown face")
args = parser.parse_args()
Path("training").mkdir(parents=True, exist_ok=True)
Path("output").mkdir(parents=True, exist_ok=True)
Path("validation").mkdir(parents=True, exist_ok=True)

#Encode known faces from images in the 'training' directory.
def encode_known_faces(model="hog", encodings_location=DEFAULT_ENCODINGS_PATH):
    names = []
    encodings = []
    for filepath in Path("training").rglob("*/*"):
        #Extracts the name of the person from the parent directory name and loads the image.
        name = filepath.parent.name
        image = face_recognition.load_image_file(filepath)

        # Uses face_recognition.face_locations to detect the locations of faces in each image.
        # Returns a list of four-element tuples, one tuple for each detected face
        face_locations = face_recognition.face_locations(image, model=model)
        # Uses face_recognition.face_encodings to generate encodings for the detected faces in an image
        face_encodings = face_recognition.face_encodings(image, face_locations)

        #Appends the detected name and face encoding to the respective lists
        for encoding in face_encodings:
            names.append(name)
            encodings.append(encoding)
   
    #Creates a dictionary name_encodings with two keys: "names" (list of names) and "encodings" (list of face encodings).
    name_encodings = {"names": names, "encodings": encodings}
    with encodings_location.open(mode="wb") as f:
        pickle.dump(name_encodings, f)

def recognize_faces(image_location, model="hog", encodings_location=DEFAULT_ENCODINGS_PATH):
    with encodings_location.open(mode="rb") as f:
        loaded_encodings = pickle.load(f)
    input_image = face_recognition.load_image_file(image_location)
    input_face_locations = face_recognition.face_locations(input_image, model=model)
    input_face_encodings = face_recognition.face_encodings(input_image, input_face_locations)

    pillow_image = Image.fromarray(input_image)  # Creates a pillow image object from your loaded input image
    draw = ImageDraw.Draw(pillow_image)  # creates an ImageDraw object, which draws a bounding box around detected faces

    # Iterates through input_face_locations and input_face_encodings in parallel using zip().
    for bounding_box, unknown_encoding in zip(input_face_locations, input_face_encodings):
        name = _recognize_face(unknown_encoding, loaded_encodings)
        if not name:
            name = "Unknown"
        _display_face(draw, bounding_box, name)
    del draw
    pillow_image.show()

def _recognize_face(unknown_encoding, loaded_encodings):
    boolean_matches = face_recognition.compare_faces(loaded_encodings["encodings"], unknown_encoding)
    votes = Counter(
        name
        for match, name in zip(boolean_matches, loaded_encodings["names"])
        if match
    )
    if votes:
        return votes.most_common(1)[0][0]

def _display_face(draw, bounding_box, name):
    top, right, bottom, left = bounding_box
    draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)
    text_left, text_top, text_right, text_bottom = draw.textbbox((left, bottom), name)
    draw.rectangle((text_left, text_top), (text_right, text_bottom),
                   fill="blue",
                   outline="blue"
                   )
    draw.text(
        (text_left, text_top),
        name,
        fill="white",
    )

def validate(model="hog"):
    for filepath in Path("validation").rglob("*"):
        if filepath.is_file():
            recognize_faces(image_location=str(filepath.absolute()), model=model)

if __name__ == "__main__":
    if args.train:
        encode_known_faces(model=args.m)
    if args.validate:
        validate(model=args.m)
    if args.test:
        recognize_faces(image_location=args.f, model=args.m)
