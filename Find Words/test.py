from nt import remove
from pprint import pprint


class WordsFinder:
    file_names = []

    def __init__(self, *args):
        for file in args:
            self.file_names.append(file)

    def get_all_words(self):
        self.all_words = {}
        remove_ch = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']  # список символов для удаления
        for file in self.file_names:
            file_list = []  # список со значениями для словаря по отдельному файлу
            _str = ''  # строка для добавления символов из текста файла
            with open(file, 'r', encoding='utf-8') as file:
                for line in file:  # для каждой строки
                    for char in line:  # для каждого символа в строке
                        if char == '\n':
                            char = ' '  # \n меняем на пробел, что бы слова не сливались в методе split # 26
                        if char not in remove_ch:
                            _str = _str + char.lower()  # все символы добавляем в ниж рег
            value = _str.split()  # список из слов (строку разбили по пробелам)
            self.all_words.update({file.name: value})  # добавили в словарь ключ -файл, значение - список
        return self.all_words

    def find(self, word):  # возвращает словарь ключ - название файла, значение - индекс первого совпадени
        dict = {}
        for item in self.all_words.items():  # паре улюч значение
            if word.lower() in item[1]:
                dict.update({item[0]: item[1].index(word.lower())})  # ключ - название файла, значение - ндекс
        return dict

    def count(self, word):  # возвращает словарь ключ - название файла, значение - индекс колличество вхождения
        dict = {}
        for item in self.all_words.items():
            if word.lower() in item[1]:
                dict.update({item[0]: item[1].count(word.lower())})
        return dict


a = WordsFinder('text1.txt', 'text2.txt', 'text3.txt')
print(a.get_all_words())
print(a.find('Is'))
print(a.count('iS'))
print(a.find('teXt'))
print(a.count('TEXT'))
