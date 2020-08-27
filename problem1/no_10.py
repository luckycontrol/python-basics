def run():
    num = int(input('숫자를 입력하세요: '))
    sum = 0

    for i in range(num, 0, -2):
        sum += i

    print(f'결과 값: {sum}')

if __name__ == '__main__':
    run()