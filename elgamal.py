import random

from params import p
from params import g

q = (p - 1) / 2


def keygen():
    a = random.randint(1, q)
    sk = a
    pk = pow(g, a, p)
    return pk, sk


def encrypt(pk, m):
    r = random.randint(1, q)
    c1 = pow(g, r, p)
    # c2 = (pow(pk, r) * m) % p
    c2 = pow(pow(pk, r, p) * m, 1, p)
    return [c1, c2]


def decrypt(sk, c):
    c1, c2 = c
    m = pow(c2 / pow(c1, sk), 1, p)
    return m
