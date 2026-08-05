from data.dataloader import create_loaders
from models.model import SimpleCNN
import torch
import torch.nn as nn

train_loader, val_loader, test_loader = create_loaders(
    data_dir = ("data/processed"),
    batch_size = 32,
)
model = SimpleCNN()

criterion = nn.CrossEntropyLoss()

optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)

NUM_EPOCHS = 1

for epoch in range(NUM_EPOCHS):

    model.train()   # ML convention. It does nothing for this model.

    running_loss = 0
    correct = 0
    total = 0

    for batch_idx, (images, labels) in enumerate(train_loader):
        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        running_loss += loss.item()

        predictions = outputs.argmax(dim=1)

        correct += (predictions == labels).sum().item()

        total += labels.size(0)

        if (batch_idx + 1) % 100 == 0:
            print(
                f"Epoch {epoch + 1}/{NUM_EPOCHS} | "
                f"Batch {batch_idx + 1}/{len(train_loader)} | "
                f"Loss: {loss.item():.4f}"
            )

    avg_loss = running_loss / len(train_loader)

    accuracy = correct / total

    print(
        f"Epoch {epoch+1}/{NUM_EPOCHS} | "
        f"Loss: {avg_loss:.4f} | "
        f"Accuracy: {accuracy:.2%}"
    )