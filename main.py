from numbers.prime_generator import get_prime
from numbers.primitive_root import get_primitive_roots


def main():
     
    # Both persons agrees on public keys Gs and Ps
    # Prime number P
    Ps = get_prime(12)
     
    # Gs is primitive root for Ps
    Gs = get_primitive_roots(Ps)
    if len(Gs) > 0: 
        Gs = Gs[len(Gs) - 1]
    else:
        print("Error In Generation Of Primitive root ..!!")
        return 
     
      
    print('Value of Ps is : ', Ps)
    print('Value of Gs is : ', Gs)
     
    # g is the private key chosen by Joy
    g = 4
    print('Private Key g is: %d'%(g))
     
    # fetches the generated key
    p = int(pow(Gs,g,Ps)) 
     
    # h will be the chosen private key by Happy
    h = 3
    print('Private Key h is : %d'%(h))
    
    # fetches the generated key
    q = int(pow(Gs,h,Ps)) 
     
     
    # Joy's Secret key
    K_A = int(pow(q,g,Ps))
     
    #  Happy's Secret key
    K_B = int(pow(p,h,Ps))
     
    print('Joy\'s Secret key is : %d'%(K_A))
    print('Happy\'s Secret key is : %d'%(K_B))


if __name__ == '__main__':
    main()