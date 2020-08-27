def run():
    float_input = float(input())

    [print(float_num) for float_num in frange(float_input)]

def frange(val, start=0.0, step=0.1):
    frange_list = []

    for float_num in range(0.0, val, 0.1):
        frange_list.append(float_num)

    return frange_list

if __name__ == '__main__':
    run()