#Table of lenght 1 Million and one 
#isPrime[N] should equal True if N is a prime and false if no

isPrime = [True] * 101
p = 2
while (p * p <= 101):
    if (isPrime[p] == True):
        for i in range(p * p, 101, p):
            isPrime[i] = False
    p += 1    
isPrime[0], isPrime[1] = False, False