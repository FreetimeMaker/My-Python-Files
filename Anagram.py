def main ():

    print("Welcome to Anagram Finder!")

    while True:
        text1 = input("Please enter your text! The Text will be checked: ").lower().strip()
        text2 = input("Please enter another Text: ").lower().strip()

        if sorted(text1) == sorted(text2):
            print("Your words", text1, "and", text2, "are an anagram!")
        else:
            print("Your words", text1, "and", text2, "are not an anagram!")
        break
main()