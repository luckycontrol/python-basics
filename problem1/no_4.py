def run():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{j} x {i} = {j * i}', end='\t\t')
        print()

if __name__ == '__main__':
    run()