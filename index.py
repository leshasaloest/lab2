import random
from aes128 import AES as AES_128
from aes192 import AES as AES_192
from aes256 import AES as AES_256


def change_random_bit(data):
    byte_string = bytearray(data, "utf-8")
    barray = []
    for byte in byte_string:
        barray.append(byte)
    hex_string = ''.join(format(x, '02x') for x in barray)
    values = [int(digit, 16) for digit in hex_string]
    digitindex = random.randint(0, len(hex_string)-1)
    values[digitindex] ^= 1
    return bytes.fromhex("".join("0123456789abcdef"[val] for val in values))


msg = 'Two One Nine Two'
encode = '__all__'
print('AES 128')
key = 'Thats my Kung Fu'    # 16 character / 128 bits
encrypt_128 = AES_128()
x = encrypt_128.encrypt(key, msg, encode)
y = encrypt_128.decrypt(key, x['hex'])
sum = 0
for i in range (1000):
    changed_msg = change_random_bit(msg).decode("utf-8")
    a = encrypt_128.encrypt(key, changed_msg, '0b')
    compared_bits = int(x['0b'], 2) ^ int(a, 2)
    for digit in bin(compared_bits)[2:].zfill(len(a)):
        sum += int(digit)
sum1 = 0
for i in range (1000):
    changed_key = change_random_bit(key).decode("utf-8")
    a = encrypt_128.encrypt(changed_key, msg, '0b')
    compared_bits = int(x['0b'], 2) ^ int(a, 2)
    for digit in bin(compared_bits)[2:].zfill(len(a)):
        sum1 += int(digit)
print(x['hex'])
print(sum/1000, "в середньому (серед 1000 випадкових випробувань) бiт криптотексту змiнюється при змiнi одного бiта "
                "вiдкритого тексту")
print(sum1/1000, "в середньому (серед 1000 випадкових випробувань) бiт криптотексту змiнюється при змiнi одного бiта "
                "ключа")
print(y, end='\n\n')


print('AES 192')
key = 'Thats my Kung Fu Panda !'    # 24 character / 192 bits
encrypt_192 = AES_192()
x = encrypt_192.encrypt(key, msg, encode)
y = encrypt_192.decrypt(key, x['hex'])
sum = 0
for i in range (1000):
    changed_msg = change_random_bit(msg).decode("utf-8")
    a = encrypt_192.encrypt(key, changed_msg, '0b')
    compared_bits = int(x['0b'], 2) ^ int(a, 2)
    for digit in bin(compared_bits)[2:].zfill(len(a)):
        sum += int(digit)
sum1 = 0
for i in range (1000):
    changed_key = change_random_bit(key).decode("utf-8")
    a = encrypt_192.encrypt(changed_key, msg, '0b')
    compared_bits = int(x['0b'], 2) ^ int(a, 2)
    for digit in bin(compared_bits)[2:].zfill(len(a)):
        sum1 += int(digit)
print(x['hex'])
print(sum/1000, "в середньому (серед 1000 випадкових випробувань) бiт криптотексту змiнюється при змiнi одного бiта "
                "вiдкритого тексту")
print(sum1/1000, "в середньому (серед 1000 випадкових випробувань) бiт криптотексту змiнюється при змiнi одного бiта "
                "ключа")
print(y, end='\n\n')


print('AES 256')
key = 'Thats my Kung Fu Panda ! Style12'    # 32 character / 256 bits
encrypt_256 = AES_256()
x = encrypt_256.encrypt(key, msg, encode)
y = encrypt_256.decrypt(key, x['hex'])
sum = 0
for i in range (1000):
    changed_msg = change_random_bit(msg).decode("utf-8")
    a = encrypt_256.encrypt(key, changed_msg, '0b')
    compared_bits = int(x['0b'], 2) ^ int(a, 2)
    for digit in bin(compared_bits)[2:].zfill(len(a)):
        sum += int(digit)
sum1 = 0
for i in range (1000):
    changed_key = change_random_bit(key).decode("utf-8")
    a = encrypt_256.encrypt(changed_key, msg, '0b')
    compared_bits = int(x['0b'], 2) ^ int(a, 2)
    for digit in bin(compared_bits)[2:].zfill(len(a)):
        sum1 += int(digit)
print(x['hex'])
print(sum/1000, "в середньому (серед 1000 випадкових випробувань) бiт криптотексту змiнюється при змiнi одного бiта "
                "вiдкритого тексту")
print(sum1/1000, "в середньому (серед 1000 випадкових випробувань) бiт криптотексту змiнюється при змiнi одного бiта "
                "ключа")
print(y, end='\n\n')