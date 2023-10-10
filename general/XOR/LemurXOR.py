# D:\CryptoHack_Challenges\general\XOR\flag1.png
# D:\CryptoHack_Challenges\general\XOR\lemur1.png

from PIL import Image;
import numpy as np

#PIL 모듈 사용
flag = Image.open('flag1.png') 
lemur = Image.open('lemur1.png')

#rgb(#, #, #) => 배열 형식 
#사진의 배열 받아오기
flagarr = np.array(flag)
lemurarr = np.array(lemur)

#배열 xor 연산
v = np.bitwise_xor(flagarr, lemurarr)

#np.bitwise_xor의 데이터 타입 확인
print(type(v))

#xor 연산이 된 배열을 이미지로 변환 
flag2 = Image.fromarray(v)
#이미지 출력
flag2.show()


