def run():
    float_input = float(input())

    float_list = frange(float_input)
    print(float_list)

def frange(val, start=0.0, step=0.1):
    frange_list = []

    while True:
        if start >= val:
            break

        else:
            frange_list.append(start)
            start += step

    return frange_list

if __name__ == '__main__':
    run()