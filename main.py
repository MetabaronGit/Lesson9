def main() -> None:
    """Hlavni ridici funkce moji kalkulacky"""
    UVODNI_ZPRAVA = "Vitejte v nasi kalkulacce"
    ODDELOVAC = f"\n{'=' * 50}\n"
    pozdrav_uzivatele(UVODNI_ZPRAVA, ODDELOVAC)
    while (operator := zvol_operator()) != "exit":
        if operator in ("+", "-"):
            x1, x2 = zvol_cisla().replace(" ","").split(",")
            print(f"vysledek: {zpracovani_vypoctu(x1, x2, operator)}",
                  end=ODDELOVAC)
        else:
            print("Tento operator tu neni")

    else:
        print("Ukoncuji kalkulacku")
        quit()


def pozdrav_uzivatele(uvod: str, oddelovac: str) -> None:
    print(f"{uvod}".center(50), end=oddelovac)

def vypis_nabidku(oddelovac: str, *args) -> None:
    print(f"{' | '.join(args)}".center(50), end=oddelovac)


def zvol_operator() -> str:
    return input("Vyber matematickou opereci: ")

def zvol_cisla() -> str:
    return input("Zadej dve cisla a oddel je carkou: ")

def zpracovani_vypoctu(x1: str, x2: str, op: str) -> float:
    return {
        "+": float(x1) + float(x2),
        "-": float(x1) - float(x2)
        }.get(op)

main()