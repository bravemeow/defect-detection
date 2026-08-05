from data.dataloader import create_loaders
from models.model import SimpleCNN

train_loader, val_loader, test_loader = create_loaders(
    data_dir = ("data/processed"),
    batch_size = 32,
)

model = SimpleCNN()

for images, label in train_loader:
    
    output = model(images)    
    print(images.shape)
    print(output.shape)
    print(output.max())
    break