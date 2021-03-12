def rozdel_na_slova(text) -> list:
  return text.lower().split()


def vycisti_text(jednotliva_slova: list) -> list:
  cista_slova = []
  for word in jednotliva_slova:
      cista_slova.append(word.strip(" ,.!`\":_'?"))
  return cista_slova


def soucet_jednotlivych_slov(cista_slova: list) -> dict:
  vyskyt_slov = dict()
  while cista_slova:
      word = cista_slova.pop()
      vyskyt_slov[word] = vyskyt_slov.get(word, 0) + 1
  return vyskyt_slov

def main() -> None:
    # vstupni_text = input("Zadej text: ")
    vstupni_text = "Ahoj' hugo, máme  doma prase.? ahoj"

    vstupni_text = rozdel_na_slova(vstupni_text)
    vstupni_text = vycisti_text(vstupni_text)
    vstupni_text = soucet_jednotlivych_slov(vstupni_text)

    print(vstupni_text)


main()