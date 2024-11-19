nome_completo = str(input("Qual é o seu nome completo? ")).strip().split()

print("Muito prazer em te conhecer!")
print(f"O seu primeiro nome é: {nome_completo[0]}")
print(f"O seu último nome é: {nome_completo[len(nome_completo)-1]}")