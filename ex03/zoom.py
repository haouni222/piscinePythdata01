import matplotlib
import matplotlib.pyplot as plt
from load_image import ft_load
matplotlib.use('TkAgg')


def ft_display_zoom(img_path):
    try:
        img = ft_load(img_path)
        if img is None:
            return
        print(img)
        target_height = 400
        target_width = 400
        offset_x = 450
        offset_y = 100
        zoomed_img = img[offset_y:offset_y+target_height, offset_x:offset_x+target_width]
                        
        gray_zoomed_img = zoomed_img[..., 0]  

        print(f"New shape after slicing: {gray_zoomed_img.shape}")
        plt.imshow(gray_zoomed_img, cmap='gray')
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")

ft_display_zoom('animal.jpeg')
