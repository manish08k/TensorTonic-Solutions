import numpy as np

def cross_entropy_loss(y_true, y_pred):
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    probs = y_pred[np.arange(len(y_true)), y_true]
    loss = -np.mean(np.log(probs))

    return loss