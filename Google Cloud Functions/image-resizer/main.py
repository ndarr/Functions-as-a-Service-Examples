import base64
import requests
from PIL import Image
from io import BytesIO
import numpy as np
import os

from imageresizer import resize


def handler(request):
    # Retrieve url to image from request
    imgurl = request['imgurl']
    filename = "/tmp/out.jpg"

    # Retrieve image
    response = requests.get(imgurl)
    img = Image.open(BytesIO(response.content))

    # Convert img data into NumPy-Array
    img_raw = np.array(img)

    # Resize Image
    resized_image_raw = resize(img_raw, scale=0.1)

    # Convert Array back to image
    resized_image = Image.fromarray(resized_image_raw)
    # Save image to local disk
    resized_image.save(filename)

    # Read bytes from image and encode them
    with open(filename, 'rb') as f:
        encode_img = base64.standard_b64encode(f.read())

    # Clean up disk
    os.remove(filename)

    # Send response with encoded image
    return {
        'img': str(encode_img, "utf-8")
    }
