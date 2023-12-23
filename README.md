# Facial Recognition Photo Organizer

## Overview

Have you ever been inundated with a plethora of event photos and found yourself struggling to organize them by individuals? Introducing a Python tool that simplifies the sorting process using facial recognition!

This tool leverages the power of Dlib and OpenCV to effortlessly sort event photos based on individual faces. Simply provide a single cropped facial image, and let the magic happen! The tool swiftly identifies matching faces among the event photos, making photo organization a breeze.

## Features

- **Facial Recognition**: Utilizes Dlib's face detection and facial recognition models.
- **Effortless Sorting**: Quickly identifies and segregates images by individual faces.
- **Stress Tested**: Successfully handled a thousand JPG images for efficient processing.
- **User-Friendly**: Aims to be transformed into a user-friendly UI tool for easy accessibility.

## Usage

### Setup

1. **Clone the repository:**

   ```bash
   git clone [Your GitHub Repo URL]

2. **Set up a Virtual Environment (optional but recommended):**
    python -m venv env
    source env/bin/activate  # For Linux/Mac
    .\env\Scripts\activate   # For Windows

3. **Install dependencies:**
    pip install -r requirements.txt

**NOTE:** Ensure Python 3.7 or later is installed.

## Running the Tool

* Provide a single cropped facial image.
* Run the tool:
    python sort_photos.py
* Retrieve sorted photos in the specific_face_directory.

## Limitations

* **Single Face Images Only:** Currently optimized for single cropped facial images.
* **JPG Format:** Stress testing specifically performed on JPG format images.
* **Multiple Faces Not Supported:** Tool doesn’t handle multiple faces in the input image.

## Contribution

Contributions are welcome! If you'd like to enhance this tool or propose features, feel free to create a pull request or raise an issue.

## Future Improvements

* Explore handling multiple faces in input images.
* Optimize for various image formats.
* Develop a user-friendly UI for wider accessibility.

## License

This project is licensed under the [Your License] - see the LICENSE file for details.

## Acknowledgments

Special thanks to Dlib and OpenCV for their powerful libraries that make this tool possible.

## Contact

For inquiries, feedback, or collaborations, feel free to reach out at [jyotirmoymukhopadhyay2@gmail.com] or connect on [LinkedIn](https://www.linkedin.com/in/mukhopadhyay-jyoti/).

