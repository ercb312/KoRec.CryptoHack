
from Crypto.Util.number import inverse
# C = m**emod(N)
# N = p * q
# pow(base, exponent, modulus)
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

phiN = 882564595536224140639625987657529300394956519977044270821168

e = 65537

# ed = 1 mod(phiN)

# ed % phiN = 1

# a = qd + r 
# q 몫, r 나머지
# a = r mod(d)

a = inverse(e, phiN)
print(a)

