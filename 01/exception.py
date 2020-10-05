def  handling_exception():
    lst = []

    try:
        print("예외 가능 코드 블록")
        if len(lst) > 3: # 방어 코드
            lst[3] = 1

        # result = 4 / 0
        int("string")
    except Exception as e: # 구체적 예외
        print(e, type(e))


    print("End of code")


def caller(): # 호출 하는 함수
    try:
        result = callee(4, 0)
    except ZeroDivisionError as e:
        print(e, type(e))
    else:
        print(result)

def callee(a, b): # 호출 되는 함수
    """
    호출 되는 함수는 내부에서 완벽하게 예외를 처리해 복구하기 힘들다면

    """
    if b == 0:
        raise ZeroDivisionError("0으로 나눌 수 없다.")

    return str.format(f"{a} / {b} = {a / b}")

if __name__ == "__main__":
    handling_exception()