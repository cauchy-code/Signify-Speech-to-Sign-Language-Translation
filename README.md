# Signify 🔊🤟  
**Real-Time Speech to Sign Language Translator using Transformer-Based Models**

---

## 📌 Description

**Signify** is a Flask-based web application that enables real-time translation of spoken English into Indian Sign Language (ISL) gestures. Built using **transformer-based models** like **Wav2Vec 2.0** (for speech recognition) and **Vision Transformer (ViT)** (for sign rendering), Signify aims to bridge the communication gap for the hearing-impaired community.

---

## 🧠 Features

- 🎤 Speech-to-text conversion using **Wav2Vec 2.0** (with Whisper fallback)
- 🤖 Text-to-sign conversion using static sign gesture images
- 📷 Vision Transformer integration for future gesture recognition
- ⚡ Real-time, low-latency performance
- 🌐 Intuitive UI with modern design and contributor credits

---

## 📁 Project Structure

Signify/
├── app.py # Flask backend
├── static/
│ ├── Sign_images/ # Sign language images (A-Z)
│ ├── css/
│ │ └── styles.css # Styling file
│ └── images/ # Logo and background images
├── templates/
│ ├── index.html # Main translation page
│ ├── about.html # About page
│ └── welcome.html # Welcome splash screen
├── uploads/ # Temporary folder for audio
├── requirements.txt # Required Python libraries
└── README.md # This file

yaml
Copy
Edit

---

## 🛠️ Installation

### 🔸 Prerequisites

- Python ≥ 3.8
- `pip` installed
- Git

---

### 🔸 Clone Repository

```bash
git clone https://github.com/yourusername/Signify.git
cd Signify
🔸 Create Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
🔸 Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
Required libraries include:
Flask, SpeechRecognition, transformers, pyaudio, torch, librosa, soundfile, scikit-learn, etc.

🚀 Running the Application
🖥️ Run Flask App
bash
Copy
Edit
python app.py
Visit http://127.0.0.1:5000 in your browser.

🧪 How to Use
Launch the app.

You’ll see a splash screen → then About → then Speak Interface.

Click the 🎤 button to start speaking.

Your speech will be converted to text using Wav2Vec 2.0.

The text is broken into characters, each rendered as sign language gestures.

Images corresponding to each character appear on the screen in real-time.

📂 Notes
Ensure your microphone is enabled and accessible via the browser.

Add your Sign_images (A-Z) in static/Sign_images/ folder.

The logo image and background should be added under static/images/.

✍️ Contributors
Kasi Viswanathan K, Student, SRMIST

Elatchuman RV, Student, SRMIST

Karthikeyan M, Assistant Professor, SRMIST

Sandhia GK, Associate Professor, SRMIST

📜 License
This project is developed for academic and research purposes.

💡 Future Scope
Add dynamic gesture animations using ViT + video sequences

Integrate multi-lingual support using Whisper

Build Android version using Flutter

Use ViT for dynamic video gesture generation from text

yaml
Copy
Edit
