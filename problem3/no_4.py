# 구구단 게임
# 문제를 내고 맞춘다.

'''
and 와 or 문제
user_input.lower() != "y" and user_input.lower() != "n"
y 혹은 n이 아니면 다시입력.. or 아닌가 했지만
or 를 쓰면 y와 n 을 입력해도 다시 입력하라 함.
'''

import random

def run():
    while True:
        multiplyGame()

        while True:
            user_input = input('다시 하시겠습니까? ( y or n ) > ')
            if user_input.isdigit() or user_input.lower() != "y" and user_input.lower() != "n":
                print('다시 입력해주세요.')
            else:
                break

        if user_input == 'n':
            break


def multiplyGame():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    answer = num1 * num2
    answer_location = [random.randint(0, 2), random.randint(0, 2)]

    print(f'{num1} x {num2} = ?', end='\n\n')

    for i in range(3):
        for j in range(3):
            if i == answer_location[0] and j == answer_location[1]:
                print(answer, end='\t')

            else:
                print(random.randint(1, 81), end='\t')
        print()

    print()

    while True:
        user_input = input('answer: ')
        if user_input.isdigit():
            if int(user_input) == answer:
                print(f'\n 정답')
                break
            else:
                print('틀렸습니다. 다시 도전해보세요.')
        else:
            print('숫자를 입력해주세요.')

if __name__ == '__main__':
    run()