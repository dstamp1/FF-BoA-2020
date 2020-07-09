product = 1
for i in range(1,20):
    product *= i
print(product)


for i in range(1,product):
    remainders = [i % j for j in range(1,20)]
    if sum(remainders) == 0:
        print(i)
        break   
