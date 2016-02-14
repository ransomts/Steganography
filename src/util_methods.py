# Increment to the next logical index
def next_pixel(current_pixel, dim):
    test_location = (current_pixel[0]+1, current_pixel[1])
    if (test_location[0] >= dim[0]):
        test_location = (test_location[0]%dim[0], test_location[1]+1)
    # I really don't like this...    
    if test_location[1] > dim[1]:
        return False
    return test_location

# spits out the nth binary bit of a char
def nth_bit(character, n):
    return (ord(character) >> (7-n))  % 2

def print_bits(character):
    print(character , end = " : ")
    for i in range(8):
        print(nth_bit(character, i), end=" ")
    print()

# Puts the new bits in the least significant place of the tuple values
def place_bits(current_pixel, new_bits):
    current_pixel = list(current_pixel)
    for i in range(0, 3):
        if (new_bits[i] == 1):
            current_pixel[i] = current_pixel[i] | 1
        else:
            current_pixel[i] = current_pixel[i] & -2
    return tuple(current_pixel)

# Returns a string with the contents of a file in it
def read_message_from_file(filename):
    with open(filename, "r") as file:
        message = file.read()
    file.close()
    return message

