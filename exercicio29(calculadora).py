num1 = int(input('Digite um Número:'))
num2 = int(input('Digite um Segundo Número:'))
acao = str(input('Escolha uma das Funções (+),(-),(*),(/):'))

print('O resultado é:')

if acao == '+':
    print(num1 + num2)
elif acao == '-':
    print(num1 - num2)
elif acao == '*':
    print(num1 * num2)
elif acao == '/':
    print(num1 / num2)
else:
    print('Ação Inválida!')