import cv2
import numpy as np
import tensorflow.keras.models as models

# Load the pre-trained CNN model
model_path = "C:/Users/hridh/Downloads/Plant disease detection system/kaggle/working/model1.h5"
model = models.load_model(model_path)

# Load the input image
image_path = "C:/Users/hridh/Downloads/Plant disease detection system/sample_image.jpg"
img = cv2.imread(image_path)

# Check if image is loaded correctly
if img is None:
    raise ValueError(f"Error: Image not found at {image_path}. Please check the file path.")

# Convert BGR to RGB (if required)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Resize to match model input shape
img = cv2.resize(img, (224, 224))  # Change (224, 224) if needed

# Preprocess image
img = img / 255.0  # Normalize
img = np.expand_dims(img, axis=0)  # Add batch dimension

# Predict on the input image
preds = model.predict(img)

# Print the predictions
print("Predictions:", preds)
