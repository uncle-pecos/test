import xml.etree.ElementTree as ET
import os, fnmatch

def xml_parse(xml_file, tag):
    result = {}
    settings = xml_file.findall(tag)
    for i in settings:                            #закидываем инфу из тегов в массив
        for j in range(1,36):  
            try:                                  #парсим 35 тегов    
              temp = settings[0][j].text.strip()  #закидваем значение, удаляя пробелы
              name = settings[0][j].tag
              result[name] = temp                 #добавляем "тег = значение" в словарь
            except:
                AttributeError
                FileNotFoundError
                pass
    for i in result:
        print(i, ' = ', result[i])              #выводим всё, что распарсили
    print('Файл пропарсен')

def get_map_name(file):                            #вытаскиваем название карты из имени файла
    map_name = ''
    index = file.index('_wotreplay')
    temp = file[index-1]
    while not temp.isdigit():                                       
        temp = file[index-1] 
        index -= 1            
        map_name += temp
    while temp.isdigit():
        temp = file[index-1]
        index -= 1       
        map_name += temp
    map_name = map_name[::-1]
    map_name = map_name[1:]   
    return map_name


path = "C:\\testttttt"
files = []
file_names = []

try:
    print('Введите название стенда:')
    dir = input()                                   #вводим название стенда (папки)
    listOfFiles = os.listdir(path + '\\' + dir)     #добавляем его в путь
    print('Введите расширение файлов для парсинга:')
    pattern_for_file = '*.' + input()               #вводим расширение файла для парсинга(для демо, захардкодим расширение, когда доделаем)

    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern_for_file):
            print('Добавлен файл для парсинга ' + entry)    
            files.append(path + '\\' + dir + '\\' + entry)   #создаем список файлов с полным путем
            file_names.append(entry)                        #создаем отдельно список названий файлов
    if files == []:                                         #если список по итогу пустой, то файлов с нужным расширением у нас нет
        print('Файлов с таким расширением не найдено')
    else:
        print('Введите название тега для парсинга:')        #вводим тег, внутри которого мы будем доставать инфу
        input_tag = input()
  
    for i in files:                                         
        try:
            xml_file = ET.parse(i)
            print('Парсим файл', i)
            print('Название карты: ' + get_map_name(i))     #выводим название карты для каждого файла
            xml_parse(xml_file,input_tag)                   
        except:
            FileNotFoundError
            xml_file = ET.parse(i)                          #except для файлов другой структуры(если нет в имени файла название карты)
            xml_parse(xml_file,input_tag)                   
            pass  
except:
    FileNotFoundError
    print('Такой дериктории не найдено')



