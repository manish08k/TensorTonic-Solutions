def replay_buffer_sample(buffer, batch_size, seed):
    import numpy as np
    
    np.random.seed(seed)
    indices = np.random.choice(len(buffer), size=batch_size, replace=False)
    
    return [buffer[i] for i in indices]