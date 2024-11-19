n1 = float(input("Digite um número: "))
n2 = float(input("Digite um segundo número: "))
n3 = float(input("Digite um terceiro número: "))

lista = [n1, n2, n3]
lista_ordenada = sorted(lista)

print(f"O menor número é {lista_ordenada[0]}")
print(f"O maior número é {lista_ordenada[2]}")