def linear_lr(step, total_steps, initial_lr, final_lr=0.0, warmup_steps=0):

    if step >= total_steps:
        return float(final_lr)


    if warmup_steps > 0 and step < warmup_steps:
        return (step / warmup_steps) * initial_lr


    decay_start = warmup_steps
    decay_steps = total_steps - warmup_steps

    if decay_steps <= 0:
        return float(final_lr)

    t = step - decay_start
    return final_lr + (initial_lr - final_lr) * (decay_steps - t) / decay_steps