from math import gcd

def get_primitive_roots(modulo):
    coprime_set = { num for num in range(1, modulo) if gcd(num, modulo) == 1 }
    return [g for g in range(1, modulo) if coprime_set == {pow(g, powers, modulo)
            for powers in range(1, modulo)}]

