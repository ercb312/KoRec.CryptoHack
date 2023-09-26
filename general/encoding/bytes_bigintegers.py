from Crypto.Util.number import *

a = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
#long 은 정수형 데이터 타입 그러므로 따옴표로 묶으면 안 됨
print(long_to_bytes(a).decode())

print(bytes.fromhex(hex(a)[2:]).decode())