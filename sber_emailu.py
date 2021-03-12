# posbírání emailů z textu
my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
nunc ultricies. Duis facilisis ultrices lacus, id
tiger123@email.cz auctor massa molestie at. Nunc tristique
fringilla congue. Donec ante diam cnn@info.com, dapibus
lacinia vulputate vitae, ullamcorper in justo. Maecenas
massa purus, ultricies a dictum ut, dapibus vitae massa.
Cras abc@gmail.com vel libero felis. In augue elit, porttitor
nec molestie quis, auctor a quam. Quisque b2b@money.fr
pretium dolor et tempor feugiat. Morbi libero lectus,
porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
Pellentesque id dui viverra, auctor enim ut, fringilla est.
Maecenas gravida turpis nec ultrices aliquet.
'''


def get_emails(text: str) -> list:
    result = []
    words = text.split()
    for word in words:
        if "@" in word:
            result.append(word.strip(".,!?:\""))
    return result


def is_any_digit(text: str) -> bool:
    for ch in text:
        if ch.isdecimal():
            return True
    return False


def get_num_emails(emails: list) -> list:
    result = []
    for email in emails:
        if is_any_digit(email):
            result.append(email)
    return result

def get_domains(emails: list) -> list:
    result = []
    for email in emails:
        result.append(email[email.index("@") + 1:])
    return result

def main():
    result = dict()
    email_list = get_emails(my_str)
    emails_with_nums = get_num_emails(email_list)
    domains = get_domains(email_list)
    result = {"domains": domains, "emails_with_nums": emails_with_nums}
    print(result)
    return result

main()
# ---------------------------------------------------------------------
# vzorové řešení
# ---------------------------------------------------------------------

# Funkce pro posbirani emailu ze stringu
def collect_emails(text):
    words = text.split()
    emails = []

    for word in words:
        if '@' in word:
            email = word.strip(".,:!?")
            emails.append(email)

    return emails


# Funkce pro extrahovani emailu obsahujici cisla
def select_num_emails(emails):
    num_mails = []

    for email in emails:
        if contains_number(email):
            num_mails.append(email)

    return num_mails


def contains_number(string):
    for num in range(10):
        if str(num) in string:
            return True
    return False


# Funkce pro extrahovani domen vsech emailu
def extract_domains(emails):
    domains = []
    for email in emails:
        domains.append(email.split('@')[-1])
    return domains


def main():
    result = {
        'emails_with_nums': None,
        'domains': None
    }

    emails = collect_emails(my_str)

    result['emails_with_nums'] = select_num_emails(emails)
    result['domains'] = extract_domains(emails)

    print(result)
    return result


main()

