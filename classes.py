from abc import ABC, abstractmethod
from json import dumps, dump


class Storage(ABC):

    @abstractmethod
    def add(self, title, quantity):
        """
        увеличивает запас items
        :param title: название
        :param quantity: количество
        :return:
        """
        pass

    @abstractmethod
    def remove(self, title, quantity):
        """
        уменьшает запас items
        :param title: название
        :param quantity: количество
        :return:
        """
        pass

    @abstractmethod
    def get_free_space(self):
        """
        :return: вернуть количество свободных мест
        """
        pass

    @abstractmethod
    def get_items(self):
        """
        :return: возвращает содержание склада в словаре {товар: количество}
        """
        pass

    @abstractmethod
    def get_unique_items_count(self):
        """
        :return: возвращает количество уникальных товаров
        """
        pass


class Store(Storage):

    def __init__(self, items, capacity=100):
        self.__items = items
        self.__capacity = capacity

    def __repr__(self):
        return self.__items

    def get_free_space(self):
        """
        :return: вернуть количество свободных мест
        """
        return self.__capacity - sum([value for value in self.__items.values()])

    def add(self, title, quantity):
        """
        увеличивает запас items
        :param title: название
        :param quantity: количество
        :return:
        """
        if title in self.__items.keys():
            if self.get_free_space() >= quantity:
                self.__items[title] += quantity
                return True
            else:
                print('На складе недостаточно места, попробуйте что то другое')
                return False
        else:
            if self.get_free_space() >= quantity:
                self.__items[title] = quantity
                return True
            else:
                print('На складе недостаточно места, попробуйте что то другое')
                return False



    def remove(self, title, quantity):
        """
        уменьшает запас items
        :param title: название
        :param quantity: количество
        :return:
        """
        if self.__items[title] >= quantity:
            self.__items[title] -= quantity
            return True
        else:
            print(f'Нет столько {title}, попробуйте заказать меньше')
            return False

    @property
    def get_items(self):
        """
        :return: возвращает содержание склада в словаре {товар: количество}
        """
        return self.__items

    def get_unique_items_count(self):
        """
        :return: возвращает количество уникальных товаров
        """
        return len(self.__items)


class Shop(Store):

    def __init__(self, items, capacity=20):
        super().__init__(items, capacity)

    def add(self, title, quantity):
        if title in self.get_items or super().get_unique_items_count() < 5:
            return super().add(title, quantity)
        else:
            print('В магазине недостаточно места, попробуйте что то другое')
            return False


class Request:

    def __init__(self, stores, task: str):
        __req_list = task.split(' ')
        self.__action = __req_list[0]
        self.__amount = int(__req_list[1])
        self.__product = __req_list[2]
        if self.__action == 'Доставить':
            self.__from_place = __req_list[4]
            self.__to_place = __req_list[6]
        elif self.__action == 'Забрать':
            self.__from_place = __req_list[4]
            self.__to_place = None
        elif self.__action == 'Привезти':
            self.__to_place = __req_list[4]
            self.__from_place = None
        self.stores = stores

    def move(self):

        if self.__from_place is not None:

            was_taken = eval(self.__from_place).remove(self.__product, self.__amount)
            if was_taken:
                print(f'Курьер забрал {self.__amount} {self.__product} из {self.__from_place}')
                if self.__to_place is not None:
                    print(f'Курьер везет {self.__amount} {self.__product} в {self.__to_place}')
                    was_added = eval(self.__to_place).add(self.__product, self.__amount)
                    if was_added:
                        print(f'Курьер доставил {self.__amount} {self.__product} в {self.__to_place}')

        else:

            if self.__to_place is not None:
                print(f'Курьер везет {self.__amount} {self.__product} в {self.__to_place}')
                was_added = eval(self.__to_place).add(self.__product, self.__amount)
                if was_added:
                    print(f'Курьер доставил {self.__amount} {self.__product} в {self.__to_place}')


store_1 = Store(items={'товар1': 1, 'товар2': 2, 'товар3': 7})
store_2 = Store(items={'товар1': 3, 'товар2': 6, 'товар3': 4})
shop = Shop(items={'товар1': 3, 'товар2': 6, 'товар3': 4})