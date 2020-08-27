cal_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
count_list = []

def run():
    money = int(input('금액: '))

    for index in range(len(cal_list)):
        count_list.append(money // cal_list[index])
        money = money % cal_list[index]

    for count in range(len(count_list)):
        print(f'{cal_list[count]}원 : {count_list[count]}개')

if __name__ == '__main__':
    run()