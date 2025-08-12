Animal Image Classification with ResNet50

📌 Overview
A deep learning project for classifying animal images using Transfer Learning with ResNet50. Built with PyTorch, trained on a custom dataset combined from multiple sources, and achieving 96.59% validation accuracy.
Key Features:
- End-to-end image classification pipeline.
- Data preprocessing and augmentation for better generalization.
- ResNet50 fine-tuned for optimal performance.
- Achieved 96.59% validation accuracy.
- Evaluation using confusion matrix and classification report.
- Model was trained on kaggle and deployed on streamlit(https://animalimageclassificationresnet50-gyvtphv5nivq8wbtedsgcu.streamlit.app/)

📂 Dataset
This project uses a custom dataset created by merging multiple sources into a unified animal image classification dataset. The dataset contains 10 animal classes:

- 🦋 Butterfly
- 🐱 Cat
- 🐔 Chicken
- 🐄 Cow
- 🐶 Dog
- 🐘 Elephant
- 🐎 Horse
- 🐑 Sheep
- 🕷 Spider
- 🐿 Squirrel

Folder Structure:
<pre>dataset/
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
    └── squirrel/ </pre>


📊 Results
- Best Validation Accuracy: 96.59%
- Example Confusion Matrix: (Generated during evaluation)
- Sample Predictions: (Example outputs with predicted labels)

📈 Future Improvements
- Expand dataset for more animal classes.
- Apply model pruning or quantization for edge deployment.

📜 License
This project is licensed under the MIT License - see the LICENSE file for details.
