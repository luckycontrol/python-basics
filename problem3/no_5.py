# 선택정렬문제
# 내림차순 정렬

arr = [5, 9, 3, 8, 60, 20, 1]

def run():
    print(f'Before sort. \n {arr}')

    for _ in range(len(arr)):
        for sort_index in range(len(arr)):
            if sort_index != len(arr) - 1:
                if arr[sort_index] < arr[sort_index + 1]:
                    arr[sort_index], arr[sort_index + 1] = arr[sort_index + 1], arr[sort_index]

    print(f'After Sort. \n {arr}')

if __name__ == '__main__':
    run()