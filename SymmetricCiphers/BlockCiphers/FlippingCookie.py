from Crypto.Util.number import bytes_to_long, long_to_bytes
# Get_Cookie() = 739af852fe4c8a96ba8af35c0643fc4d792d1c1a5417ea9a607a40f715a2c04d7c3f760ddd6795740fd175d03b2cbbde
# Get_Cookie() = iv | C1 | C2
a = "739af852fe4c8a96ba8af35c0643fc4d792d1c1a5417ea9a607a40f715a2c04d7c3f760ddd6795740fd175d03b2cbbde"
print(a[:32]) # iv
print(a[32:64]) # C1
print(a[64:]) # C2

iv = 0x739af852fe4c8a96ba8af35c0643fc4d
C1 = "792d1c1a5417ea9a607a40f715a2c04d"
C2 = "7c3f760ddd6795740fd175d03b2cbbde"

#여기서 x 는 xor 연산을 의미
# C1 = Enc(P1 X iv)
# C2 = Enc(P2 x C1)

#XOR Tool 을 이용하여  P1, P2를 구하자
P1 = 0x61646d696e3d46616c73653b65787069
P2_ = "05126a1789707fee6fab35272e8e7b93"
P2 = "05126a1789707fee6fab3527"

# Cookie = C1 | C2

#  padded = pad(cookie, 16)
MAL = bytes_to_long("admin=True;:))))".encode())
print(hex(MAL^P1^iv))
#7c3f760ddd6795740fd175d03b2cbbde

# iv x P1 x MAL = 05126a1789707fee6fab35272e8e7b93
# iv x P1 = 792d1c1a5417ea9a607a40f715a2c04d



