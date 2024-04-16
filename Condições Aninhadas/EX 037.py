num = int(input('Digite um número inteiro: '))
print('''Escolha um das bases para conversão:
[ 1 ] converter para binário
[ 2 ] converter para octal
[ 3 ] converter para HEXADECIMAL''')
opção = int(input('Sua opção:'))
if opção == 1:
    print(f'{num} convertido para binário é {bin(num)}')
elif opção == 2:
    print(f'{num} convertido para octal é {oct(num)}')
elif opção == 3:
    print(f'{num} convertido para hex é {hex(num)}')
else:
    print('Opção inválida, tente novamente')