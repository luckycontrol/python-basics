def run():
    for i in range(10):
        for star in range(i):
            print('*', end='')
        print()

    for i in range(10):
        print('*' * i)

if __name__ == '__main__':
    run()