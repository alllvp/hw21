from classes import Request, shop, store_1, store_2


def main():
    stores = ['store_1', 'store_2', 'shop']
    user_input = input('Введи задание:\n')
    if user_input == 'stop':
        print('Hasta la vista')
        exit()
    try:
        request = Request(stores, user_input)
        request.move()
        for store_item in stores:
            if store_item in user_input:
                print(f'\nВ {store_item} хранится:')
                got_items = eval(store_item).get_items
                for item in got_items:
                    print(f'{got_items[item]} {item}')
    except Exception as e:
        print('Input error:', e.__repr__())


if __name__ == '__main__':
    print('Привет!\n')
    while True:
        main()
