def run():
    s = """We encourage everyone to contribute to Python. If you still have have questions after reviewing the material is this guide, then the Python Mentors group is available to help guide new contributors through the process."""

    # ',' '.' '\n' 제거.
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace('\n', '')

    # 공백으로 Split
    s_split = s.split(' ')

    # 모두 대문자로
    s_split = [word.upper() for word in s_split]

    # 출력
    for _ in s_split:
        print(_)

if __name__ == '__main__':
    run()


