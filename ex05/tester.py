from load_image import ft_load
from pimp_image import ft_invert, ft_red, ft_green, ft_blue, ft_grey
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from load_image import ft_load
matplotlib.use('TkAgg')

array = ft_load("landscape.jpg")
invert = ft_invert(array)
#red = ft_red(array)
#green = ft_green(array)
#blue = ft_blue(array)
#grey = ft_grey(array)
#print(ft_invert.__doc__)

plt.figure(figsize=(15, 10))
plt.imshow(grey)
plt.show()