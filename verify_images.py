from PIL import Image
import matplotlib.pyplot as plt
import os

real_img_path = os.path.join("data", "real", os.listdir("data/real")[0])
fake_img_path = os.path.join("data", "fake", os.listdir("data/fake")[0])

real_img = Image.open(real_img_path)
fake_img = Image.open(fake_img_path)

plt.figure(figsize=(6,3))

plt.subplot(1,2,1)
plt.imshow(real_img)
plt.title("Real")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(fake_img)
plt.title("Fake")
plt.axis("off")

plt.show()
