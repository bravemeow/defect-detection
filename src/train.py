from data.dataloader import create_loaders


train_loader, val_loader, test_loader = create_loaders(
    data_dir = ("data/processed"),
    batch_size = 32,
)
