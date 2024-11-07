from math import sin, cos, tan, radians

angulo = float(input("Digite o ângulo que você deseja: "))
angulo_convertido = radians(angulo)

seno = sin(angulo_convertido)
cosseno = cos(angulo_convertido)
tangente = tan(angulo_convertido)

print(f"O ângulo de {angulo} tem o SENO de {seno:.2f}")
print(f"O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")
print(f"O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")