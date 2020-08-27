# 문제1. 키보드로 정수를 입력받아 3의 배수인지 판단.

import sys

def run():
    num = input('수를 입력하세요: ')



    num = int(num)
    if num % 3 == 0:
        print('3의 배수 입니다.')
    else:
        print('3의 배수가 아닙니다.')

if __name__ == "__main__":
    run()