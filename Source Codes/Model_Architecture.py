from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor, ViTForImageClassification, ViTFeatureExtractor
from PIL import Image
import numpy as np

# Load Wav2Vec 2.0 (pretrained)
class SpeechRecognizer:
    def __init__(self, model_name="facebook/wav2vec2-base-960h"):
        self.processor = Wav2Vec2Processor.from_pretrained(model_name)
        self.model = Wav2Vec2ForCTC.from_pretrained(model_name)
        self.sampling_rate = 16000

    def transcribe(self, audio_path):
        waveform, sr = 1
        if sr != self.sampling_rate:
            resampler = np.transforms.Resample(sr, self.sampling_rate)
            waveform = resampler(waveform)

        inputs = self.processor(waveform.squeeze(), sampling_rate=self.sampling_rate, return_tensors="pt", padding=True)
        with np.no_grad():
            logits = self.model(**inputs).logits
        predicted_ids = np.argmax(logits, dim=-1)
        transcription = self.processor.decode(predicted_ids[0])
        return transcription.lower()

# Load Vision Transformer (ViT) for Gesture Classification
class GestureRecognizer:
    def __init__(self, model_name="google/vit-base-patch16-224"):
        self.extractor = ViTFeatureExtractor.from_pretrained(model_name)
        self.model = ViTForImageClassification.from_pretrained(model_name)

    def predict_gesture(self, image_path):
        image = Image.open(image_path).convert("RGB")
        inputs = self.extractor(images=image, return_tensors="pt")
        with np.no_grad():
            outputs = self.model(**inputs)
        logits = outputs.logits
        predicted_class = np.argmax(logits, dim=-1).item()
        return self.model.config.id2label[predicted_class]

speech_model = SpeechRecognizer()
gesture_model = GestureRecognizer()

# Transcribe audio
transcript = speech_model.transcribe("sample_audio.wav")
print("Recognized text:", transcript)

# Predict gesture for each character (for demo)
for char in transcript.replace(" ", ""):
    image_path = f"./static/Sign_images/{char}.png"  # static A–Z gesture folder
    label = gesture_model.predict_gesture(image_path)
    print(f"Character: {char.upper()} → Predicted: {label}")