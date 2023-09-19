#map
a = list(range(20)) 
# a 나누기 3의 나머지 값이 a mod3 (= a%3)
def b(a):
    return a%3

c = list(map(lambda b : b%3,a))
print(c)


#byte type으로 저장하기
a = b'asdasdasd'
print(a.hex())
a.hex()
print(bytes.fromhex(a.hex))
print(type(a.hex()))

b = 'asdasdasd'



#zip
#numbers = [1, 2, 3]
#letters = ["A", "B", "C"]
#for pair in zip(numbers, letters):
