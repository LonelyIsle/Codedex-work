import imageio.v3 as iio

filenames = ['images/nyan-cat1.png','images/nyan-cat2.png','images/nyan-cat3.png']
images = []

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('Nyan-Cat.gif', images, duration = 500, loop = 0)