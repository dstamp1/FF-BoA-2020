#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

N = 600851475143


def is_prime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

factors = []
for i in range(1,N):
    if i > N/2:
        break
    elif is_prime(i):
        if N % i == 0:
            factors.append(i)
    else:
        pass

print(factors)
print(factors[-1])
