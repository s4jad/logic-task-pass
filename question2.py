
# function to find prime numbers up to a given number
def prime_numbers(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)
prime_numbers(100)