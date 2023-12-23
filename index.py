import dlib
import cv2
import numpy as np
import os


# Initialize dlib's face detector and facial recognition models
detector = dlib.get_frontal_face_detector()
shape_predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
face_recognition_model = dlib.face_recognition_model_v1("dlib_face_recognition_resnet_model_v1.dat")

# Function to extract facial embeddings from an image
def get_face_embeddings(image):
    faces = detector(image, 1)
    face_descriptors = []
    for face in faces:
        shape = shape_predictor(image, face)
        face_descriptor = face_recognition_model.compute_face_descriptor(image, shape)
        face_descriptors.append(face_descriptor)
    return face_descriptors

# Function to compare a given face with faces in an image
def check_if_face_exists(given_face_embedding, face_embeddings_in_image, threshold=0.6):
    # Compare the given face embedding with all face embeddings in the image
    for face_embedding in face_embeddings_in_image:
        # Calculate Euclidean distance between the embeddings
        distance = np.linalg.norm(np.array(given_face_embedding) - np.array(face_embedding))
        
        # Set a threshold for similarity
        if distance < threshold:
            return True  # Face exists in the image
    return False  # Face doesn't exist in the image

# Load the given face image (the face you want to check)
#Chanthe image path for single face image accordingly
#####################################################################################################
given_face_image = cv2.imread("IMG_0030.JPG")

# Directory containing the given multiple face or group images
given_multi_face_dir = "images/"
# Get face embeddings from the given face image
given_face_embeddings = get_face_embeddings(given_face_image)

# Assuming the given face image has only one face, take the first face embedding
given_face_embedding = given_face_embeddings[0]


# Directory containing the image files
directory_path = "images"  # Replace with your directory path

# Get all files in the directory
files_in_directory = os.listdir(directory_path)

# Filter JPEG files (files ending with '.jpg' or '.JPG')
jpg_files = [file for file in files_in_directory if file.endswith(".JPG")]

# Initialize variables
# CREATED NEW DIR NAME
specific_face_directory = "specific_face_directory"
face = []
no_exist = []

# Loop through the list of JPEG files
for jpg_file in jpg_files:
    
    # Create a specific face directory if it doesn't exist
    if not os.path.exists(specific_face_directory):
        os.makedirs(specific_face_directory)

    # Load the image with multiple faces
    image_with_multiple_faces = cv2.imread(given_multi_face_dir + jpg_file)

    # Get face embeddings from the image with multiple faces
    face_embeddings_in_image = get_face_embeddings(image_with_multiple_faces)   

    # Check if the given face exists among faces in the image
    face_exists = check_if_face_exists(given_face_embedding, face_embeddings_in_image)
    if face_exists:
        face.append(jpg_file)
        cv2.imwrite(specific_face_directory + "/" + jpg_file, image_with_multiple_faces)
        print("Given face exists in the image with multiple faces.")
    else:
        no_exist.append(jpg_file)
        print("Given face does not exist in the image with multiple faces.")
print(face)
