addresses = [
    "  пгт. Нижний Куранах. ул. Нижняя, д.12 ",
    "г.Геленджик, Геленджикский проскет, д.34",
    "  г. Рязань, пр. Ленина, д.53 "
]
for i, addr in enumerate(addresses, 1):
    original = addr
    cleaned = addr.strip()
    cleaned = cleaned.replace("г.", "г. ")
    cleaned = cleaned.replace("ул.", "ул. ")
    cleaned = cleaned.replace("д.", "д. ")
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")
    cleaned = cleaned.replace(" ,", ",")
    cleaned = cleaned.replace(",", ", ")
    while "  " in cleaned:
        cleaned = cleaned.replace("  ", " ")
    print(f"#{i}")
    print(f"ДО  : '{original}'")
    print(f"ПОСЛЕ: '{cleaned}'")
    print()
