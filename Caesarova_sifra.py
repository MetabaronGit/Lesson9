CHARS = "abcdefghijklmnopqrstuvwxyz"

message = 'abc def ghi jkl mno pqr stu vwx Yz'

def caesar(text, key):
    result = ""

    for char in text:
        if char == " ":
            result += char
        else:
            index = CHARS.index(char.lower())
            shifted_char = CHARS[(index + key) % len(CHARS)]
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
    return result

print(caesar(message, -2))

# vzorove řešení
# --------------------------------------------------------
# Definice fce caesar
def caesar(message, offset):
    # Abeceda
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Vysledna zprava
    encrypted=[]

    # For loop pro zpravu
    for char in message:

        # Pokud znak neni v abecede, nahrajeme ho jen tak
        if char.lower() not in alphabet:
            encrypted.append(char)
            continue

        # Zjisteni pozice pismene
        position = alphabet.index(char.lower())

        # Novy index pismene
        index = (position+offset) % len(alphabet)

        # Ziskani noveho pismene
        if char.isupper():
            new_char = alphabet[index].upper()
        else:
            new_char = alphabet[index]

        # Nahrani do vysledne zpravy
        encrypted.append(new_char)

    # Vraceni zpravy jako stringu
    return ''.join(encrypted)
# Zprava
message = 'abc def ghi jkl mno pqr stu vwx Yz'
# Zavolani fce
print(caesar(message,-2))