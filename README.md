# SVD Image Approximation App

This Streamlit web application allows users to approximate images using Singular Value Decomposition (SVD). The app provides two options for image sources: URL and local file upload. Users can choose the number of singular values (k) for the approximation.

## Getting Started

### Prerequisites

Make sure you have the required Python libraries installed. You can install them using the following command:

```bash
pip install streamlit numpy matplotlib Pillow
```

### Running the App

Clone the repository and navigate to the project directory. Run the app using the following command:

```bash
streamlit run app.py
```

This will launch the app in your default web browser.

## Usage

1. Choose the image source:
   - **URL:** Enter the image URL in the provided text input.
   - **File on Device:** Upload an image file (supported formats: jpg, jpeg, png).

2. Select the number of singular values (k) using the slider.

3. View the original image and its approximation side by side.

4. Experiment with different images and values of k to observe the impact on image quality and file size.

## Features

- **SVD Image Approximation:** The app uses Singular Value Decomposition to approximate the input image based on the selected number of singular values (k).
- **Dynamic Image Display:** The app dynamically displays the original and approximated images side by side.
- **Image Sources:** Users can choose images from URLs or upload local image files.
- **Interactive Slider:** Adjust the number of singular values (k) with the interactive slider.

## Example

Here's a brief example of how to use the app:

1. Choose "URL" as the image source.
2. Enter the URL of the image you want to approximate.
3. Adjust the slider to set the number of singular values (k).
4. View the original and approximated images.

## Notes

- The app automatically scales down large images for better visualization.
- Ensure a stable internet connection when using the "URL" option.

Feel free to explore and experiment with different images to observe the effects of SVD approximation!