import os
import speech_recognition as sr
from PIL import Image
import matplotlib.pyplot as plt
# Path to the folder containing sign images
SIGN_IMAGE_PATH = r"D:\SRM\FOURTH YEAR\SEMESTER 8\Major Project\Source Codes\Sign_Images"
# Function to display hand gesture images for the given text
def text_to_sign_language(input_text):
    # Split input text into words
    words = input_text.lower().split()    
    # List to hold all images (letters + spaces)
    all_images = []
    for word in words:
        for letter in word:
            # Construct file path for the letter
            image_path = os.path.join(SIGN_IMAGE_PATH, f"{letter}.png")
            if os.path.exists(image_path):
                # Append the image to the list
                img = Image.open(image_path)
                all_images.append(img)
            else:
                # Placeholder for unknown letters
                all_images.append(Image.new("RGB", (100, 100), color="gray"))  # Gray placeholder
        # Add a blank image to represent space between words
        space_img = Image.new("RGB", (50, 100), color="white")
        all_images.append(space_img)    
    # Remove the last added space (not needed after the final word)
    if all_images and all_images[-1] == space_img:
        all_images.pop()
    # Create a figure to display the images
    fig, axes = plt.subplots(1, len(all_images), figsize=(2 * len(all_images), 5))    
    # Handle single-character input gracefully
    if len(all_images) == 1:
        axes = [axes]    
    for i, img in enumerate(all_images):
        axes[i].imshow(img)
        axes[i].axis("off")  # Hide axes

    plt.tight_layout()
    plt.show()
# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak something...")
        try:
            # Capture audio and recognize speech
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError:
            print("Could not request results; check your internet connection.")
    return ""
# Main function
if __name__ == "__main__":
    # Convert speech to text
    spoken_text = speech_to_text()
    if spoken_text:
        # Convert text to sign language
        text_to_sign_language(spoken_text)
