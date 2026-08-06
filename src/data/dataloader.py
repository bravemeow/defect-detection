from pathlib import Path
from torch.utils.data import DataLoader
from .dataset import CrackDataset
from .transforms import (
    train_transform,
    val_transform,
    test_transform,
)

def create_loaders(data_dir, batch_size):
    train_dataset = CrackDataset(
        Path(data_dir) / "train",
        transform=train_transform,
    )
    train_loader = DataLoader(
        train_dataset,
        batch_size=batch_size,
        shuffle=True,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True
    )

    val_dataset = CrackDataset(
        Path(data_dir) / "val",
        transform=val_transform,
    )
    val_loader = DataLoader(
        val_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True
    )

    test_dataset = CrackDataset(
        Path(data_dir) / "test",
        transform=test_transform,
    )
    test_loader = DataLoader(
        test_dataset,
        batch_size=batch_size,
        shuffle=False,
        num_workers=8,
        pin_memory=True,
        persistent_workers=True
    )

    return train_loader, val_loader, test_loader