# 3 6 9 게임
# 1. 수에 3 6 9 가 들어가면 짝
# 2. 수에 3 6 9 가 두 번 들어가면 짝짝

def run():
    correct_arr = ['3', '6', '9']

    for num in range(1, 100):
        count = 0
        for inner_num in str(num):
            if inner_num in correct_arr:
                count += 1

        if count >= 1:
            print(num, end=' ')
            for _ in range(count):
                print("짝", end='')
            print()

if __name__ == '__main__':
    run()