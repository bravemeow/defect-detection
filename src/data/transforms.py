import numpy as np
import cv2
import torch
from torchvision.transforms import v2


# values from 02_compute_mean_std.ipynb
MEAN = [0.69521675, 0.67518179, 0.64234832]
STD = [0.13157990, 0.12834182, 0.12764223]

class BGRToRGB():
    def __call__(self, image: np.ndarray):
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# using v2(newest version) to resize 'ndarray' directly
train_transform = v2.Compose([
    BGRToRGB(),
    v2.ToImage(),
    v2.Resize((224,224)),
    v2.ToDtype(torch.float32, scale=True),
    v2.Normalize(mean=MEAN, std=STD),
])

# all transforms are the same for now, since there's no random augmented.
val_transform = train_transform
test_transform = train_transform