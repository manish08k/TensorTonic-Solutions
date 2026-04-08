def sarsa_update(q_table, state, action, reward, next_state, next_action, alpha, gamma):
    new_q = [row[:] for row in q_table]
    current_q = q_table[state][action]
    next_q = q_table[next_state][next_action]
    delta = reward + gamma * next_q - current_q
    new_q[state][action] = current_q + alpha * delta
    
    return new_q