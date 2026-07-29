import random
from pathlib import Path
import shutil

SEED = 42  # seed 42 as convention

DATA_DIR = Path("./data/raw/surface-crack")
PROCESSED_DIR = Path("./data/processed")

n_dir = DATA_DIR / "Negative"
p_dir = DATA_DIR / "Positive"

def main():
    nImages = get_images(n_dir)
    pImages = get_images(p_dir)

    nTrain, nVal, nTest = split_images(nImages, 0.8, 0.1)
    pTrain, pVal, pTest = split_images(pImages, 0.8, 0.1)

    copy_images(nTrain, PROCESSED_DIR / "train" / "Negative")
    copy_images(pTrain, PROCESSED_DIR / "train" / "Positive")
    copy_images(nVal, PROCESSED_DIR / "val" / "Negative")
    copy_images(pVal, PROCESSED_DIR / "val" / "Positive")
    copy_images(nTest, PROCESSED_DIR / "test" / "Negative")
    copy_images(pTest, PROCESSED_DIR / "test" / "Positive")

    print("completed.")


def get_images(path: Path) -> list[Path]:
    return list(path.glob("*.jpg"))


def split_images(images: list[Path], 
                 train_ratio: float=0.8, 
                 val_ratio: float=0.1, # test_ratio = 0.1
                 ) -> tuple[list[Path], list[Path], list[Path]]:
    assert train_ratio + val_ratio < 1

    images = images.copy()
    random.seed(SEED)
    random.shuffle(images)

    train_end = int(len(images) * train_ratio)
    val_end = train_end + int(len(images) * val_ratio)
    
    train_images = images[:train_end]
    val_images = images[train_end:val_end]
    test_images = images[val_end:]
    
    return train_images, val_images, test_images


def copy_images(images: list[Path], destination: Path) -> None:
    for image in images:
        shutil.copy(image, destination)

if __name__ == "__main__":
    main()
