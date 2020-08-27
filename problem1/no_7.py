from functools import reduce

def run():
    arr = []

    for _ in range(5):
        arr.append(int(input()))

    print(f'평균 : {reduce(lambda x, y: x + y, arr) / 5}')

if __name__ == '__main__':
    run()
