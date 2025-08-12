import streamlit as st
import torch
import torchvision.transforms as transforms
from PIL import Image
from torchvision.models import resnet50

# Class labels
class_names = [
    "butterfly", "cat", "chicken", "cow", "dog",
    "elephant", "horse", "sheep", "spider", "squirrel"
]

@st.cache_resource
def load_model():
    model = resnet50(pretrained=False)
    model.fc = torch.nn.Linear(model.fc.in_features, len(class_names))
    model.load_state_dict(torch.load("resnet50_animal_classifier.pth", map_location="cpu"))
    model.eval()
    return model

model = load_model()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

st.title("🐾 Animal Image Classification with ResNet50")
st.write("Upload an animal image to classify.")

file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if file:
    img = Image.open(file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_container_width=True)  # ✅ updated here
    img_t = transform(img).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img_t)
        _, pred = torch.max(outputs, 1)
    st.success(f"**Predicted:** {class_names[pred.item()]}")
