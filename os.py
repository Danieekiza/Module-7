import os
print('Текущая директория:',os.getcwd())  # папка проекта
# os.mkdir('second')  # создание папки
if os.path.exists('second'): # проверяет наличие указанного пути
    os.chdir('second') # изменение текущей дирректории
else:
    os.mkdir('second') # если нет, то создать
    os.chdir('second')

print('Текущая директория:',os.getcwd())
# os.makedirs(r'third\fourth')  # создает вложенные папки в текущей дирректории r - для \
# print('Текущая директория:',os.getcwd())  # папка проекта
for i in os.walk('.'):  # просмотр вложенных папок
    print(i)
os.chdir(r'C:\Users\D.Kozlov\PycharmProjects\pythonProject1')
print('Текущая директория:',os.getcwd()) # изменение текущей дирректории
# my_file = open("file.txt", "w+")  # создать в тек дир файл
# for i in os.walk('.'):  # просмотр вложенных папок
#     print(i)
file = [f for f in os.listdir() if os.path.isfile(f)] # генератор списков упорядоченный
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(file)
print(dirs)
# os.startfile(file[7]) # Здесь [3] — это индекс файла в списке file,
# указывающий на четвертый элемент. После выполнения этой команды будет открыт текстовый файл
print(os.stat(file[7]))  # время создания, время обновления, размер и другие атрибуты
os.system('pip install random2') # обращение к командной строке
