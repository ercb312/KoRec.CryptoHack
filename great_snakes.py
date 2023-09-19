#!/usr/bin/env python3

import sys
# import this

if sys.version_info.major == 2:
    print("You are running Python 2, which is no longer supported. Please update to Python 3.")

ords = [81, 64, 75, 66, 70, 93, 73, 72, 1, 92, 109, 2, 84, 109, 66, 75, 70, 90, 2, 92, 79]

print("Here is your flag:")

print("\n")

for _ in ords:
    print(chr(_^0x32), end='')

print("\n")

a = list(map(lambda a: chr(a^0x32), ords))
print(''.join(a))

print("\n")

print("".join(chr(o ^ 0x32) for o in ords))

print("\n")


#0x32 == 16진수로 50표현
#^ == XOR 연산자
#"".join(chr(o ^ 0x32) for o in ords) == list comprehension

#ords == 문자열을 아스키코드로 반환할 수 있는 함수이다. 
#ord(c) 형태로 이용한다. 괄호( ) 안에 문자를 넣으면 
#그 문자에 해당하는 아스키코드를 숫자로 반환한다. 

#ords list와 chr(o ^ 0x32) 연산을 해준다