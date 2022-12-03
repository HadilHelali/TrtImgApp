import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def showImage(imgname):
    img = mpimg.imread(imgname)
    imgplot = plt.imshow(img, cmap='gray')
    plt.show()
    return plt