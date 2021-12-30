'''Jogo: pedra papel tesoura'''
import random
import placar

print('Welcome to rock-paper-scissors Game')


def main() -> None:
    game()


def game():
    acao = int(input('press 1 to choose rock, 2 for paper, or 3 for scissor: '))
    contra = random.randint(1, 3)

    dict = {1: 'rock', 2: 'paper', 3: 'scissor'}

    print(f'You choose: {dict[acao]}'
          f'\nYour opponent choose: {dict[contra]}')

    if acao == contra:
        print('You tie!')
        placar.emp += 1
        resp = input('One more game? (y/n)')

        if resp == 'y':
            game()
        else:
            print(f'Score: \n\nWin: {placar.vit}, \nTie: {placar.emp}, \nLoss: {placar.der}'
                  f'\nEND GAME')

    elif (acao == 1 and contra == 2) or (acao == 2 and contra == 3) or (acao == 3 and contra == 1):
        print('You lost!')
        placar.der += 1
        resp = input('One more game? (y/n)')

        if resp == 'y':
            game()
        else:
            print(f'Score: \n\nWin: {placar.vit}, \nTie: {placar.emp}, \nLoss: {placar.der}'
                  f'\nEND GAME')

    else:
        print('You win!')
        placar.vit += 1
        resp = input('One more game? (y/n)')

        if resp == 'y':
            game()
        else:
            print(f'Score: \n\nWin: {placar.vit}, \nTie: {placar.emp}, \nLoss: {placar.der}'
                  f'\nEND GAME')


if __name__ == '__main__':
    main()





