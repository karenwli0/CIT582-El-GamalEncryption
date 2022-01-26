from elgamal import *

pk, sk = keygen()
# print(pk, sk)

c = encrypt(pk, 1)
m = decrypt(sk, c)

print(m)
