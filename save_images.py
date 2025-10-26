from datasets import load_dataset
import os
from tqdm import tqdm

dataset = load_dataset("JamieWithofs/Deepfake-and-real-images", split="train")

os.makedirs("data/real", exist_ok=True)
os.makedirs("data/fake", exist_ok=True)

for i, item in enumerate(tqdm(dataset)):
    label = 'real' if item['label'] == 0 else 'fake'
    img = item['image']  
    img_path = f"data/{label}/{i}.jpg"

    try:
        img.save(img_path)
    except Exception as e:
        print(f"Failed to save image {i}: {e}")

    if i >= 500:
        break

print("Finished saving images.")
