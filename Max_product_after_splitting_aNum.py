n = int(input())

if n == 2:
    print(1)
elif n == 3:
    print(2)
else:
    product = 1

    while n > 4:
        product *= 3
        n -= 3

    product *= n

    print(product)
