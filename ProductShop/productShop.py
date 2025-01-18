with open('products.txt', 'w') as file:  # открываем файл и очищаем содержимое
    file.write('')
    file.close()


class Shop():
    __file_name = 'products.txt'

    def add(self, *products):  # добавление в список продутов
        name = self.__file_name
        with open('products.txt', 'a') as file:  # открыть файл для добавления записи
            for product in products:
                if str(product) in self.get_products():  # если продукт в списке, то не записываем
                    print(f'Продукт "{product}" уже есть в магазине')
                else:
                    file.write(f'{product}\n')  # дописываем продутк и ставим символ переноса строки
            file.close()

    def get_products(self):  # получение списка продуктов
        with open('products.txt', 'r') as file:  # открывает файл для чтения
            product_list = file.read()
            file.close()
        return product_list


class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __repr__(self):
        return f'{self.name}, {self.weight}, {self.category}'

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


if __name__ == "__main__":
    milk = Product('milk', 1.0, 'dairy products')
    meat = Product('meat', 2.6, 'meat products')
    bananas = Product('bananas', 1.3, 'fruits')
    tide = Product('Tide', 3.0, 'washing')
    splat = Product('splat', 0.250, 'toothpaste')

    my_list = Shop()
    my_list.add(milk, meat, bananas)
    print(my_list.get_products())
    my_list.add(tide, splat, bananas) # бананы уже были
    print(my_list.get_products())
