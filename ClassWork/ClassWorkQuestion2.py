import math

def is_prime(n):
    # 6k+1 method
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def trial_division(n):
    # Trial division method
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    if len(factors) == 0:
        print(str(n) + " is prime.")
    else:
        print(str(n) + " is not prime. Factors: " + str(factors))

student_number = 200433162
append_numbers = [1, 3, 7, 9]

for num in append_numbers:
    new_number = int(str(student_number) + str(num))
    print("Checking primality of " + str(new_number) + ":")
    if is_prime(new_number):
        print("- 6k+1 method: " + str(new_number) + " is prime.")
    else:
        print("- 6k+1 method: " + str(new_number) + " is not prime.")
    trial_division(new_number)