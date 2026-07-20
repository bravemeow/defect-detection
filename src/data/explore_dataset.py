from pathlib import Path
import cv2

DATA_DIR = Path("data/raw/surface_crack")

for label_dir in DATA_DIR.iterdir():
    images = list(label_dir.glob("*.jpg"))

    print(label_dir.name)
    print("count:", len(images))

    image = cv2.imread(str(images[0]))
    print("shape:", image.shape)