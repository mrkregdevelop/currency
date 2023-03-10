"""
A

Taras
['T', 'a', 'r', 'a', 's']
[84, 97, 114, 97, 115] + 1
[85, 98, 115, 98, 116]
['U', 'b', 's', 'b', 't']
Ubsbt

A -|||> B

B

Ubsbt
['U', 'b', 's', 'b', 't']
[85, 98, 115, 98, 116] - 1
[84, 97, 114, 97, 115]
['T', 'a', 'r', 'a', 's']
Taras

"""
KEY = 2


def encrypt(message: str) -> str:
    encrypted_message = ''
    for char in message:
        encrypted_message += chr(ord(char) + KEY)

    return encrypted_message


def decrypt(message: str) -> str:
    encrypted_message = ''
    for char in message:
        encrypted_message += chr(ord(char) - KEY)

    return encrypted_message
