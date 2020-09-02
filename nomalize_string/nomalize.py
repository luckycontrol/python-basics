"""
OCP - 프로그램 개발 원칙
1. 프로그램은 수정되지 말아야한다.
2. 하지만 수정 가능해야한다.

객체지향은 OCP를 위해 오버라이딩과 상속을 사용한다.

파이썬은 함수가 객체기에 함수를 잘 사용하면..
"""

import re

# Functional Programming
# 함수를 여러개 받도록 만든다.
# 여러개의 함수가 지나가면서 데이터를 건드린다.
# data0 ---> data1 ---> data2 ---> data3
#        f1         f2         f3
def run():
    states = ['Alabama', 'Georgial', 'Georgia', 'georgia', 'FlOrida', 'south carolina ', 'West virginia?']

    states = clean_string(states, str.strip, remove_special)
    print(states)

def clean_string(strings, *funcs):
    results = []

    for s in strings:
        for f in funcs:
            s = f(s)

        results.append(s)

    return results

def f1(s):
    # s.strip - 객체의 함수
    r = str.strip(s)
    return r

def remove_special(s):
    return re.sub('[?!#^&$@]', '', s)

if __name__ == '__main__':
    run()