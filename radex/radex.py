import numpy as np
from PIL import Image
from .utils import (
    calculate_all_bs, f_given_x, fill_in_the_xs_for_y,
    transform_padding
)

def get_xs_ys_new_cubic_radon(N, a_lb, a_ub, step_a, bs):
    list_xs, list_ys = [], []
    x = [j for j in range(N)]

    for a in np.arange(a_lb, a_ub, step_a):
        for b in bs:
            y = f_given_x(x, a, b, N)
            y = transform_padding(y, max_val=N)
            x_new, y_new = fill_in_the_xs_for_y(x, y, a, b, N)
            if y_new.shape[0] != y.shape[0]:
                list_xs.append(x_new)
                list_ys.append(y_new)
            else:
                list_xs.append(x)
                list_ys.append(y)
    return list_xs, list_ys

def populate_image_matrix(empty_image, im, list_xs, list_ys, a_lb, a_ub, step_a, bs):
    item_number, row_num = 0, 0
    for a in np.arange(a_lb, a_ub, step_a):
        col_num = 0
        for b in bs:
            xs, ys = list_xs[item_number], list_ys[item_number]
            pixel_sum = np.sum(im[xs, ys]) / len(xs)
            empty_image[row_num][col_num] = pixel_sum
            item_number += 1
            col_num += 1
        row_num += 1
    return empty_image

def create_empty_image(a_lb, a_ub, step_a, bs):
    nrows = len(np.arange(a_lb, a_ub, step_a))
    ncols = len(bs)
    return np.zeros([nrows, ncols])

def get_radon_transform(file_path, a_lb, a_ub, step_a, bs, list_xs, list_ys, resize_dim=(512, 512)):
    N = resize_dim[0]
    
    empty_image1 = create_empty_image(a_lb, a_ub, step_a, bs)
    im = Image.open(file_path).convert('L').resize(resize_dim)
    im = np.array(im)
    im = (im - np.min(im)) / (np.max(im) - np.min(im))
    empty_image1 = populate_image_matrix(empty_image1, im, list_xs, list_ys, a_lb, a_ub, step_a, bs)

    empty_image2 = create_empty_image(a_lb, a_ub, step_a, bs)
    im = Image.open(file_path).convert('L').resize(resize_dim)
    im = np.array(im)[::-1, ::-1]
    im = (im - np.min(im)) / (np.max(im) - np.min(im))
    empty_image2 = populate_image_matrix(empty_image2, im, list_xs, list_ys, a_lb, a_ub, step_a, bs)

    final_img = np.concatenate([empty_image1, empty_image2])

    final_img_resized = Image.fromarray(
        (final_img * 255).astype(np.uint8)
    ).resize(resize_dim)

    return final_img_resized

def generate_radex_image(image_path, step_divisor=10, resize_dim=(512, 512)):
    N = resize_dim[0]
    a_lb, a_ub, b_lb, b_ub, b_big_step = 0, N+1, -6, 6, 0.5
    step_a = N / step_divisor
    tiny_bs, pick_up_b_list = 150, 256

    bs = calculate_all_bs(N, a_lb, a_ub, step_a, b_lb, b_ub, b_big_step, tiny_bs, pick_up_b_list)
    list_xs, list_ys = get_xs_ys_new_cubic_radon(N, a_lb, a_ub, step_a, bs)

    radex_img = get_radon_transform(image_path, a_lb, a_ub, step_a, bs, list_xs, list_ys, resize_dim)
    
    return radex_img

