def main():

    print("Welcome to Roman Numbers!")

    roman_map = [
        (1000, "M"), (900, "CM"),
        (500, "D"),  (400, "CD"),
        (100, "C"),  (90, "XC"),
        (50, "L"),   (40, "XL"),
        (10, "X"),   (9, "IX"),
        (5, "V"),    (4, "IV"),
        (1, "I")
    ]

    single = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

    def int_to_roman(n: int) -> str:
        if n < 1 or n > 3999:
            raise ValueError("Only numbers in 1..3999 are supported")
        parts = []
        for value, symbol in roman_map:
            if n >= value:
                count = n // value
                parts.append(symbol * count)
                n %= value
            if n == 0:
                break
        return ''.join(parts)

    def roman_to_int(s: str) -> int:
        s = s.strip().upper()
        i = 0
        total = 0
        while i < len(s):
            if i + 1 < len(s):
                pair = s[i:i+2]
                if pair in {"CM","CD","XC","XL","IX","IV"}:
                    total += {"CM":900,"CD":400,"XC":90,"XL":40,"IX":9,"IV":4}[pair]
                    i += 2
                    continue
            ch = s[i]
            if ch not in single:
                raise ValueError("Invalid Roman numeral")
            total += single[ch]
            i += 1
        # Bereich + kanonische Form prüfen
        if total < 1 or total > 3999:
            raise ValueError("Only Roman numerals for 1..3999 are supported")
        if int_to_roman(total) != s:
            raise ValueError("Invalid or non-canonical Roman numeral (1..3999 only)")
        return total

    while True:
        raw = input("Enter a positive integer (1..3999) or a Roman numeral (I..MMMCMXCIX): ").strip()
        if not raw:
            print("Please enter something :(")
            continue
        if raw.isdigit():
            n = int(raw)
            try:
                print("Roman numeral:", int_to_roman(n))
                break
            except ValueError as e:
                print("Error:", e)
                continue
        else:
            try:
                value = roman_to_int(raw)
                print("Integer value:", value)
                break
            except ValueError as e:
                print("Error:", e)
                continue
main()