import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Models to compare
models = [
    "ConvLSTM (Base Model)", "Wav2Vec 2.0", "Transformer-TTS", "Whisper",
    "ViT", "SpeechT5", "Seq2Seq", "Multimodal Transformer", "Fine-tuned GPT"
]

# Simulated accuracy, F1-score, and precision values (realistic values based on prior comparison)
accuracy = [92.4, 97.1, 91.2, 94.5, 96.7, 93.3, 91.7, 94.6, 92.3]
f1_score = [91.8, 96.5, 90.8, 93.7, 95.6, 92.1, 90.4, 93.8, 91.2]
precision = [90.5, 95.3, 89.4, 93.4, 94.3, 91.8, 88.9, 94.0, 90.1]

# Create a DataFrame for visualization
df = pd.DataFrame({
    "Model": models,
    "Accuracy": accuracy,
    "F1-Score": f1_score,
    "Precision": precision
})

# Set figure size
plt.figure(figsize=(12, 6))

# Line plot for Accuracy, F1-Score, and Precision in one graph
sns.lineplot(x="Model", y="Accuracy", data=df, marker="o", label="Accuracy", color="blue")
sns.lineplot(x="Model", y="F1-Score", data=df, marker="o", label="F1-Score", color="green")
sns.lineplot(x="Model", y="Precision", data=df, marker="o", label="Precision", color="red")

# Rotate x-axis labels for better readability
plt.xticks(rotation=45, ha="right")

# Set labels and title
plt.ylabel("Scores (%)")
plt.title("Comparison of Model Performance: Accuracy, F1-Score, and Precision")
plt.legend(title="Metrics")
plt.grid(True)

# Display the plot
plt.tight_layout()
plt.show()

# Display data in tabular format for reference
import ace_tools as tools
tools.display_dataframe_to_user(name="Model Performance Comparison", dataframe=df)
