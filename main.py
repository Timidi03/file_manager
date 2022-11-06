import os
import shutil

i=0
while(i!=11):
    print('''
    1. Создание папки (с указанием имени);
    2. Удаление папки по имени;
    3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
    4. Создание пустых файлов с указанием имени;
    5. Запись текста в файл;
    6. Просмотр содержимого текстового файла;
    7. Удаление файлов по имени;
    8. Копирование файлов из одной папки в другую;
    9. Перемещение файлов;
    10.Переименование файлов.
    11.Закончить программу.
            ''')
    i = int(input())
    if (i == 1):
        print(os.getcwd())
        name = input('Введите название папки: ')
        path = os.getcwd() + '/'+name
        os.mkdir(path)
    elif (i == 2):
        print(os.listdir())
        name = input('Введите название папки: ')
        path = os.getcwd() + '/'+name
        os.rmdir(path)
    elif (i == 3):
        print(os.listdir())
        print(os.getcwd())

        k=input('вверх или вниз?' )
        if k =='вверх':
            path=os.pardir
        elif k == 'вниз':
            name = input('Введите название папки: ')
            path = os.getcwd() + '/' + name
        os.chdir(path)
    elif (i == 4):
        name = input('Введите название файла: ')
        path = os.getcwd() + '/'+name
        text_file = open(path, 'w')
    elif (i == 5):
        text = input('Введите текст для записи в файл: ')
        text_file.write(text)
    elif (i == 6):
        print(os.listdir())
        name = input('Введите название файла: ')
        with open(name,'r') as text_file:
            for line in text_file:
                print(line)
    elif (i == 7):
        print(os.listdir())
        name = input('Введите название файла: ')
        path = os.getcwd() + '/'+name
        os.remove(path)
    elif (i == 8):
        print(os.listdir())
        name = input('Введите название файла: ')
        path = input('Введите путь: ')
        shutil.copy(name, path)
    elif (i == 9):
        print(os.listdir())
        name = input('Введите название файла: ')
        path = input('Введите путь: ')
        shutil.move(name,path)
    elif (i == 10):
        print(os.listdir())
        name = input('Введите старое название файла: ')
        namenew = input('Введите новое название файла: ')
        os.rename(name,namenew)

