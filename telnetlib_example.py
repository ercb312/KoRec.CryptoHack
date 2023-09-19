#!/usr/bin/env python3

import telnetlib
import json

HOST = "socket.cryptohack.org"
PORT = 11112

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")

def json_recv()-> dict: #받는 argument가 없음
    line = readline() #스트링 받아서 line에 저장
    line = line.decode() #line을 decode하고 딕셔너리로 바꿔준다
    return json.loads(line) 

def json_send(hsh:dict):
    request = json.dumps(hsh).encode() #hsh(딕셔너리)를 json으로 보내기 위헤 처리 = 스트링(문자열)으로 바꿔줌
    tn.write(request) #telenet으로 스트링(문자열) request를 보냄


print(readline())
print(readline())
print(readline())
print(readline())


request = {
    "buy": "flag" #파이썬 딕셔너리 개념 활용 #dic = {Key1:Value1} #"buy": "flag" 하면 flag가 나옴
}
json_send(request)

response = json_recv() #response에 json.loads(line.decode())가 return됨

print(response)

