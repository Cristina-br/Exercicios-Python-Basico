import random

print("=" * 30)
print("Sorteando um aluno da lista")
print("=" * 30)
print("Menu:")

lista_alunos = []


def add_alunos_lista (lista_alunos):
    while True:
        novo_aluno = input("Digite o nome do aluno ou digite 'sair' para ver outras opções: ")
        if novo_aluno.lower() == "sair":
            break
        else:
            lista_alunos.append(novo_aluno)
    return lista_alunos


while True:
    opção = int(input("1 - Para adicionar alunos na lista\n2 - Para ver a lista de alunos\n3 - Para sortear um aluno da lista\n4 - Para sair do programa\nEscolha uma opção: "))
    if opção == 1:
        add_alunos_lista(lista_alunos)
    elif opção == 2:
        print(lista_alunos)
    elif opção == 3:
        print(f"O aluno sorteado foi {random.choice(lista_alunos)}")
    elif opção ==4:
        print("Saindo do programa")
        break
    else:
        print("Escolha uma opção válida:")