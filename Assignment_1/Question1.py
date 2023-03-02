import math

primes = [1, 3, 7, 9]
studentID = "200483287"


def six_k_plus_one(number):
    # this is the 6k+1 method
    if number <= 3:
        return number > 1
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def trial_division(number):
    # trial division method
    factors = []
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.append(i)
            factors.append(number // i)
    if len(factors) == 0:
        print("Using Trial Division " + str(number) + " is prime.")
    else:
        print("Using Trial Division " + str(number) + " is not prime. Factors are: " + str(factors))


for number in primes:
    test_for_prime = studentID + str(number)
    if six_k_plus_one(int(test_for_prime)):
        print("Using 6k+-1 " + str(test_for_prime), "is not a prime number")
    else:
        print("Using 6k+-1  " + str(test_for_prime), "is a prime number!")

    trial_division(int(test_for_prime))

print("done")

# Execution Logs
# Using 6k+-1 2004832871 is not a prime number
# Using Trial Division 2004832871 is prime.
# Using 6k+-1 2004832873 is not a prime number
# Using Trial Division 2004832873 is prime.
# Using 6k+-1  2004832877 is a prime number!
# Using Trial Division 2004832877 is not prime. Factors are: [22721, 88237]
# Using 6k+-1  2004832879 is a prime number!
# Using Trial Division 2004832879 is not prime. Factors are: [7, 286404697, 83, 24154613, 581, 3450659]
