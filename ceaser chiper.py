#code to write the ceaser chiper encoding and decoding
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
direction = input("Enter 'encode' to encrypt and 'decode'to decript")
def encode(message):
    shift_number = int(input("Enter the shift number"))
    a =""
    for letter in message:
        position=alphabet.index(letter)
        new_position=position+shift_number
        if new_position > 26:
            new_position = new_position -26
            new_message=alphabet[new_position]
            a=a+new_message
        else:
            new_message=alphabet[new_position]
            a = a+new_message
    print("The encrypted message is ", a)



def decode(message):
    shift_number = int(input("Enter the shift number"))
    b = ""
    for letters in message:
        position = alphabet.index(letters)
        new_position=position-shift_number
        if new_position < 0:
            new_position = 26 - new_position
            new_message = alphabet[new_position]
            b = b+new_message
        else:
            new_message = alphabet[new_position] 
            b=b+new_message
    print("The decrypted message is", b)



message = input("Enter the message")
if direction == "encode":
    encode(message)
else:
    decode(message)