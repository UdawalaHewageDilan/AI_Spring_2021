import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from model import MNISTModel
import data_handler as dh


model = MNISTModel()
optimizer = optim.Adam(model.parameters(), lr=0.001)
loss_function = nn.NLLLoss()

for epoch in range(5):
    for data in dh.trainset:
        X, y = data
        model.zero_grad()
        output = model(X.view(-1, 784))
        loss = F.nll_loss(output, y)
        loss.backward()
        optimizer.step()
    print(loss)

    correct = 0
    total = 0

    with torch.no_grad():
        for data in dh.testset:
            X, y = data
            output = model(X.view(-1, 784))

            for idx, i in enumerate(output):
                if torch.argmax(i) == y[idx]:
                    correct += 1
                total += 1


print(correct/total)
torch.save(model, "Best_model2.pth")



