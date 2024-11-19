while True:
    try:
        velocidade = float(input("O seu carro está rodando a quantos Km/h? "))
        if velocidade <= 80:
            print("Tenha uma boa viagem!")
        else:
            print("A velocidade ultrapassou o permitido!")
            print("\033[31mVOCÊ FOI MULTADO!\033[m")
            print(f"Pague uma taxa de R${(velocidade - 80) * 7:.2f}.")
        break
    except ValueError:
        print("Por favor, digite um número válido.")
