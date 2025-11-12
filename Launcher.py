import importlib

programs = {
    "1": ("Anagram", "main"),
    "2": ("RomanNumbers", "main"),
    "3": ("Palindrome", "main"),
    "4": ("Number", "main"),
    "5": ("Money", "main"),
    "6": ("Factorial", "main"),
    "7": ("pyramide", "main"),
    "8": ("PrimeNumbers", "main"),
    "9": ("Analyse", "main"),
    "10": ("Ticket", "main"),
}

def menu():
    print("Choose a Program:")
    for k, (mod, _) in programs.items():
        print(f"{k}) {mod}")
    return input("Choosen: ").strip()

def run(choice):
    mod_name, func_name = programs[choice]
    mod = importlib.import_module(mod_name)  # nutzt Dateien wie Anagram.py, RN.py ...
    getattr(mod, func_name)()               # ruft main() auf

if __name__ == "__main__":
    choice = menu()
    if choice in programs:
        run(choice)
    else:
        print("Invalid Choice")