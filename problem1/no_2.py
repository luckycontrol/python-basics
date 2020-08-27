def run():
    num = int(input('수를 입력하세요: '))

    if num % 2 == 0:
        print('짝수')
    else:
        print('홀수')

if __name__ == '__main__':
    run()