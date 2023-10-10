# D:\CryptoHack_Challenges\general\XOR\flag1.png
# D:\CryptoHack_Challenges\general\XOR\lemur1.png

from PIL import Image;
import numpy as np
from pwn import *


flag = Image.open('flag1.png')
lemur = Image.open('lemur1.png')

flagarr = np.array(flag)
lemurarr = np.array(lemur)

v = np.bitwise_xor(flagarr, lemurarr)

# print(type(v))

flag2 = Image.fromarray(v)
flag2.show()


