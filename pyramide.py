print("Welcome to build a pyramid with numbers!")

# Zahleneingabe wiederholen bis gültig
while True:
    number = input("Please enter your number! The number will be the height of the pyramid: ").strip()

    if number.isdigit():
        number = int(number)

        if number == 0:
            print("Please enter a number above 0!")
        elif number > 0:
            print("You got it! You entered:", number)
            break   # gültige Zahl -> Schleife verlassen
    else:
        print("Invalid input, please enter a positive number.")

# Ja/Nein-Abfrage wiederholen bis gültig
while True:
    answer = input("Do you want the pyramid? (o/O = Outlined, f/F = Filled, h/H = Halfed): ").strip()

    if answer in ["o", "O"]:
        # Outline pyramid
        for i in range(1, number + 1):
            spaces = " " * (number - i)
            if i == 1:
                print(spaces + "#")
            elif i == number:
                print("#" * (2 * i - 1))
            else:
                middle = " " * (2 * i - 3)
                print(spaces + "#" + middle + "#")
        break

    elif answer in ["f", "F"]:
        adder = 1
        # Filled pyramid
        for i in range(0, number + 1):
            spaces = " " * (number - i)
            hashes = "#" * (adder)
            print(spaces + hashes)
            adder += 2
        break

    elif answer in ["h", "H"]:
        for i in range(1, number + 1):
            spaces = " " * (number - i)
            hashes = "#" * i
            print(spaces + hashes + " " + hashes)
        break

    else:
        print("Invalid input, please only enter o/O or f/F or h/H.")
