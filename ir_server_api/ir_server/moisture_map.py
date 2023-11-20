from random import randrange

import cv2
import matplotlib.pyplot as plt
import numpy as np
from cv2 import add


def str_2_np(s):
    lines = s.splitlines()
    data_idx = lines.index("[Data]")
    lines = lines[data_idx + 1 : data_idx + 512]

    bytes_str = [l.replace(",", ".").strip("	").split("	") for l in lines]
    bytes = [list(map(float, l)) for l in bytes_str]
    np_arr = np.array(bytes)
    return np_arr


def calc_mean_heat(ref):
    mean_np_1 = np.mean(ref, axis=1)
    mean_np = np.mean(mean_np_1, axis=0)
    return


def calc_cov_map(heat_map, heat_ref):
    (
        w,
        h,
        t,
    ) = heat_map.shape
    cov_map = np.zeros((w, h))
    for i in range(w):
        for j in range(h):
            cov_map[i, j] = np.cov(heat_map[i, j, :], heat_ref)[1, 0]
    return cov_map


def float_2_colormap(np_arr):
    np_img = 255 * (np_arr - np_arr.min()) / (np_arr.max() - np_arr.min())
    np_img = np_img.astype(np.uint8)
    color_map = cv2.applyColorMap(np_img, cv2.COLORMAP_INFERNO)
    return color_map


def float_2_normalized(np_arr):
    np_img = 255 * (np_arr - np_arr.min()) / (np_arr.max() - np_arr.min())
    return np_img


def read_from_asc(asc_file):
    with open(asc_file, encoding="CP932") as f:
        f = f.read()
        np_img = str_2_np(f)
    return np_img


def read_from_png(png_file):
    return cv2.imread(png_file, cv2.IMREAD_GRAYSCALE)
