#16 byte의 16진수(hex)를 입력한다 (ex: 10001000100010001000100010001000)
#위의 16 byte의 hex를 암호화(AES-CBC)한다 
#Dec(a) = IV|C1|C2
# x는 xor연산을 나타낸다
a = "c7193a7c9d1dc6db1f5ac150a14d04597cf17a42a9e3f3e737ffe1fa2144a8d05e74f7c0b44ded003335dcb3eb95c15a"

print(a[:32])
print(a[32:64])
print(a[64:])



#Flag = F1|F2
#IV: c7193a7c9d1dc6db1f5ac150a14d0459
#C1: 7cf17a42a9e3f3e737ffe1fa2144a8d0
#C2: 5e74f7c0b44ded003335dcb3eb95c15a

#FxIV: 
#Enc(F1xIV) = C1:
#Enc(C1xF2) = C2:

#F1 구하기
#Dec(C1) = F1xIV
#(F1xIV)xIV = F1

#F2 구하기
#Dec(C2) = C1xIV
#(C1xIV)xC1 = F2

#F1: 63727970746f7b3363625f3575636b35
#F2: 5f34763031645f31375f21212121217d
#Flag = F1|F2