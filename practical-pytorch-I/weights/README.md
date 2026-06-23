# Weights for Part 7 (the digit-reader capstone)

`mnist_mlp.pt` is the trained state dict that the Part 7 post and notebook load.
Phase I doesn't train, so this is shipped pre-trained — exactly what "pretrained" means.

**To generate it** (one-time, ~30s on Colab CPU):

```bash
pip install torch torchvision
python train_mnist_mlp.py   # writes mnist_mlp.pt next to this file
```

Then commit `mnist_mlp.pt` here. The post loads it from:
`https://github.com/engineers-musings/blog-companion/raw/main/practical-pytorch-I/weights/mnist_mlp.pt`

The architecture must stay in sync with the post:
`nn.Sequential(nn.Flatten(), nn.Linear(784, 128), nn.ReLU(), nn.Linear(128, 10))`.
