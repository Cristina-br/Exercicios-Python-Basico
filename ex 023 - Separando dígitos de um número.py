n = input("Digite um número inteiro de 0 a 9999: ")


def validar_n(num):
    while True:
        try:
            num = int(num)
            if num >= 0 and num <= 9999:
                break
            else:
                num = int(input("Você digitou um número inválido. Digite um número inteiro de 0 a 9999: "))
        except ValueError:
            num = input("Entrada inválida. Digite um número inteirosdvh de 0 a 9999: ")
    return num


num_validado = validar_n(n)
num_validado_str = f"{num_validado:04d}"

print(f"Analisando o número {num_validado}")
print(f"Unidade: {num_validado_str[3]}")
print(f"Dezena: {num_validado_str[2]}")
print(f"Centena: {num_validado_str[1]}")
print(f"Milhar: {num_validado_str[0]}")