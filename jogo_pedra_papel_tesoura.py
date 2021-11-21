'''Jogo:

pedra papel tesoura
'''
import random
import placar

print('Welcome to rock-paper-scissors Game')


def main() -> None:
    game()


def game():
    acao = int(input('Digite 1 para escolher pedra, 2 para papel, ou, 3 para tesoura: '))
    contra = random.randint(1, 3)

    dict = {1: 'pedra', 2: 'papel', 3: 'tesoura'}

    print(f'Você escolheu: {dict[acao]}')
    print(f'O seu oponente escolheu: {dict[contra]}')

    if acao == 1 and contra == 1 or acao == 2 and contra == 2 or acao == 3 and contra == 3:
        print('Vocês empataram!')
        placar.emp += 1
        resp = input('Deseja jogar mais uma partida? (s/n)')

        if resp == 's':
            game()
        else:
            print(f'Placar: \n\nVitorias: {placar.vit}, \nEmpates: {placar.emp}, \nDerrotas: {placar.der}')
            print('\nFIM DE JOGO')

    elif acao == 1 and contra == 2 or acao == 2 and contra == 3 or acao == 3 and contra == 1:
        print('Você perdeu!')
        placar.der += 1
        print('Deseja jogar mais uma partida? (s/n)')
        resp = input(' ')

        if resp == 's':
            game()
        else:
            print(f'Placar: \n\nVitorias: {placar.vit}, \nEmpates: {placar.emp}, \nDerrotas: {placar.der}')
            print('\nFIM DE JOGO')

    else:
        print('Você venceu!')
        placar.vit += 1
        print('Deseja jogar mais uma partida? (s/n)')
        resp = input(' ')

        if resp == 's':
            game()
        else:
            print(f'Placar: \n\nVitorias: {placar.vit}, \nEmpates: {placar.emp}, \nDerrotas: {placar.der}')
            print('\nFIM DE JOGO')


if __name__ == '__main__':
    main()





