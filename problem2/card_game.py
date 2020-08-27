import random

def run():
    while True:
        game()

        again = input('다시 하시겠습니까(y / n) >> ')
        if again == 'n':
            break

def game():
    rand_num = random.randint(1, 100)
    count = 1

    print('수를 결정하였습니다. 맞추어 보세요.')
    print('1 - 100')

    while True:
        user_input = int(input(f'{count} >> '))

        if user_input > rand_num:
            print('더 낮게')
        elif user_input < rand_num:
            print('더 높게')
        else:
            print('맞았습니다!')
            break

        count += 1

if __name__ == '__main__':
    run()