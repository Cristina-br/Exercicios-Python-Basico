frase = str(input("Digite uma frase: ")).strip().lower()

print(f"Essa frase tem {frase.count("a")} letras A.")
print(f"A primeira letra A aparece na posição {frase.find("a")+1}.")
print(f"A última letra A aparece na posição {frase.rfind("a")+1}")