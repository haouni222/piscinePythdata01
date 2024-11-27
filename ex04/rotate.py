from load_image import ft_load
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.use('TkAgg')


def shape(tab):
    i = 0
    max = -1
    while i < len(tab):
        if len(tab[i]) > max:
            max = len(tab[i])
        i += 1
    return (len(tab), max)


def transpose(tab):
    data = []
    i = 0
    while i < len(tab[0]):
        data.append([])
        j = 0
        while j < len(tab):
            data[i].append(tab[j][i])
            j += 1
        i += 1
    return data


def rotate_image(img):
    transposed_img = transpose(img)
    a = np.array(transposed_img)
    return a

def ft_zoom(img_path):
    try:
        img = ft_load(img_path)
        if img is None:
            return

        target_height = 400
        target_width = 400
        offset_x = 450
        offset_y = 100
        zoomed_img = img[offset_y:offset_y+target_height, offset_x:offset_x+target_width]
        gray_zoomed_img = zoomed_img[..., 0]
        print(f"the shape of image is: {gray_zoomed_img.shape}")
        print(gray_zoomed_img)

    except Exception as e:
        print(f"An error occurred: {e}")

    return gray_zoomed_img

def ft_display_rotate(img_path):
    try:
        img = ft_zoom(img_path) 
        if img is None:
            return
        
        rotated_img = rotate_image(img)
        
        print(f"New shape after Transpose: {rotated_img.shape}")
        print(rotated_img)
        
        plt.imshow(rotated_img, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")



def main():
    ft_display_rotate('animal.jpeg')

if __name__ == "__main__":
    main()


