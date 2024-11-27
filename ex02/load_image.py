import matplotlib.image as mpimg


def ft_load(path: str):
    """ load une image et verifie si c'est un jpg/jpeg
      et si c'est une image RGB, return l'image
      print la shape de l'image"""

    try:
        img = mpimg.imread(path)

        if img is None:
            raise FileNotFoundError

        if not path.lower().endswith(('.jpg', '.jpeg')):
            raise ValueError("Not a jpg/jpeg file")

        if img.ndim != 3 or img.shape[2] != 3:
            raise ValueError("Not an RGB image")

        height, width, _ = img.shape
        print("The shape of this image is : ("
              + str(height) + ", " + str(width) + ", " + str(img.ndim) + ")")

    except FileNotFoundError:
        print("File not found")
        exit(1)
    except Exception as e:
        print(e)
        exit(1)

    return img
