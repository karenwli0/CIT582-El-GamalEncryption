from elgamal import *

pk, sk = keygen()
# print(sk)

c = encrypt(pk, 2)
m = decrypt(sk, c)

print(m)
