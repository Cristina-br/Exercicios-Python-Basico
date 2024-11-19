while True:
    try:
        n = int(input("Digite um número inteiro: "))
        if n % 2 == 0:
            print(f"O número {n} é PAR")
            break
        else:
            print(f"O número {n} é ÍMPAR")
            break
    except ValueError:
        print("Digite um número válido.")
