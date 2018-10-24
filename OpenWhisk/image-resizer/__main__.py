from imageresizer import resize
from PIL import Image
import requests
from io import BytesIO
import base64
import os
import numpy as np


def main(args):
    filename = 'out.jpg'
    # Download Image
    response = requests.get(args['imgurl'])
    img = Image.open(BytesIO(response.content))

    # Convert img data into NumPy-Array
    imgRaw = np.array(img)

    # Resize Image
    resized_image_raw = resize(imgRaw, 0.1)

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
    return {"headers": {"Content-Type": "image/jpg", "statusCode": 200}, "body": str(encode_img, 'utf-8')}
