import base64
import json

import requests
from PIL import Image
from io import BytesIO
import numpy as np
import os

from imageresizer import resize

def handler(event, context):
    bodyRaw = event['body']
    body = json.loads(bodyRaw)
    imgurl = body['imgurl']
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
        'statusCode': 200,
        'body':json.dumps({
            'img': str(encodeImg, "utf-8")
        })
    }