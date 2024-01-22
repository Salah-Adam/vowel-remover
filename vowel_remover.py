def remover_vowels(text):
    vowels = "aeuoi"
    consnents = ""
    for char in text:
        if char.lower() not in vowels:
            consnents += char
    return consnents

print(remover_vowels("Good mornIng"))