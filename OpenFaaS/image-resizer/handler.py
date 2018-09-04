import numpy
import imageio
import matplotlib.pyplot as plt
import sys


def resize(image, scale):
    # Define new picture
    if scale >= 1.0:
        return
    max_x = int(scale * len(image))
    max_y = int(scale * len(image[0]))
    sized_image = numpy.ndarray(shape=(max_x, max_y, 3), dtype=numpy.uint8)
    rec_scale = 1 / scale
    for i in range(max_x):
        oldX = int(rec_scale * i)
        for k in range(max_y):
            oldY = int(rec_scale * k + (oldX % scale))
            sized_image[i][k] = image[oldX][oldY][0:3]

    return sized_image


def handle(req):
    """handle a request to the function
    Args:
        req (str): Url to image
    """

    # Download Image
    img = imageio.imread(req)

    #TODO: Define scale from absolute goal res like scale down to max 640x480

    #Resize Image
    resizedImage = resize(img, 0.1)

    #TODO: use uuid() for unique filenames
    plt.imsave('out.jpg', resizedImage)

    #Return image
    with open('out.jpg', 'rb') as f:
        data = f.read()
        sys.stdout.buffer.write(data)

    #TODO: delete temporary file
    return