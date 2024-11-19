def validar_distancia():
    while True:
        try:
            distancia = float(input("Digite a distância da viagem em Km para saber o preço da passagem: "))
            if distancia == float(distancia):
                break
        except ValueError:
            print("Digite um número válido.")
    return distancia


km = validar_distancia()

if km <= 200:
    print(f"A passagem para uma viagem de {km:.2f}Km custará R${km * 0.5:.2f}")
else:
    print(f"A passagem para uma viagem de {km:.2f}Km custará R${km * 0.45:.2f}")


