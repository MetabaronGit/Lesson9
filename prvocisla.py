# algoritmus Eratosthenova síta

def list_primes(max_num: int) -> list:
    result = []
    if max_num > 1:
        work_list = list(range(2, max_num + 1))

        while work_list:
            multiplier = work_list.pop(0)
            result.append(multiplier)

            for i in work_list:
                if i % multiplier == 0:
                    work_list.pop(work_list.index(i))
    return result

def is_prime(number: int) -> bool:
    work_list = list_primes(number + 1)
    return number in work_list

print(list_primes(10))
print(is_prime(7))

# vzorove řešení
# Definice fce is_prime
def is_prime(n):
    # Vraceni boolean hodnoty
    return n in list_primes(n)


# Definice fce list_primes
def list_primes(n):

    # Vygenerovani listu k projiti
    nums = list(range(2,n+1))

    # Pomocna promenna pro ukladani prvocisel
    result = set()

    # While loop pro prochazeni listu
    while nums:

        # Prvocislo
        i = nums.pop(0)

        # Pridani prvocislo do vysledku
        result.add(i)

        # For loop pro odstraneni nasobku prvocisla
        for num in nums:
            if num % i==0:
                nums.remove(num)

    # Vraceni vysledku
    return result

# Volani fce is_prime
print(is_prime(23))

# Volani list_primes
print(list_primes(100))