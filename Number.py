def main():

    import random

    print("Welcome to Numbers!")

    lives = 7

    fehl = 1

    num = int(random.randint(1, 100))

    while True: 

        number = input("Please enter a Number: ")

        if number.isdigit():
            number = int(number)

            if number == 0:
                print("Please enter a number above 0!")
            elif number > 0:
                print("Thanks!")
                if number == num and lives >= 1:
                    print("You got it right!")
                    break
                elif lives <= 1:
                    print("The Number I was thinking of is", num)
                    print("You thought it was", number)
                    break
                elif lives >= 1 and num >= number:
                    print("The Number I am Thinking of is Higher then the Number you provided!")
                    lives -= fehl
                    print("You got", lives, "Lives left!")
                elif lives >= 1 and num <= number:
                    print("The Number I am Thinking of is Smaller then the Number you provided!")
                    lives -= fehl
                    print("You got", lives, "Lives left!")
        else:
            print("Invalid input, please enter a positive number!")
main()