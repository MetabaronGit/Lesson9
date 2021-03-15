import random

WORDS = ["autobus", "buben", "kladivoun", "mamba"]


def print_hangman(hangman):
    # os.system('cls' if os.name == 'nt' else 'clear')
    for ch in hangman:
        print(ch, end=" ")
    print()


def get_letter(counter):
    return input(f"\nTipni písmeno (počet zbývajících pokusů je {counter}):").upper()


def replace_letters(letter, secret, hangman):
    char_counter = 0
    for i, char in enumerate(secret):
        if letter == char:
            hangman[i] = letter
            char_counter += 1
    if letter in secret:
        print(f"Ano, písmeno \"{letter.upper()}\" je v mém slově {char_counter}x.")
        return True
    else:
        print(f"Ne, písmeno \"{letter.upper()}\" v mém slově není.")
        return False


def is_game_continue(try_counter, hangman):
    return try_counter and "_" in hangman


def main():
    secret = random.choice(WORDS).upper()
    hangman = list("_" * len(secret))
    try_counter = 5
    print("Myslím si slovo. Jaké to je?")
    print_hangman(hangman)

    while is_game_continue(try_counter, hangman):
        letter = get_letter(try_counter)
        if not replace_letters(letter, secret, hangman):
            try_counter -= 1
        print_hangman(hangman)

    # final result
    if "_" in hangman:
        print("Došly ti pokusy. Neuhodl jsi! Moje slovo bylo:", secret)
    else:
        print("Výborně, uhodl jsi! Moje slovo je", secret + ".")

main()

