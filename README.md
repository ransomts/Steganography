# Steganography

Hiding information in images is a modern practice of steganography, I've chosen to imlement it with Python.

## Overview
The idea is that the ascii values of the characters that make the message can be written into the least significant bit of the pixels RGB color values. This is a very small change and is near impossible to tell by looking at the picture, particularly for large images.

## TODO

* Test Command Line arguments
  * Help works when given `-h` `--help` or nothing
  * Encrypt text to file with `$./driver.py -pt <string> -e <file>`
  * Decrypt file with `$./driver.py -d <file>`
* Test for large text inputs and image sizes
* Maybe add gui?

