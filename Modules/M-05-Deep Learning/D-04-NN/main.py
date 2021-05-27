import numpy as np
import matplotlib.pyplot as plt
import torch
import torchvision as vn
from torchvision import transforms, datasets
from torch.utils.data import DataLoader
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

train = datasets.MNIST('', train=True, download=True, transform=transforms.Compose([
    transforms.ToTensor()
]))

test = datasets.MNIST('', train=False, download=True, transform=transforms.Compose([
    transforms.ToTensor()
]))

train_set = DataLoader(train, batch_size=32, shuffle=True)
test_set = DataLoader(test, batch_size=32, shuffle=False)


class NNet(nn.Module):
    def __init__(self):
        super(NNet, self).__init__()
        self.in_layer = nn.Linear(in_features=28*28, out_features=64)
        self.hl1 = nn.Linear(in_features=64, out_features=64)
        self.hl2 = nn.Linear(in_features=64, out_features=64)
        self.out_layer = nn.Linear(in_features=64, out_features=10)

    def feed_forward(self, x):
        x = F.relu(self.in_layer(x))
        x = F.relu(self.hl1(x))
        x = F.relu(self.hl2(x))
        x = F.log_softmax(self.out_layer(x), dim=1)
        return x


n_net = NNet()

optimizer = optim.SGD(n_net.parameters(), lr=0.1, momentum=0.9)
lr_decay = optim.lr_scheduler.CyclicLR(optimizer=optimizer, base_lr=0.0001, max_lr=0.1, step_size_down=2)

epochs = 20

for epoch in range(epochs):
    print(epoch)
    for data in train_set:
        X, y = data
        n_net.zero_grad()
        output = n_net.feed_forward(X.view(-1, 28*28))
        loss = F.nll_loss(output, y)
        loss.backward()
        optimizer.step()
    lr_decay.step()
    print(lr_decay.get_last_lr())
    print(loss)


correct_train = 0
total_train = 0

with torch.no_grad():
    for data in train_set:
        X, y = data
        output1 = n_net.feed_forward(X.view(-1, 784))
        for idx, i in enumerate(output1):
            if torch.argmax(i) == y[idx]:
                correct_train += 1
            total_train += 1

correct_test = 0
total_test = 0

with torch.no_grad():
    for data in test_set:
        X, y = data
        output1 = n_net.feed_forward(X.view(-1, 784))
        for idx, i in enumerate(output1):
            # if idx % 1000 == 0:
            #     print(f'True: {y[idx]}')
            #     print(f'Predicted: {torch.argmax(i)}')
            if torch.argmax(i) == y[idx]:
                correct_test += 1
            total_test += 1

print(f'Accuracy on train set: {round((correct_train/total_train)*100, 3)}%')
print(f'Accuracy on test set: {round((correct_test/total_test)*100, 3)}%')



