from datetime import date

nascimento = int(input('Seu ano de nascimento: '))
data = date.today().year
idade = data - nascimento

if idade > 18:
    print(f'Já se passaram {idade - 18} anos, venha até a unidade RIB PRETO.')
elif idade == 18:
    print('É hora de se alistar, vá até o posto mais próximo')
elif idade < 18:
    print(f'Ainda faltam {18 - idade} anos, é cedo demais... ')
else:
    print('Por favor, digite novamente o seu ano de nascimento.')