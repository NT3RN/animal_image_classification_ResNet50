Animal Image Classification with ResNet50

📌 Overview
A deep learning project for classifying animal images using Transfer Learning with ResNet50. Built with PyTorch, trained on a custom dataset combined from multiple sources, and achieving 96.59% validation accuracy.
Key Features:
- End-to-end image classification pipeline.
- Data preprocessing and augmentation for better generalization.
- ResNet50 fine-tuned for optimal performance.
- Achieved 96.59% validation accuracy.
- Evaluation using confusion matrix and classification report.
- Model was trained on kaggle

📂 Dataset
This project uses a custom dataset created by merging multiple sources into a unified animal image classification dataset. The dataset contains 10 animal classes:
🦋 Butterfly
🐱 Cat
🐔 Chicken
🐄 Cow
🐶 Dog
🐘 Elephant
🐎 Horse
🐑 Sheep
🕷 Spider
🐿 Squirrel

Folder Structure:
dataset/
├── train/
│   ├── butterfly/
│   ├── cat/
│   ├── chicken/
│   ├── cow/
│   ├── dog/
│   ├── elephant/
│   ├── horse/
│   ├── sheep/
│   ├── spider/
│   └── squirrel/
├── validation/
│   ├── butterfly/
│   ├── cat/
│   ├── chicken/
│   ├── cow/
│   ├── dog/
│   ├── elephant/
│   ├── horse/
│   ├── sheep/
│   ├── spider/
│   └── squirrel/
└── test/
    ├── butterfly/
    ├── cat/
    ├── chicken/
    ├── cow/
    ├── dog/
    ├── elephant/
    ├── horse/
    ├── sheep/
    ├── spider/
    └── squirrel/

🛠️ Installation
1. Clone the repository:
   git clone https://github.com/NT3RN/animal_image_classification_ResNet50 \n
   cd animal_image_classification_ResNet50

3. Create virtual environment (optional but recommended):
   python -m venv venv \n
   source venv/bin/activate   # On Windows use: venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt
🚀 Usage
1. Training the Model:
   python train.py

2. Testing the Model:
   python test.py

3. Running the Jupyter Notebook:
   jupyter notebook animal-2-test.ipynb

📊 Results
Best Validation Accuracy: 96.59%
Example Confusion Matrix: (Generated during evaluation)
Sample Predictions: (Example outputs with predicted labels)

📈 Future Improvements
- Deploy as a Streamlit or Flask web application.
- Expand dataset for more animal classes.
- Apply model pruning or quantization for edge deployment.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
