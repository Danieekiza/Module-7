import os
import time

directory = r'C:\Users\Danil - Victoria\PycharmProjects\pythonProject3\second\third\fourth'  # переменна пути для каталога
filename = 'file.txt'
print('Текущая директория:', os.getcwd())  # показать текущую директорию
# for i in os.walk('.'):  # просмотр вложенных папок
#     print(i)
path = os.path.join(directory, filename)  # объединяет два пути в один
print(path)
print(os.path.getmtime(filename))  # отображает время созданя файла в unix time
print(os.path.getsize(filename))  # отображает размер файла
print('Текущая директория:', os.getcwd())  # показать текущую директорию
path_dir = os.path.dirname(path)  # путь к родительской дирректории
print('Родительская директория:', path_dir)

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(os.getcwd(), file)  # записываем текущую директорию
        # print(filepath)
        filetime = os.path.getmtime(filepath)
        # print(filetime)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        # print(formatted_time)
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(os.path.join(os.getcwd(), file))  # родительская дирректория указывается только
        # для полного пути к файлу
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time},\n'
              f'     Родительская директория: {parent_dir}')
