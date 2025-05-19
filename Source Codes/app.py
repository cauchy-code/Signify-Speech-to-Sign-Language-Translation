from flask import Flask, render_template, request, jsonify
import os
import speech_recognition as sr
# Initialize Flask app
app = Flask(__name__)
# Path to sign images
SIGN_IMAGE_PATH = "static/Sign_images/"
# Function to convert speech to text
def speech_to_text(audio_file=None):
    recognizer = sr.Recognizer()
    if audio_file:
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
    else:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Error: Could not understand the audio."
    except sr.RequestError:
        return "Error: Check your internet connection."
# Route for landing page
@app.route("/")
def landing():
    return render_template("landing.html")
# Route for about page
@app.route("/about")
def about():
    return render_template("about.html")
# Route for Speech-to-Sign Page
@app.route("/speak")
def index():
    return render_template("index.html")
# Route for processing speech-to-text
@app.route("/process_speech", methods=["POST"])
def process_speech():
    if "audio" in request.files:
        audio_file = request.files["audio"]
        audio_path = os.path.join("uploads", audio_file.filename)
        audio_file.save(audio_path)
        text = speech_to_text(audio_file=audio_path)
        os.remove(audio_path)  # Clean up uploaded file
    else:
        text = speech_to_text()
    
    return jsonify({"text": text})
# Route for converting text to sign images
@app.route("/text_to_sign", methods=["POST"])
def text_to_sign():
    data = request.json
    input_text = data.get("text", "").lower()
    sign_images = []
    
    for word in input_text.split():
        for letter in word:
            image_path = os.path.join(SIGN_IMAGE_PATH, f"{letter}.png")
            if os.path.exists(image_path):
                sign_images.append(f"/{image_path}")
            else:
                print(f"Missing image for letter: {letter}")
        sign_images.append("NEWLINE")

    if sign_images and sign_images[-1] == "NEWLINE":
        sign_images.pop()

    return jsonify({"images": sign_images})
if __name__ == "__main__":
    app.run(debug=True)
