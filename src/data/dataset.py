from torch.utils.data import Dataset
from pathlib import Path
import cv2

class CrackDataset(Dataset):
    def __init__(self, root_dir: Path, transform=None) -> None:
        self.transform = transform
        self.root_dir = root_dir
        self.samples = self._load_samples()

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, index):
        image_path, label = self.samples[index]

        image = cv2.imread(str(image_path))

        if self.transform:
            image = self.transform(image)

        return image, label

    def _load_samples(self) -> list[tuple[Path, int]]:
        samples = []
        
        n_dir = self.root_dir / "Negative"
        p_dir = self.root_dir / "Positive"

        for image_path in n_dir.glob("*.jpg"):
            samples.append((image_path,0))

        for image_path in p_dir.glob("*.jpg"):
            samples.append((image_path, 1))

        return samples