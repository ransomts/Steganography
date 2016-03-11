#!/usr/bin/python

import encrypt
import decrypt
import util_methods
import argparse
import sys

# Argument parser to handle the command line arguments in a standard Python format
parser = argparse.ArgumentParser(description=                                   \
    "Store a message in an image file by hiding the message binary in the least \
    significant bits of the pixel color data.")

# Specify either a message or a filename with message in plain text and a filename 
#     of an image to put it in, or a image with a message already in it and an optional 
#     filename to output the message into.
# driver -m "message" -e "image.png"
# driver -ptf "plain_text.txt" -e "image.png"
# driver -d "image.encrypted.png"
parser.add_argument("-pt", "--plain_text",
                    nargs = '?',
                    dest = "plain_text",
                    help = "Plaintext string")
parser.add_argument("-ptf", "--plain_text_file",
                    nargs = '?',
                    dest = "plain_text_file",
                    help = "File containing message")
parser.add_argument("-e", "--encrypt_file",
                    nargs = '?',
                    dest = "encrypt_file",
                    help = "File to encrypt to")
parser.add_argument("-d", "--decrypt_file",
                    nargs = '?',
                    dest = "decrypt_file",
                    help = "File to decrypt")
parser.add_argument("-o", "--decrypted_output",
                    nargs = '?',
                    dest = "decrypted_output",
                    help = \
    "File to print decrypted output to, if not specified, prints to console.")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
args = parser.parse_args()


# Uses the plain text command line argument unless there is a filename specified
message = args.plain_text
if (args.plain_text_file != ""):
    message = read_message_from_file(plain_text_file)

# if there is a message to encode, encode it
if (message != ""):
    encode_text(message, args.encrypt_file)
else:
    # otherwise decrypt the image specified
    message = decode_text(args.decrypt_file)
    # and output the message to the console or to a file
    if args.decrypted_output == "":
        print(message)
    else:
        decrypted_file = open(args.decrypted_output, "w")
        decrypted_file.write(message)
        decrypted_file.close()


