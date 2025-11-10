print("Welcome to Prime Numbers!")

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

while True:
    number = input("Please enter a number: ").strip()

    if number.isdigit():
        number = int(number)

        if number <= 0:
            print("Please enter a number above 0!")
        else:
            primes_up_to_n = [str(i) for i in range(2, number + 1) if is_prime(i)]
            print(", ".join(primes_up_to_n) if primes_up_to_n else "None")
            break
    else:
        print("Invalid input, please enter a positive number.")