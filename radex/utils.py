import numpy as np

def transform_padding(v, min_val=0, max_val=64):
    v = np.round(v).astype(int)
    v[v >= max_val] = max_val - 1
    v[v < min_val] = min_val
    return v

def pick_elements(lst, x):
    """Pick x elements from a list at equal intervals."""
    n = len(lst)
    interval = n // x
    return [lst[i * interval] for i in range(x)]

def f_given_x(x, a, b, N):
    exp_term = np.float64(b * (x - a))
    return N * ((np.exp(exp_term) - 1) / (np.exp(exp_term) + 1) + 1) / 2

def f_given_y(y, a, b, N):
    return a + (1/b)*(np.log(y / (N - y)))

def f_b_given_x_y_a_N(x, y, a, N):
    denom = 1 / (x - a)
    return denom * np.log(y / (N - y))

def fill_in_the_xs_for_y(x, y, a, b, N):
    x_new_list, y_new_list = [], []

    for i in range(y.shape[0]-1):
        before_y, after_y = y[i], y[i+1]
        x_new_list.append(x[i])
        y_new_list.append(y[i])

        if abs(after_y - before_y) > 1:
            for new_y in range(before_y + 1, after_y):
                new_x = f_given_y(new_y, a, b, N)
                x_new_list.append(new_x)
                y_new_list.append(new_y)
                
    x_new_list = transform_padding(np.array(x_new_list), max_val=N)
    y_new_list = transform_padding(np.array(y_new_list), max_val=N)

    return x_new_list, y_new_list

def calculate_all_bs(N, a_lb, a_ub, step_a, b_lb, b_ub, b_big_step, tiny_bs, pick_up_b_list=100):
    x = N / 2
    b_list = []

    for a in np.arange(a_lb, a_ub, step_a):
        if a == N/2:
            continue
        for y in np.arange(N/2, N, 1):
            b = f_b_given_x_y_a_N(x, y, a, N)
            b_list.append(b)

    b_list = np.sort(np.array(b_list))
    
    if len(b_list) < tiny_bs:
        raise ValueError(f"Too few b values: {len(b_list)} < {tiny_bs}")

    b_neg_list = np.arange(b_lb, np.min(b_list), b_big_step)
    b_pos_list = np.arange(np.max(b_list), b_ub, b_big_step)
    b_list_chosen = np.array(pick_elements(list(b_list), pick_up_b_list))

    bs = np.concatenate([b_neg_list, b_list_chosen, b_pos_list])
    return bs
