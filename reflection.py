"""
File: reflection.py
----------------
Take an image. Generate a new image with twice the height. The top half
of the image is the same as the original. The bottom half is the mirror
reflection of the top half.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


def make_reflected(filename):
    image = SimpleImage(filename)
    original_width = image.width
    original_height = image.height
    reflection = SimpleImage.blank(original_width, original_height*2)
    for x in range(original_width):
        for y in range(original_height):
            pixel = image.get_pixel(x, y)
            reflection.set_pixel(x, y, pixel)
            reflection.set_pixel(x, (original_height*2) - (y + 1), pixel)
    return reflection


def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original = SimpleImage('images/mt-rainier.jpg')
    original.show()
    reflected = make_reflected('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
