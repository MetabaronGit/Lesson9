import random

WORDS = ["autobus", "buben", "kladivoun"]



def print_hangman(hangman):
    # os.system('cls' if os.name == 'nt' else 'clear')
    for ch in hangman:
        print(ch, end=" ")


def main():
    secret = random.choice(WORDS)
    hangman = list("_" * len(secret))
    counter = 9
    print("Myslím si slovo. Jaké to je?")
    while counter > 0:
        print_hangman(hangman)
        letter = input(f"\nTipni písmeno (počet zbývajících pokusů je {counter}):")
        counter -= 1


main()

