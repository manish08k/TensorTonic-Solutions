import numpy as np

def wasserstein_critic_loss(real_scores, fake_scores):
    """
    Compute Wasserstein Critic Loss.
    """
    mean_real = np.mean(real_scores)
    mean_fake = np.mean(fake_scores)
    
    return mean_fake - mean_real