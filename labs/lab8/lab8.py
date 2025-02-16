import random
import string

# сгенерировать ключ ascii
def key_hex(n):
    key = ''
    for i in range(n):
        key += random.choice(string.ascii_letters + string.digits) 
    return key

# зашифровать по ключу
def cipher(plain, key):
    new_text = ''
    for i in range(len(plain)): 
        new_text += chr(ord(plain[i]) ^ ord(key[i % len(key)]))
    return new_text

plain1 = 'Neque porro quisquam est qui dolorem' # открытый текст 1
key = key_hex(len(plain1)) # сгенерировать ключ для обоих текстов
cipher1 = cipher(plain1, key) # шифротекст 1
deciphered1 = cipher(cipher1, key) # расшифровать шифротекст 1 по ключу

plain2 = 'Fusce eu venenatis erat. Aliquam sed' # открытый текст 2
cipher2 = cipher(plain2, key) # шифротекст 2
deciphered2 = cipher(cipher2, key) # расшифровать шифротекст 2 по ключу

# человекочитаемый вывод

print('оригинальный текст 1: ', plain1, "\nсгенерированный ключ: ", key, '\nшифротекст: ', cipher1, '\nрасшифровка: ', deciphered1,'\n')
print('оригинальный текст: ', plain2, "\nсгенерированный ключ: ", key, '\nшифротекст: ', cipher2, '\nрасшифровка: ', deciphered2,'\n')

xored = cipher(cipher2, cipher1) # проксорить второй через первый
print('второй по первому: ', cipher(plain1, xored))
print('первый по второму: ', cipher(plain2, xored))
