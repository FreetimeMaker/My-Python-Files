def main():

    print("Welcome to Palindrome Finder!")

    while True:
        text = input("Please enter your text! The Text will be checked: ").lower().strip()
        if text == text[::-1]:
            print(text, "is a palindrome")
            break
        else:
            print(text, "is not a palindrome")
main()