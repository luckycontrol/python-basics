'''
파이썬과 소수에 대한 이슈

부동소수점에 관하여 연산을 수행할 때 하드웨어는 이진수에 근사한 수를 저장한다.
하지만 파이썬은 위의 이진법에 근사한 수를 10진수에 가깝게 출력한다.
예를 들어 0.1은 하드웨어 측면에서 0.10000000000001115123125... 이지만
이를 파이썬에서는 보기쉽게 0.1로 출력해준다.
이는 이진 부동소수점에서 흔한 모습이다.
보기 좋게 출력하기 위해서 round 함수를 이용한다.
round 함수 내에서 ndigits 인수에 값을 주어, 해당 자릿수부터 반올림하도록 한다.
'''

def run():
    float_input = float(input())ㄴ

    float_list = frange(float_input)
    print(float_list)

def frange(val, start=0.0, step=0.1):
    frange_list = []

    while True:
        if start >= val:
            break

        else:
            frange_list.append(round(start, 2))
            start += step

    return frange_list

if __name__ == '__main__':
    run()