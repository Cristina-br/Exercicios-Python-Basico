def validar_moeda(moeda):
    moedas_validas = ["dólares", "dolares", "dólar", "dolar", "euros", "euro", "ienes", "iene"]
    return moeda.lower() in moedas_validas


def conversor_moedas(real, moeda_escolhida):
    if moeda_escolhida.lower() in ["dólares", "dolares", "dólar", "dolar"]:
        return real / 5.63
    elif moeda_escolhida.lower() in ["euros", "euro"]:
        return real / 6.22
    elif moeda_escolhida.lower() in ["ienes", "iene"]:
        return real / 0.039


dinheiro_em_carteira = 0
moeda_escolhida = ""

while True:
    try:
        dinheiro_em_carteira = float(input("Quanto dinheiro você tem na carteira? R$"))
        if dinheiro_em_carteira <=0:
            print("Digite um valor positivo para o dinheiro em carteira.")
            continue
        moeda_escolhida = input("Você gostaria de comprar dólares, euros ou ienes? ")
        if validar_moeda(moeda_escolhida):
            break
        else:
            print("Moeda inválida. Por favor, escolha uma das opções: dólares, euros ou ienes. ")
    except ValueError:
        print("Digite um valor numérico válido para o dinheiro em carteira.")

valor_convertido = conversor_moedas(dinheiro_em_carteira, moeda_escolhida)

print(f"Com {dinheiro_em_carteira:.2f} reais você pode comprar {valor_convertido:.2f} {moeda_escolhida}.")
