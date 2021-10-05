# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
# com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata
# de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar
# o tempo que falta ou que passou do prazo.
import datetime
ano = int(input('Qual o seu ano de nascimento: '))
hoje = datetime.date.today().year
idade = (hoje - ano)

if idade == 18:
    print('É o momento exato para se alistar')
elif idade > 18:
    print('Já se passou {} anos do  tempo do alistamento'.format(idade - 18))
elif idade < 18:
    print('Ainda faltam {} anos para o seu alistamento'.format(18 - idade))
