"""Train the tiny MNIST MLP used by Part 7 (the digit-reader capstone).

This produces `mnist_mlp.pt`, the state dict the blog post and notebook load.
Run it once (Colab CPU is fine, ~30s) and commit the resulting .pt next to this
file. The architecture MUST match the one rebuilt in the post:

    nn.Sequential(nn.Flatten(), nn.Linear(784, 128), nn.ReLU(), nn.Linear(128, 10))

Usage:
    pip install torch torchvision
    python train_mnist_mlp.py
"""
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

tfm = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,), (0.3081,)),  # the mean/std the post reuses
])
train = datasets.MNIST(root="./data", train=True, download=True, transform=tfm)
loader = DataLoader(train, batch_size=128, shuffle=True)

mlp = nn.Sequential(
    nn.Flatten(),
    nn.Linear(28 * 28, 128),
    nn.ReLU(),
    nn.Linear(128, 10),
)
opt = torch.optim.Adam(mlp.parameters(), lr=1e-3)
loss_fn = nn.CrossEntropyLoss()

mlp.train()
for epoch in range(3):  # ~97% test accuracy is plenty for the demo
    for xb, yb in loader:
        opt.zero_grad()
        loss_fn(mlp(xb), yb).backward()
        opt.step()
    print(f"epoch {epoch + 1} done")

torch.save(mlp.state_dict(), "mnist_mlp.pt")
print("saved mnist_mlp.pt")
