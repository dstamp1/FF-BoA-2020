
accumulator = 1
for i in range(1,10):
    a = 2*i+1
    c = int((a**2+1)/2)
    accumulator += a
    b = accumulator
    print(a,b,c)
