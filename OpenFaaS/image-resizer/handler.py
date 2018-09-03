from scipy import misc
import numpy
import imageio
import file

def resize(image, scale):
    # Define new picture
    if scale >= 1.0:
        return

    maxX = int(scale * len(image))
    maxY = int(scale * len(image[0]))
    sizedImage = numpy.ndarray(shape=(maxX, maxY, 3))
    recScale = 1 / scale
    for i in range(maxX):
        oldX = int(recScale * i)
        for k in range(maxY):
            oldY = int(recScale * k + (oldX % scale))
            sizedImage[i][k] = image[oldX][oldY]
    return sizedImage

def handle(req):
    """handle a request to the function
    Args:
        req (str): Url to image
    """
    #Download Image
    img = imageio.imread(req)

    f = file()
    resizedImage = resize(img, 0.5)

    imageio.imwrite()
    return resizedImage

