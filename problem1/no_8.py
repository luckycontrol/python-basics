def run():
    sentence = input('입력> ')

    reversed_str = reverse(sentence)
    print(''.join(reversed_str))

def reverse(s):
    reversed_str = []

    for i in range(len(s)-1, -1, -1):
        reversed_str.append(s[i])

    return reversed_str

if __name__ == '__main__':
    run()