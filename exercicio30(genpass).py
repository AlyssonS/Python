import random

baixo = "abcdefghijklmnopqrstuvwxyz"
medio = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = "0123456789"
sim = '[]{}()*:/,._-'

todos = baixo + medio + num + sim
tamanho = 16
senha = "".join(random.sample(todos, tamanho))

print(senha)

