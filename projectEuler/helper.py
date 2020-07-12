def fibonaci(number):
    return fibonaci_list(number)[number]

def fibonaci_list(number):
    fib_list = []
    fib_list.append(1)
    fib_list.append(1)
    for i in range(2,number+1):
        next_term = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_term)

    return fib_list

def get_primes(n):
    numbers = set(range(n, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p*2, n+1, p)))
    return primes

print(triangular_list(10))
