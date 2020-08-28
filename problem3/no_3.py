# 신문배달 문제

'''
구독료가 미납된 세대를 제외하는 방법
모든 nested arr 마다 aarears를 검사하기는 비효율적..
층 마다 하나씩 제외해야할 세대가 있기 때문에
1층 - index 0, 2층 - index 1, 3층 - index 2, 4층 - index 3 으로..
각각 하나씩 검사하는 걸로
'''

apart = [[101, 102, 103, 104], [201, 202, 203, 204], [301, 302, 303, 304], [401, 402, 403, 404]]
arrears = [101, 203, 301, 404]

def run():
    for floor in range(4):
        for customer in range(4):
            if apart[floor][customer] != arrears[floor]:
                print(f'Newspaper delivery: {apart[floor][customer]}')

if __name__ == '__main__':
    run()