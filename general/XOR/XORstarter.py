from pwn import *



#label -> converting each character to the integer representing the Unicode character
#13 -> converting the integer from decimal to binary
c = 'label'
a = [ord(z) for z in 'label']

string = []

for b in a: 
    d = (b^13) 
    # print(d)
    e = chr(d)
    string.append(e)

string = "".join(string)
print(string)



#a = 13
#b = 'label'
#c = xor(a, b)
#print(c)