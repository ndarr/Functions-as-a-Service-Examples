import json
import imageio
import matplotlib.pyplot as plt
import sys
import os
from . import imageresizer


def handle(req):
    filename = 'out.jpg'
    # Retrieve url to image from request
    url = json.loads(req)['imgurl']
    # Retrieve image
    img = imageio.imread(url)

    # Resize Image
    resized_image = imageresizer.resize(img, 0.1)

    # Save resized image
    plt.imsave(filename, resized_image)

    # Write to STDOUT to return image
    with open(filename, 'rb') as f:
        data = f.read()
        sys.stdout.buffer.write(data)

    # Clean up disk
    os.remove(filename)
    return
