from dataclasses import replace
from mailbox import NoSuchMailboxError
from os.path import split

nome = input("Escreva seu nome completo: ")

print("Analisando seu nome...")
print(f"Seu nome em minúsculas: {nome.lower()}")
print(f"Seu nome em maiúsculas: {nome.upper()}")

nome_sem_espaco = nome.replace(" ", "")
num_letras_nome = len(nome_sem_espaco)
primeiro_nome = nome.split()[0]
num_letras_primeiro_nome = len(primeiro_nome)

print(f"Seu nome tem {num_letras_nome} letras")
print(f"Seu primeiro nome tem {num_letras_primeiro_nome} letras")