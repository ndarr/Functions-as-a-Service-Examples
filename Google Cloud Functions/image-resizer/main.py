import base64
import requests
from PIL import Image
from io import BytesIO
import numpy as np
import os

from imageresizer import resize

def handler(request):
    imgurl = request['imgurl']
    filename = "/tmp/out.jpg"
    response = requests.get(imgurl)
    img = Image.open(BytesIO(response.content))

    imgRaw = np.array(img)

    resizedImageRaw = resize(imgRaw, scale = 0.1)

    resizedImage = Image.fromarray(resizedImageRaw)
    resizedImage.save(filename)

    with open(filename, 'rb') as f:
        encodeImg = base64.standard_b64encode(f.read())

    os.remove(filename)

    return {
        'img': str(encodeImg, "utf-8")
    }