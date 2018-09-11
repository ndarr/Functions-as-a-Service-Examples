from imageresizer import resize
import imageio
import matplotlib.pyplot as plt
import base64
import os


def main(args):
    # Download Image
    img = imageio.imread(args.imgurl)

    #TODO: Define scale from absolute goal res like scale down to max 640x480

    #Resize Image
    resizedImage = resize(img, 0.1)

    #TODO: use uuid() for unique filenames
    plt.imsave('out.jpg', resizedImage)

    #Return image
    with open('out.jpg', 'rb') as f:
        encodeImg = base64.standard_b64encode(f.read())

    os.remove('out.jpg')
    #TODO: delete temporary file
    return { "headers": {"Content-Type":"image/jpg", "statusCode": 200}, "body": str(encodeImg, 'utf-8')}