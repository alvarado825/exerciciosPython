
from random import randint
import time

def ex_1():
    
    valor = input('Digite um texto: ')
    caracteres_especiais = ['!','@','#','$','%','&','*','_']
    novo_valor = ''

    for caractere in valor:
        novo_valor+= caractere if not caractere in caracteres_especiais else ''

    print(novo_valor)

def ex_2():

    valor = input('Digite um texto: ')
    novo_valor = ''

    for caractere in valor:
        novo_valor += caractere if caractere.isnumeric() else ''

    print(novo_valor)

def ex_3():
    
    valor = input('Digite sua idade: ')
    
    if valor.isnumeric() and int(valor) >= 0:
        mensagem = 'Maior de idade' if int(valor) >= 18 else 'Menor de idade'
        print(mensagem)
    else:
        print('Digite um Número Válido')

def ex_4():
    
    valor = input('Digite um texto: ')
    vezes = int(input('Digite o numero de vezes que o texto deve ser escrito: '))

    print((valor +'\n') * vezes)

def ex_5():
    a = input('Digite um valor para A: ')
    b = input('Digite um valor para B: ')

    print(f'Valor de A é : {a} - Valor de B é : {b}')

    a = a+ '-' +b
    b,a = a.split('-')

    print()
    print(f'Valor de A agora é: {a} - e o Valor de B agora é: {b}')

    '''
    a = a+b
    b = a[:len(a) - len(b)]
    a = a[len(b):]
    
    ou

    a = a+b
    b = a.replace(b,"") 
    a = a.replace(b,"")
    
    '''
    
def ex_6():

    filmes = []
    
    while(1):
        filme = input('Digite um Filme, ou digite "ok" para fazer o sorteio: ').title()
        if filme == 'Ok':
            break
        else:
            filmes.append(filme)
            
    sorteio = randint(0, len(filmes))
    print(f'O filme sorteado foi: {filmes[sorteio -1]}')
    print()

if __name__ == '__main__':
    
    cont = 0
    while(True):
        input('Pressione Enter para voltar ao menu principal') if cont > 0 else ''
        try:
            cont = 1
            print()
            opcao = int(input('1 Fazer um programa pra remover os caracteres especiais do valor que o usuário digitar\n2 Fazer um programa pra remover letras e deixe apenas os numeros que o usuário digitar\n3 Fazer um programa que o usuário digite a idade e o programa diga se ele é maior ou menor de idade\n4 Fazer um programa que o usuário digite um texto e o programa escreva o texto quantas vezes o usuário quiser,\n5 Fazer um programa com as variaveis "a" e "b" e trocar entre elas sem declarar mais nenhuma variavel\n6 Fazer um programa que o usuário digite o nome de varios filmes (quantos ele quiser) e o programa sorteie um dos filmes pra ele assistir\n\nEscolha uma opção: '))
        except Exception as e:
            print()
            print('Digite um número')
            cont = 0
            continue

        if  opcao < 1 or opcao > 6:
            print()            
            print('Escolha uma opção de 1 a 6')
            
        else:
            if opcao == 1:
                ex_1()
            elif opcao == 2:
                ex_2()
            elif opcao == 3:
                ex_3()
            elif opcao == 4:
                ex_4()
            elif opcao == 5:
                ex_5()
            elif opcao == 6:
                ex_6()
            
                    
                
                
                
            
