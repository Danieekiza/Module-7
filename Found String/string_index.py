from idlelib.iomenu import encoding

with open('text.txt', 'w') as file:  # открываем файл и очищаем содержимое
    file.write('')
    file.close()


def custom_write(file_name, strings):
    with open(file_name, 'a', encoding='utf-8') as file:  # открываем файл для добавления в кодировке utf-8
        num = 0  # счетчик строк
        strings_positions = {}  # словарь строк файла
        for string in strings:
            cur = file.tell()  # положение курсора перед записью строки
            num += 1
            file.write(f'{string}\n')  # запись строки
            index = (num, cur)  # ключ словаря
            strings_positions.update({index: string})  # запись ключ-значения в чловарь
    file.close()
    return strings_positions


_list = ['Однажды', 'в', 'студеную', 'зимнюю', 'пору', 'я', 'вышел', 'из', 'дому']

info = custom_write('text.txt', _list)
for elem in info.items():
    print(elem)
