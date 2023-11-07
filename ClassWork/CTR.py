#@/usr/bin/env python3

from Crypto.Cipher import AES
from Crypto.Util import Counter
import os

KEY = os.urandom(16)

def encrypt(plaintext):
    cipher = AES.new(KEY, AES.MODE_CTR, counter=Counter.new(128))
    ciphertext = cipher.encrypt(plaintext)
    return ciphertext.hex()

thug_life = b"Yeah Beyonce Perfect And Rihanna too Kanye's a genius And Drake's so cool All the Kardashian's China and Caitlyn too I want to be famous gonna be famous Just like you"
print(encrypt(thug_life))

with open('flag.txt', 'rb') as f:
    flag = f.read().strip()

print(encrypt(flag))

#result
#32573d4b4282e0d37b0347cead9b85d4c72def2293c408e65fe49851b05bb12e965997592c95f36862817439edad63bfe2f480243a78bb2d735424f562fc4a61ac72832f8260ebe283157761084d238399b70eaf9d8c43fd4b962e3f78f25291fe432c21a13917f7ebd273fff7dff18b23de21c231eb49495fc065dbc396c153236a1f262b7f476bcd75d28e8bc14ed0f476ac4c6fe7b733ad41287a505e13a2df9bd0dc33b0
#2071086519b4edc347326dd8d2a195d5d517cd09d1e001eb31f89857b66a9c27d3488a69798eef
