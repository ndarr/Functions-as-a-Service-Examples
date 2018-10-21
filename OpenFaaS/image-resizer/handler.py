import json
from imageresizer import resize
import imageio
import matplotlib.pyplot as plt
import sys

def handle(req):
    """handle a request to the function
    Args:
        req (str): Url to image
    """

    url = json.loads(req)['imgurl']
    # Download Image
    img = imageio.imread(url)

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




img_url = "https://s3.eu-central-1.amazonaws.com/faas-evaluation/testimage.png"
handle('{"imgurl":"'+img_url +'"}')