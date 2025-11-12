def extras(TicketPrice, ticketamount, FilmName):
    prices = {
        "popcorn": 5,
        "water": 3,
        "cola": 5,
        "icetea": 7,
        "sprite": 9,
        "fanta": 11,
    }

    popcorn_total = 0
    popcorn_choice = input("Do you want Popcorn? 1 Popcorn costs 5 CHF/Swiss Franks! (Y/N): ").strip()
    if popcorn_choice in ["Y", "Yes", "y", "yes"]:
        popcorn_amount = input("How many Popcorn do you want: ").strip()
        if popcorn_amount.isdigit():
            popcorn_amount = int(popcorn_amount)
            if popcorn_amount >= 1:
                popcorn_total = prices["popcorn"] * popcorn_amount
            else:
                print("Invalid input, please enter a positive number!")

    drink_total = 0
    drink_choice = input("Do you want to drink something during the Film? (Y/N): ").strip()
    if drink_choice in ["Y", "Yes", "y", "yes"]:
        drink_menu = (
            "Available drinks:\n"
            " 1) Water (3 CHF)\n"
            " 2) Cola (5 CHF)\n"
            " 3) IceTea (7 CHF)\n"
            " 4) Sprite (9 CHF)\n"
            " 5) Fanta (11 CHF)\n"
        )
        mapping = {
            "1": "water",
            "2": "cola",
            "3": "icetea",
            "4": "sprite",
            "5": "fanta",
            "water": "water",
            "cola": "cola",
            "icetea": "icetea",
            "ice tea": "icetea",
            "sprite": "sprite",
            "fanta": "fanta",
        }
        while True:
            print(drink_menu)
            drink_select = input("Please enter the drink name or number: ").strip().lower()
            drink_key = mapping.get(drink_select)
            if not drink_key:
                print("Unknown drink selection.")
            else:
                drink_amount = input(f"How many {drink_key.title()} do you want: ").strip()
                if drink_amount.isdigit():
                    drink_amount = int(drink_amount)
                    if drink_amount >= 1:
                        drink_total += prices[drink_key] * drink_amount
                    else:
                        print("Invalid input, please enter a positive number!")
                else:
                    print("Invalid input, please enter a positive number!")
            more = input("Do you want another drink? (Y/N): ").strip()
            if more not in ["Y", "Yes", "y", "yes"]:
                break

    total = TicketPrice * ticketamount + popcorn_total + drink_total
    print("You have chosen", FilmName, "for", ticketamount, "People.", end=" ")
    if popcorn_total:
        print(f"Popcorn total: {popcorn_total} CHF.", end=" ")
    if drink_total:
        print(f"Drinks total: {drink_total} CHF.", end=" ")
    print("Your Total is:", total)

def tickets(TicketPrice, FilmName):
    prompt = f"How many People are watching the Film {FilmName}? 1 Ticket costs {TicketPrice} CHF/Swiss Franks: "
    ticketamount = input(prompt).strip()
    if not ticketamount.isdigit():
        print("Invalid input, please enter a positive number!")
        return None
    ticketamount = int(ticketamount)
    if ticketamount == 0:
        print("Please enter a number above 0!")
        return None
    if ticketamount < 0:
        print("Invalid input, please enter a positive number!")
        return None
    return ticketamount

def main():
    print("Welcome to the Freetime Cinema! What Film would you like to see? There are currently only the Films: K-Pop Demon Hunters (1), Fast and Furious 7 (2) and Transporter 3 (3) available!")

    while True:

        film = input("Please enter your Film Number! The Film Number will be the Film you want to watch in the Freetime Cinema: ").strip()

        TicketPrice = 12

        if film.isdigit():
            film = int(film)

            if film == 0:
                print("Please enter a number above 0!")
            elif film == 1:
                answer = input("Do you want to watch the Film: K-Pop Demon Hunters? Y/Yes/y/yes or N/No/n/no: ").strip()
                if answer in ["Y", "Yes", "y", "yes"]:
                    ticketamount = tickets(TicketPrice, "K-Pop Demon Hunters")
                    if ticketamount is None:
                        continue
                    extras(TicketPrice, ticketamount, "K-Pop Demon Hunters")
                    break
                if answer in ["N", "No", "n", "no"]:
                    continue
            elif film == 2:
                answer = input("Do you want to watch the Film: Fast and Furious 7? Y/Yes/y/yes or N/No/n/no: ").strip()
                if answer in ["Y", "Yes", "y", "yes"]:
                    ticketamount = tickets(TicketPrice, "Fast and Furious 7")
                    if ticketamount is None:
                        continue
                    extras(TicketPrice, ticketamount, "Fast and Furious 7")
                    break
                if answer in ["N", "No", "n", "no"]:
                    continue
            elif film == 3:
                answer = input("Do you want to watch the Film: Transporter 3? Y/Yes/y/yes or N/No/n/no: ").strip()
                if answer in ["Y", "Yes", "y", "yes"]:
                    ticketamount = tickets(TicketPrice, "Transporter 3")
                    if ticketamount is None:
                        continue
                    extras(TicketPrice, ticketamount, "Transporter 3")
                    break
                if answer in ["N", "No", "n", "no"]:
                    continue
        else:
            print("Invalid input, please enter a positive number!")
main()