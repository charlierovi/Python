frase = input("Introdueix una frase: ")

vocals = "aeiouAEIOU"

comptador = 0

comptadorconsonants = 0

for lletra in frase:
    if lletra in vocals:
        comptador += 1
    else:
        comptadorconsonants += 1

print(f"La frase conté {comptador} vocals")
print(f"La frase conté {comptadorconsonants} consonants")