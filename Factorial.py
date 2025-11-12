def main():
    print("Welcome to Factorial Finder!")

    n = int(input('Factorial of n = '))
    f = 1
    for i in range(1, n + 1):
        f *= i

    print(f'{n}! = {f}')
main()