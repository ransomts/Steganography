# Steganography

Hiding information in images is a modern practice of steganography, I've chosen to imlement it with Python.

## Overview
The idea is that the ascii values of the characters that make the message can be written into the least significant bit of the pixels RGB color values. This is a very small change and is near impossible to tell by looking at the picture, particularly for large images.

## TODO

* Test Command Line arguments
  * ~~Help works when given `-h` `--help` or nothing~~
  * ~~Encrypt text to file with `-pt <string> -e <file>`~~
  * ~~Decrypt file with `-d <file>`~~
  * ~~Encryption takes file contents with `-ptf <plain_text_file> -e <file>`~~
  * ~~Decryption outputs to file with `-d <encrypted_image_file> -o <output_file>`~~
* Test for ~~large text inputs~~ and image sizes
* GUI
  * Align objects (images, info label)
  * Resizable objects (images, buttons, ~~text area~~)
  * Dynamically change images
  * Hook into actual running code
  * Finish menubar items 
    * File
      * open image to decode
      * decode image
      * encode image
    * Quit
      * help
      * about (include info about what's going on)
  * Add accelerators to menubar items