# save_images.py
from datasets import load_dataset
import os
from tqdm import tqdm

# Load dataset
dataset = load_dataset("JamieWithofs/Deepfake-and-real-images", split="train")

# Create folders for saving
os.makedirs("data/real", exist_ok=True)
os.makedirs("data/fake", exist_ok=True)

# Save first 500 images (for testing)
for i, item in enumerate(tqdm(dataset)):
    label = 'real' if item['label'] == 0 else 'fake'
    img = item['image']  # PIL Image object
    img_path = f"data/{label}/{i}.jpg"

    try:
        img.save(img_path)
    except Exception as e:
        print(f"Failed to save image {i}: {e}")

    if i >= 500:
        break

print("Finished saving images.")
