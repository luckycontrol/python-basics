def run():
    menu_dict = {'오뎅': 300, '순대': 400, '만두': 500}

    menu = input('메뉴: ')

    if menu in menu_dict.keys():
        print(f'가격 : {menu_dict[menu]}')

if __name__ == '__main__':
    run()