from pwn import *

#label -> converting each character to the integer representing the Unicode character
#13 -> converting the integer from decimal to binary
a = [ord(z) for z in 'label']

string = []

# ^ == xor 연산자
for b in a: 
    #label의 알파벳 하나씩 13과 xor 연산
    d = (b^13) 

    #xor된 ascii 값
    #print(d)

    #ascii 값을 문자로 바꿔준다
    e = chr(d)
    string.append(e)

#밑줄 생략
string = "".join(string)
print(string)


#pwntools 사용해서 푸는 방법
#a = 13
#b = 'label'
#c = xor(a, b)
#print(c)