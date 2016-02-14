
from PIL import Image
import util_methods

# decodes the text out of an image
def decode_text(encoded_image_filename):
    image = Image.open(encoded_image_filename)
    pixels = image.load()
    first_pixel = (0,0)
    second_pixel = next_pixel(first_pixel, image.size)
    third_pixel = next_pixel(second_pixel, image.size)
    message = ""
    while True:
        character = pixels[first_pixel][0] % 2
        character = (character << 1) + (pixels[first_pixel][1] % 2)
        character = (character << 1) + (pixels[first_pixel][2] % 2)

        character = (character << 1) + (pixels[second_pixel][0] % 2)
        character = (character << 1) + (pixels[second_pixel][1] % 2)
        character = (character << 1) + (pixels[second_pixel][2] % 2)

        character = (character << 1) + (pixels[third_pixel][0] % 2)
        character = (character << 1) + (pixels[third_pixel][1] % 2)
        #character = (character << 1) + (pixels[third_pixel][2] % 2)
        #print(chr(character), " ", bin(character))
        first_pixel  = next_pixel(third_pixel,  image.size)
        second_pixel = next_pixel(first_pixel,  image.size)
        third_pixel  = next_pixel(second_pixel, image.size)
        if (character == 0):
            break
        message += chr(character)
    image.close()
    return message



