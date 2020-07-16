"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for row in range(N_ROWS):
        for col in range(N_COLS):
            patch = make_recolored_patch(random.uniform(0, 2), random.uniform(0, 2), random.uniform(0, 2))
            add_patch(final_image, row, col, patch)
    final_image.show()

def add_patch(image, row, column, patch):
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            pixel = patch.get_pixel(x, y)
            image.set_pixel(x+(column*PATCH_SIZE), y+(row*PATCH_SIZE), pixel)


def make_recolored_patch(red_scale, green_scale, blue_scale):
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

if __name__ == '__main__':
    main()