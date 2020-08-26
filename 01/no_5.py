p_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def run():

    count = 0
    sum = 0

    for i in p_arr:
        if int(i) % 3 == 0:
            count += 1
            sum += i

    print(f'주어진 리스트에서 3의 배수의 개수 => {count}')
    print(f'주어진 리스트에서 3의 배수의 합 => {sum}')

if __name__ == '__main__':
    run()