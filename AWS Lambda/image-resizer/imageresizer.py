import numpy as np
def resize(image, scale):
    # Define new picture
    if scale >= 1.0:
        return
    max_x = int(scale * len(image))
    max_y = int(scale * len(image[0]))
    sized_image = np.ndarray(shape=(max_x, max_y, 3), dtype=np.uint8)
    rec_scale = 1 / scale
    for i in range(max_x):
        oldX = int(rec_scale * i)
        for k in range(max_y):
            oldY = int(rec_scale * k + (oldX % scale))
            sized_image[i][k] = image[oldX][oldY][0:3]

    return sized_image