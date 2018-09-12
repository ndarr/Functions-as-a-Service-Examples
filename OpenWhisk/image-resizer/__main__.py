from imageresizer import resize
from PIL import Image
import requests
from io import BytesIO
import base64
import os
import numpy as np
import json



def main(args):
    #json.dumps(args)
    filename = 'out.jpg'
    # Download Image
    response = requests.get(args['imgurl'])
    img = Image.open(BytesIO(response.content))

    imgRaw = np.array(img)
    #TODO: Define scale from absolute goal res like scale down to max 640x480

    #Resize Image
    resizedImageRaw = resize(imgRaw, 0.1)

    #TODO: use uuid() for unique filenames
    resizedImage = Image.fromarray(resizedImageRaw)
    resizedImage.save(filename)

    #Return image
    with open(filename, 'rb') as f:
        encodeImg = base64.standard_b64encode(f.read())

    os.remove(filename)
    #TODO: delete temporary file
    return { "headers": {"Content-Type":"image/jpg", "statusCode": 200}, "body": str(encodeImg, 'utf-8')}
