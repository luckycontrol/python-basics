def run():
    a = 10
    b = 20

    print(f'변경 전: a: {a}, b: {b}')

    a, b = b, a

    print(f'변경 후: a: {a}, b: {b}')

if __name__ == '__main__':
    run()