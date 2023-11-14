#!/usr/bin/python3
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import signal

def timeout(a1, a2):
    print("BYE ~")
    exit(-1)


class InSecureCipher:
    def __init__(self, key):
        self.size = 16
        assert len(key) == self.size
        self.key = key
        self.cipher = AES.new(key, 1)

    def encrypt(self, pt):
        return self.cipher.encrypt(pad(pt, self.size))

    def decrypt(self, ct):
        assert len(ct) % self.size == 0
        return unpad(self.cipher.decrypt(ct), self.size)


def main():

    ISC = InSecureCipher(os.urandom(16))
    secret = os.urandom(64)
    enc_secret = ISC.encrypt(secret)

    print(f"Encrypted secret : {enc_secret.hex()}")
    token = 4
    print(f'You have only 4 tokens to use my oracle.')

    for i in range(token):
        menu = input("inp > ")
        if menu == 'enc':
            pt = bytes.fromhex(input('pt(hex) > '))
            print(ISC.encrypt(pt).hex())
        elif menu == 'dec':
            ct = bytes.fromhex(input('ct(hex) > '))
            if ct == enc_secret:
                print("No. you cant do that.")
            else:
                print(ISC.decrypt(ct).hex())
        
        elif menu == 'secret':
            sec = bytes.fromhex(input('secret(hex) > '))
            if sec == secret:
                print("Congratulation!")
                exit(0)
            else:
                print("who are you?")
                exit(-1)
        else:
            print('Unexpected input')
            exit(-1)


if __name__ == "__main__":
    main()
