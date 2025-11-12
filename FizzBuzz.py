def main():
    print("Welcome to FizzBuzz!")

    while True:
        number = input("Please enter a number: ").strip()

        if number.isdigit():
            number = int(number)

            if number <= 0:
                print("Please enter a number above 0!")
            else:
                result = []  # Liste für die Ausgabe

                for i in range(1, number + 1):
                    if i % 3 == 0 and i % 5 == 0:
                        result.append("FizzBuzz")
                    elif i % 3 == 0:
                        result.append("Fizz")
                    elif i % 5 == 0:
                        result.append("Buzz")
                    else:
                        result.append(str(i))

                # Ausgabe als kommagetrennte Liste
                print(", ".join(result))

                # Letzte Zahl mit Divisor-Infos
                if number % 3 == 0 and number % 5 == 0:
                    print(f"{number} = FizzBuzz (divisible by 3 and 5)")
                    print(f"{number} / 3 = {number // 3}")
                    print(f"{number} / 5 = {number // 5}")
                elif number % 3 == 0:
                    print(f"{number} = Fizz (divisible by 3)")
                    print(f"{number} / 3 = {number // 3}")
                elif number % 5 == 0:
                    print(f"{number} = Buzz (divisible by 5)")
                    print(f"{number} / 5 = {number // 5}")
                else:
                    print(f"{number} = {number} (not divisible by 3 or 5)")
                break
        else:
            print("Invalid input, please enter a positive number!")
main()