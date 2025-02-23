# 🌿 Plant Disease Detection System (Alpha Version)

## 📌 Overview
The **Plant Disease Detection System** is a deep learning-based solution that helps identify plant diseases from images. Using a Convolutional Neural Network (CNN), this system classifies plant leaf images and provides predictions on potential diseases, enabling early intervention and better crop health management.

🚧 **Note:** This project is currently in its **alpha** phase and is not yet complete. Features and functionality may change significantly as development progresses.

## 🚀 Features (Planned)
- 🌱 Identifies diseases in plants using image classification.
- 🤖 Powered by a pre-trained CNN model.
- 📷 Accepts images of leaves as input.
- 📊 Provides accurate predictions with confidence scores.
- 🖥️ Easy-to-use Python script for inference.

## 🛠️ Installation

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/plant-disease-detection.git
cd plant-disease-detection
```

### 2️⃣ Install Dependencies
Make sure you have Python 3.10 or 3.11 installed. Then, install required libraries:
```sh
pip install -r requirements.txt
```

### 3️⃣ Download the Model (Future Update)
Ensure you have the trained model file (`model.h5`) placed inside the project directory. If needed, you can train your own model using the provided dataset and scripts.

## 🔍 Usage

### 🌿 Detecting Plant Diseases
Run the following command to classify an image:
```sh
python run.py --image path/to/your/image.jpg
```

Example:
```sh
python run.py --image sample_image.jpg
```

### 🖼️ Input
Provide an image of a plant leaf (JPEG/PNG format). Ensure the image is clear and properly captured.

### 📌 Output
The model will output the predicted disease category and confidence score.

## 🏗️ Project Structure
```
📂 plant-disease-detection/
├── 📄 README.md
├── 📄 requirements.txt
├── 📝 run.py  # Main script for inference
├── 📁 models/  # Directory for trained model files
│   ├── model.h5 (Coming Soon)
├── 📁 images/  # Sample images for testing
├── 📁 dataset/  # Optional dataset for training
└── 📁 notebooks/  # Jupyter notebooks for model training
```

## 📊 Training the Model (Planned Feature)
Training functionality will be added in a future update. Stay tuned!

## 🛠️ Troubleshooting
- **Error: No module named 'tensorflow'** ➝ Install TensorFlow: `pip install tensorflow`
- **Error: Image not loading** ➝ Ensure the file path is correct.
- **Python version issues** ➝ Use Python 3.10 or 3.11 for compatibility.

## 🤝 Contribution
This project is in its early stages. Contributions, feedback, and issue reports are welcome! 🚀

## 📜 License
This project is open-source and licensed under the MIT License.

## 👨‍💻 Author
Developed by **TUSHAR GOYAL, HRIDHANU BOSE, ADITYA PARMAR**  

## 📝 Note
- In files (Plant disease detection system\model1.h5\variables)
- (variables.data-00000-of-00001), data is missing due to size constraints. Please download and replace it from the link provided.
- https://drive.google.com/file/d/1cpzfMjsVg9u2rhaUyM-5eQwWekcQCzZD/view?usp=sharing
