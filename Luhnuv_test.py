"""
Tvým úkolem je vytvořit funkci luhn, která ověří číslo kreditní karty na základě tzv. Luhnova testu.
Luhnův test používají některé bankovní společnosti k rozpoznání platného čísla dané kreditní karty
od náhodně poskládaných číslic.

Ověření pomocí Luhnova testu vypadá následovně:

    Obrátí se pořadí číslic v čísle.

    Vezme se první, třetí...a každá další lichá číslice v tomto obráceném pořadí a sečte do sumy s1.

    Potom se vezme druhé, čtvrté...a každá sudá číslice a: a. Každá číslice se vynásobí dvěma.
    Pokud je číslo získané násobením větší než 9, sečteme jeho číslice. b.
    Sečteme všechny sudé číslici, které prošli násobením a upravením do s2.

    Pokud s1 + s2 končí 0, potom lze původní číslo považovat za platné číslo kreditní karty.

Výstupem programu by měly být hodnoty True nebo False v závislosti na tom,
jestli je dané číslo platební karty platné, nebo ne.
"""
NUM = 61789372994

def digit_sum(num: int) -> int:
    result = 0
    while num:
        result += num % 10
        num //= 10
    return result


# Definice fce
def luhn(num):
    s1 = 0
    s2 = ""
    reversed_num_list = list(str(num)[::-1])
    odd = True
    while reversed_num_list:
        if odd:
            s1 += int(reversed_num_list.pop(0))
        else:
            s2 += str(digit_sum(int(reversed_num_list.pop(0)) * 2))
        odd = not odd

    s2 = digit_sum(int(s2))

    result = True if (s1 + s2) % 10 == 0 else False

    return result


print(luhn(NUM))

# vzorové řešení
def luhn(num):
    # Odstraneni pripadnych mezer
    num_str = str(num).replace(' ','')

    # Promenne pro nacitani sum
    s1 = s2 = 0

    # Prochazeni indexu a cisel pozpatku pomoci stridingu
    for i,num in enumerate(num_str[::-1]):

        # Liche indexy - cisla na lichych pozicich
        if i % 2 == 0:
            s1 += int(num)

        #Sude indexy - cisla na sudych pozicich
        else:
            num = int(num) * 2
            if num > 9:
                num = int(str(num)[0]) + int(str(num)[1])
            s2 += int(num)

    # Overeni souctu s1 + s2
    result = True if (s1 + s2) % 10 == 0 else False

    # Vraceni vysledku
    return result

# Cislo platebni karty
num = 61789372994

# Zavolani fce
print(luhn(num))