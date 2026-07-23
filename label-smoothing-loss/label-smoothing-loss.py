import math

def label_smoothing_loss(predictions, target, epsilon):
    k = len(predictions)
    loss = 0.0

    for i in range(k):
        q = epsilon / k

        if i == target:
            q += 1 - epsilon

        loss -= q * math.log(predictions[i])

    return loss