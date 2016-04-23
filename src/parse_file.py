
from PIL import Image
from util_methods import *
import os

encode_file_number = 0

def get_file_bytes(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        for c in data:
            print(bin(ord(c)))
    return data

def prompt_next_file():
    filename = askopenfile()
    if filename != None and filename != '':
        return filename
    showinfo('Error', 'Invalid filename')

    if not os.path.isdir('encrypted'):
        os.mkdir('encrypted')

def number_of_pixels_in_image(image):
    return image.size[0] * image.size[1]

def parse_image_helper(pixels, message):
    hex_tuple = (0,0)
    num_pixels = number_of_pixels_in_image(image)
    
    for i in range(0, num_pixels)[::3]:
        # pull out the bits to insert
        data_to_insert = int(data[i:i+3], 2)
        data_tuple = ()
        data_tuple += (data_to_insert % 2,)
        data_tuple += ((data_to_insert>>1) % 2,)
        data_tuple += ((data_to_insert>>2) % 2,)
        
        # insert the bits into the pixel data of the image
        
        # increment the index tuple
        hex_tuple = next_pixel(hex_tuple)

        pixels[hex_tuple] = place_bits(pixels[hex_tuple], data_tuple)

        # if the next index is off the file, get a new file
        # 14 pixels for the token 
        if (hex_tuple[0] * len(pixels[0]) + hex_tuple[1]) > (num_pixels - 14):
            pixels = insert_middle_token(pixels)
            image.save(image.filename.replace('.', '.encoded.'))
            return [filename] + parse_image_helper(pixels, data[i:])
        else:
            image.save(image.filename.replace('.', '.encoded.'))
            return [filename]


def put_message_in_file(encode_image_filename, message):

    image = Image.open(encode_image_filename)
    pixels = image.load()
    hex_tuple = (0,0)
    data = message #get_file_bytes(message_filename)
    num_pixels = number_of_pixels_in_image(image)
    
    for i in range(0, num_pixels)[::3]:
        
        # pull out the bits to insert
        data_to_insert = int(data[i:i+3], 2)
        data_tuple  = ()
        data_tuple += (data_to_insert % 2,)
        data_tuple += ((data_to_insert>>1) % 2,)
        data_tuple += ((data_to_insert>>2) % 2,)
        
        # insert the bits into the pixel data of the image
        pixels[hex_tuple] = place_bits(pixels[hex_tuple], data_tuple)
        
        # increment the index tuple
        if (next_pixel(hex_tuple)):
            hex_tuple = next_pixel(hex_tuple)
        else:
            return "Ran out of pixels"
    return "Success"

def put_first_token_in_file(pixels, encode_file_number):
    if encode_file_number == 0:
        print('-|-')
    else:
        print(str(encode_image_filename) + '~|~' + str(encode_image_filename + 1))

def put_second_token_in_file(pixels, encode_file_number):
    if message == '':
        print('_|_')
    else:
        print(str(encode_file_number) + '~|~' + str(encode_file_number+1))
    return
            

def put_message_and_tokens_in_file(pixels, message):
    pixels = put_first_token_in_file(pixels, encode_filename_number)
    # message is substring that is the max amount of data we
    # can put in image with the two tokens
    
    pixels = put_message_in_file(pixels, message)
    # if there is any of the message left, get a new file and put the message in it
    # otherwise, put in the end token '_|_'
    pixels = put_second_token_in_file(pixels, encode_filename_number)


def parse_message(encode_image_filename, message_filename, encode_file_number):

    image = Image.open(encode_image_filename)
    pixels = image.load()

    message = get_file_bytes(message_filename)

    total_num_bits = number_of_pixels_in_image(image) * 3
    bits_in_message = len(message) * 8
    # TODO: calculate the amount of the message that can fit in the image
    # both tokens need a total of 28 pixels, so the message needs to fill the rest
    messgae_len = len(message)
    
    bits_that_fit_in_file = num_pixels * 3
    
    put_message_and_tokens_in_file(pixels, message)

        # if the next index is off the file, get a new file
        # 14 pixels for the token
    if (hex_tuple[0] * len(pixels[0]) + hex_tuple[1]) > (num_pixels - 14):
        pixels = insert_middle_token(pixels)
        image.save(image.filename.replace('.', '.encoded.'))
        # maybe put in a +3?                                     \/
        return [filename] + parse_image(prompt_next_file(), data[i:])
    else:
        image.save(image.filename.replace('.', '.encoded.'))
        return [filename]
