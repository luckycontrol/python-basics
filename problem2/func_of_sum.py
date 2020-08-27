'''
문제 5
함수 sum을 만든다. 함수는 임의의 갯수의 인수를 받아서 그 합을 계산한다.
'''

def run():
    input_arr = []

    while True:
        arg = input('press "q" to exit')

        if arg == 'q':
            break
        else:
            input_arr.append(int(arg))

    result_sum = sum(*input_arr)
    print(result_sum)


def sum(*args):
    sum_result = 0

    for i in args:
        sum_result += i

    return sum_result

if __name__ == '__main__':
    run()