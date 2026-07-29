import random
from pathlib import Path

SEED = 42  # seed 42 as convention

DATA_DIR = Path("./data/raw/surface-crack")
negative_dir = DATA_DIR / "Negative"
positive_dir = DATA_DIR / "Positive"


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
