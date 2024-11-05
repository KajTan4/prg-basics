###
# Functions to read any data type from the keyboard
#
def input_string(message):
    x = input(message)
    return str(x)

def input_integer(message):
    x = input(message)
    return int(x)

def input_real(message):
    x = input(message)
    return float(x) 

def input_boolean(message):
    x = input(message)
    if x == 'y':
        return True
    elif x == 'n':
        return False
    