
from PIL import Image
from util_methods import *

def encode_text(plain_text, image_filename, output_filename=None):

    image = Image.open(image_filename)
    # puts the image into an array format
    pixels = image.load()
    # current pixels to dick with
    first_hex_tuple  = (0,0)
    second_hex_tuple = next_pixel(first_hex_tuple, image.size)
    third_hex_tuple  = next_pixel(second_hex_tuple, image.size)
    if plain_text[len(plain_text) - 1] != '\0':
        plain_text += '\0'
    # write in the characters of the plain_text
    for c in plain_text:
        # pulls out the bits to put in the image pixels
        # the first and last digits are zero because ascii
        # characters only need seven bits [0x02, 0xF7]
        new_bits_pixel_1 = (0, nth_bit(c, 1), nth_bit(c, 2))
        new_bits_pixel_2 = (nth_bit(c, 3), nth_bit(c, 4), nth_bit(c, 5))
        new_bits_pixel_3 = (nth_bit(c, 6), nth_bit(c, 7), 0)

        # pulls out the current pixel data out to manipulate
        current_pixel_data_1 = pixels[ first_hex_tuple]
        current_pixel_data_2 = pixels[second_hex_tuple]
        current_pixel_data_3 = pixels[ third_hex_tuple]

        # puts the least significant bits in place
        new_pixel_data_1 = place_bits(current_pixel_data_1, new_bits_pixel_1)
        new_pixel_data_2 = place_bits(current_pixel_data_2, new_bits_pixel_2)
        new_pixel_data_3 = place_bits(current_pixel_data_3, new_bits_pixel_3)

        # places the new data in the image array
        pixels[ first_hex_tuple] = new_pixel_data_1
        pixels[second_hex_tuple] = new_pixel_data_2
        pixels[ third_hex_tuple] = new_pixel_data_3

        # move the three pixels forward to load in next character
        first_hex_tuple  = next_pixel( third_hex_tuple, image.size)
        second_hex_tuple = next_pixel( first_hex_tuple, image.size)
        third_hex_tuple  = next_pixel(second_hex_tuple, image.size)

    # writes the new image as encoded
    if (output_filename == None):
        output_filename = image.filename.replace(".", ".encoded.")
    else:
        output_filename = image_filename

    #image.save(image.filename)
    image.save(output_filename)
    image.close()
    
    return output_filename
