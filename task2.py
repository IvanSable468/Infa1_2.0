def is_prime(x):
    result = (x == 2 or x % 2 != 0)
    if result:
        for i in range(3, int(x**0.5), 2):
            if x % i == 0:
                return False

    return result
num = int(input())
print(is_prime(num))