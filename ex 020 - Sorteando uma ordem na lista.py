from random import sample

lista_alunos = []


def add_alunos_lista ():
    while True:
        novo_aluno = input("Digite o nome de um aluno para adicioná-lo à lista ou 'sair' para sair: ")
        if novo_aluno.lower() == "sair":
            break
        else:
            lista_alunos.append(novo_aluno)
    return lista_alunos


print("=" * 30)
print("Sorteando uma ordem de alunos na lista")
print("=" * 30)

while True:
    print("\nMenu:")
    print("1 - Para adicionar alunos na lista")
    print("2 - Para ver a lista de alunos")
    print("3 - Para sortear uma ordem de alunos na lista")
    print("4 - Para sair do programa")
    opcao = int(input("Escolha um número do Menu: "))
    if opcao == 1:
        add_alunos_lista()
    elif opcao == 2:
        while True:
            if len(lista_alunos) == 0:
                print("Não há alunos na lista")
                add_alunos_lista()
            else:
                print(f"Os seguintes alunos estão na sua lista: {lista_alunos}")
                break
    elif opcao == 3:
        while True:
            if len(lista_alunos) == 0:
                print("Não há alunos na lista")
                add_alunos_lista()
            else:
                print(f"A ordem sorteada foi {sample(lista_alunos, len(lista_alunos))}")
                break
    elif opcao == 4:
        print("Saindo do programa")
        break