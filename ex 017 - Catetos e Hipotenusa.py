from math import hypot

c_oposto = float(input("Digite o valor do cateto oposto: "))
c_adjacente = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = hypot(c_oposto, c_adjacente)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")