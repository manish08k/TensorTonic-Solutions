def policy_gradient_loss(log_probs, rewards, gamma):
    """
    Compute REINFORCE policy gradient loss with mean-return baseline.
    """
    T = len(rewards)

    returns = [0.0] * T
    returns[-1] = rewards[-1]

    for t in range(T - 2, -1, -1):
        returns[t] = rewards[t] + gamma * returns[t + 1]

    mean_return = sum(returns) / T

    loss = 0.0
    for t in range(T):
        advantage = returns[t] - mean_return
        loss += log_probs[t] * advantage

    loss = -loss / T

    return loss