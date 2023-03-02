import math
import time
import pandas as pd
import matplotlib.pyplot as plt


def find_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    primes = [2, 3, 5, 7]
    with open("Primes_Bank.txt", "w") as f:
        f.write("Few Known Primes are :- ")
        for p in primes:
            f.write(str(p))
            f.write("\n")
    n = 11
    start_time = time.time()
    i = 1
    with open("Primes_Bank.txt", "a") as f:
        f.write("Now more complex primes are :- ")
        f.write("\n")
    while time.time() - start_time < 60000:

        if (n % 10) in [2, 4, 5, 6, 8]:
            n += 1
            continue
        if find_prime(n):
            with open("Primes_Bank.txt", "a") as f:
                f.write(str(i) + " : : " + str(n) + ": DT: " + str(time.time() - start_time) + " ms")
                f.write("\n")
                i += 1

            with open("Plot_Primes.txt", "a") as f:
                f.write(str(n)+","+str(time.time() - start_time))
                f.write("\n")
        n += 1
    plot_graph()


def plot_graph():
    file = pd.read_csv("Plot_Primes.txt", sep=",", header=None)
    file = pd.DataFrame(file)
    x = file[0]
    y = file[1]
    plt.xlabel("Prime Numbers")
    plt.title("Question 4")
    plt.ylabel("Discovery Time ms/n")
    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
