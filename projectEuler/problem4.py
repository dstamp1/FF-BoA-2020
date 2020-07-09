# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def is_palindromic(number):
    num_str = str(number)
    reversed_str = num_str[-1::-1]
    return num_str == reversed_str

print(is_palindromic(1001))

palindromic = []
for i in range(100,1000):
    for j in range(100,1000):
        product = i*j
        if is_palindromic(product):
            palindromic.append(product)

print(palindromic)
print(max(palindromic))
