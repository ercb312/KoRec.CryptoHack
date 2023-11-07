from Crypto.Util.number import getPrime, inverse, GCD
p = getPrime(1024) # 1024 bit prime
q = getPrime(1024) # what’s happening if using nextPrime function..?
n = p * q
e = 65537 # Usually 0x10001
Phi_n = (p-1)*(q-1)
d = inverse(e, Phi_n)
#============================================================================================
M = 123456789101112123123123123123123

def RtoL( x , M , N): # x^M mod N
    r0 = 1
    r1 = x
    for i in range( (len(bin(M)) - 3) , -1 , -1):
        r0 = (r0 * r0) % N
        if((M >> i) & 1 == 1):
            r0 = (r0 * r1) % N
    return r0

