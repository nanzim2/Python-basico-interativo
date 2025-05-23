print('Bem Vindo!')
print('Sumário \n1 - Variavéis \n2 - soma \n3 - Verificação de variáveis \n4 - Operadores aritméticos \n5 - Calculo média \n6 - Tabuada')
valor = int(input('selecione o número do tema: '))
match valor:
    case 1:
        print('*VARIAVÉIS*')
        resposta = input(
            'Vamos começar! Você quer falar comigo? (s/n) ').lower()
        # lower para primeira letra maiuscula
        if resposta == "s":
            print('Olá, me fale mais sobre você:')
            nome = input('Qual o seu nome? ')
            idade = input('Qual a sua idade? ')
            peso = input('Qual o seu peso? ')
            print(
                f'Prazer em te conhecer {nome}, você tem {idade} anos e {peso} KG')
        else:
            print('Que pena :(')

    case 2:
        print('*SOMA*')
        n1 = int(input('Digite um númuro: '))  # int para número
        n2 = int(input('Digite um número: '))
        s = n1 + n2
        print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))

    case 3:
        print('*VERIFICAÇÃO DE VARIÁVEIS*')
        n = input('Digite algo: ')
        print('Isto é uma ', type(n))
        # se é possivel converter para numero com int()
        print('Converte para número? ', n.isnumeric())

    case 4:
        print('*OPERADORES ARITMÉTICOS*')
        n = int(input('Digite um número: '))
        ante = n - 1
        suce = n + 1
        dobro = n * 2
        triplo = n * 3
        raiz = n ** 0.5
        print('O número escolhido foi: {0} \nSeu antecessor é {1} e seu sucessor é {2} \nO seu dobro é {3} e triplo é {4} \nSua raiz quadrada é {5:.3}'.format(
            n, ante, suce, dobro, triplo, raiz))

    case 5:
        print('*CALCULO MÉDIA*')
        nota1 = int(input('Qual a sua primeira nota? '))
        nota2 = int(input('Qual a sua segunda nota? '))
        media = (nota1 + nota2) / 2
        print('Sua media é {:.3}'.format(media))

    case 6:
        print('*TABUADA*')
        n = int(input('Digite um número:'))
        print(f'{n} * 0 = {n * 0} \n{n} * 1 = {n * 1} \n{n} * 2 = {n * 2} \n{n} * 3 = {n * 3} \n{n} * 4 = {n * 4} \n{n} * 5 = {n * 5} \n{n} * 6 = {n * 6} \n{n} * 7 = {n * 7} \n{n} * 8 = {n * 8} \n{n} * 9 = {n * 9} \n{n} * 10 = {n * 10}')

    case _:
        print("Opção inválida!")
