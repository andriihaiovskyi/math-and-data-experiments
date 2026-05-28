import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(42)
X_raw = np.linspace(-3,3,100)
Y_raw = 7*X_raw**3 - 5 * X_raw**2 + 4*X_raw + 2 + np.random.normal(0,.5,100)

indices = np.random.permutation(100)
train_idx, test_idx = indices[:80], indices[80:]

X_train, Y_train = X_raw[train_idx], Y_raw[train_idx]
X_test, Y_test = X_raw[test_idx], Y_raw[test_idx]

m = 0.0
a = 0.0
b = 0.0
c = 0.0


learning_rate = 2*10**-3
epochs = 2000
N = len(X_train)

plt.ion()
fig, ax = plt.subplots(figsize = (10,6))

print("---training started---")
for epoch in range(epochs+1):
    Y_pred_train =m*(X_train**3) + a * (X_train**2) + b * X_train + c
    dm = (2/N) * np.sum((X_train**3) * (Y_pred_train - Y_train))
    da = (2/N) * np.sum((X_train**2) * (Y_pred_train - Y_train))
    db = (2/N) * np.sum(X_train * (Y_pred_train - Y_train))
    dc = (2/N) * np.sum(Y_pred_train - Y_train)

    m -= learning_rate * dm
    a -= learning_rate * da
    b -= learning_rate * db
    c -= learning_rate * dc
    print(f"\n epoch: {epoch} y = {m:.2f}x3 + {a:.2f}x² + {b:.2f}x + {c:.2f}")

    if epoch % 100 ==0:

        ax.clear()
        X_line = np.linspace(-3, 3, 100)
        Y_line = m*(X_line**3) + a * (X_line ** 2) + b * X_line + c
        ax.scatter(X_train, Y_train, color='royalblue', label = 'Train Points', alpha=0.7)
        ax.scatter(X_test, Y_test, color='crimson', label='Test Points', alpha=0.9)
        ax.plot(X_line, Y_line, color='darkorange', linewidth=3, label='AI Prediction')

        loss = np.mean((Y_pred_train - Y_train)**2)
        ax.set_title(f'Epoch: {epoch} | Training Loss: {loss:.4f}', fontsize = 14)
        ax.set_xlabel("Input (X)", fontsize=12)
        ax.set_ylabel("Output (Y)", fontsize=12)
        ax.legend(loc='upper center')
        ax.set_ylim(-20, 25)
        plt.draw()
        plt.pause(0.05)
plt.ioff() # Turn off interactive mode
print(f"\nTraining Finished! Final formula: y = {m:.2f}x3 + {a:.2f}x² + {b:.2f}x + {c:.2f}")
plt.show()
