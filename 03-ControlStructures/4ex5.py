###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''

for char in plain_text:
    # read the character's code (use ord())
    tmp_char=ord(char)
    # add one to the character's code
    tmp_char += 1
    # replace new character code with its
    letter = chr(tmp_char)
    # corresponding character (use chr())
    encrypted_text +=letter
    # add encrypted character to encrypted text
    

print(plain_text)
print(encrypted_text)