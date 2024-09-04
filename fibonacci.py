def fibonacci(n):
    sequencia = [0, 1]  # Inicia a lista com os dois primeiros números de Fibonacci

    for i in range(2, n):
        proximo_num = sequencia[-1] + sequencia[-2]  # Soma os dois últimos números da lista
        sequencia.append(proximo_num)  # Adiciona o próximo número à sequência

    return sequencia


def verifica_fibonacci(n):
    sequencia = fibonacci(1000)  # Gera a sequência de Fibonacci com uma quantidade grande de números

    if n in sequencia:
        print(f"O número {n} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {n} não pertence à sequência de Fibonacci.")


num_informado = int(input("Digite um número e descubra se ele pertence à sequência de Fibonacci: "))

verifica_fibonacci(num_informado)
