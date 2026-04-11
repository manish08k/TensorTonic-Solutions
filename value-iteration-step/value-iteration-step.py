def value_iteration_step(values, transitions, rewards, gamma):
    n_states = len(values)
    new_values = [0.0] * n_states

    for s in range(n_states):
        action_values = []

        for a in range(len(transitions[s])):
            q = rewards[s][a]

            for s_next in range(n_states):
                q += gamma * transitions[s][a][s_next] * values[s_next]

            action_values.append(q)

        new_values[s] = max(action_values)

    return new_values