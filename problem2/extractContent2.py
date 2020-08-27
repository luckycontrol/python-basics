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

    # 순서대로
    s_split = sorted(s_split)
    print(s_split)

    # 출력
    for _ in s_split:
        print(_)

    print()

    # 문자 - 갯수 출력
    result_dic = {}
    for word in s_split:
        result_dic.update({word: s_split.count(word)})

    for k, v in result_dic.items():
        print(f'{k} : {v}')

if __name__ == '__main__':
    run()


