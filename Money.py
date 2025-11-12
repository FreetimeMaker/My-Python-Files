def main():

    print("Welcome to Money Change with numbers!")

    FiveFr = 500

    TwoFr = 200

    OneFr = 100

    FiftyRp = 50

    TwentyRp = 20

    TenRp = 10

    FiveRp = 5

    # Zahleneingabe wiederholen bis gültig
    while True:
        number = input("Please enter the Number that will be the Change Money: ").strip()

        if number.isdigit():
            number = int(number)

            if number == 0:
                print("Please enter a number above 0!")
            elif number > 0:
                print("You entered:", number)
                print("Your Change Money is:")

                rest = number

                if rest >= FiveFr:
                    count = rest // FiveFr
                    print("Five Fr:", count)
                    rest = rest % FiveFr
                if rest >= TwoFr:
                    count = rest // TwoFr
                    print("Two Fr:", count)
                    rest = rest % TwoFr
                if rest >= OneFr:
                    count = rest // OneFr
                    print("One Fr:", count)
                    rest = rest % OneFr
                if rest >= FiftyRp:
                    count = rest // FiftyRp
                    print("Fifty Rp:", count)
                    rest = rest % FiftyRp
                if rest >= TwentyRp:
                    count = rest // TwentyRp
                    print("Twenty Rp:", count)
                    rest = rest % TwentyRp
                if rest >= TenRp:
                    count = rest // TenRp
                    print("Ten Rp:", count)
                    rest = rest % TenRp
                if rest >= FiveRp:
                    count = rest // FiveRp
                    print("Five Rp:", count)
                    rest = rest % FiveRp
                if rest > 0:
                    print("Restamount, That cannot be changed:", rest, "Rp")
                else:
                    print("All Changed!")
                print("The Change is Completed. Thank you so much!")
                break
        else:
            print("Invalid input, please enter a positive number!")
main()