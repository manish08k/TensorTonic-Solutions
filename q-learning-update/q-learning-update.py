def q_learning_update(Q, s, a, r, s_next, alpha, gamma):
    Q_new = [row[:] for row in Q]
    
    max_next = max(Q[s_next])
    target = r + gamma * max_next
    td_error = target - Q[s][a]
    
    Q_new[s][a] = Q[s][a] + alpha * td_error
    
    return Q_new