# 파이썬 파일 읽기

def run():
    linenum = 0

    with open('file.py', 'rt', encoding='utf-8') as f:
        while True:
            line = f.readline()

            if line == '':
                f.close()
                break

            linenum += 1
            print(f'{linenum} : {line}', end='')


    print()

    print('===== line 단위로 읽기 2 ====')

    with open('file.py', 'rt', encoding='utf-8') as f:
        lines = f.readlines()

        for num, line in enumerate(lines):
            print(f'{num + 1} : {line}', end='')

if __name__ == '__main__':
    run()