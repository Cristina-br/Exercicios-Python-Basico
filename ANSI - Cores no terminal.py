"""
Padrão ANSI de Estilo e Cores:

\033[style;text;backgroundm

style:
0 -> none
1 -> bold
4 -> underline
7 -> negative

text:
30 -> branco
31 -> vermelho
32 -> verde
33 -> amarelo
34 -> azul
35 -> roxo
36 -> azul
37 -> ciano

background:
40 -> branco
41 -> vermelho
42 -> verde
43 -> amarelo
44 -> azul
45 -> roxo
46 -> azul
47 -> ciano

\033[m (letra cinza e fundo preto é o padrão)
"""

print("\033[0;30;41mOlá, mundo!\033[m")
print("\033[4;33;44mOlá, mundo!\033[m")
print("\033[35;43mOlá, mundo!\033[m")
print("\033[1;30;42mOlá, mundo!\033[m")
print("\033[mOlá, mundo!")
print("\033[7;30mOlá, mundo!\033[m")
