import xml.etree.ElementTree as ET
import os, fnmatch
import time

def xml_parse(xml_file):
    result = []
    #result = {}                                    #словарь на случай словаря)
    results = xml_file.findall('results')           #находим тег <results>
    j = -1
    t = True
    for i in results:                      
        while t == True:  
            try:
                j += 1                                      
                temp = i[j].text.strip()            #закидваем значение, удаляя пробелы
                #name = i[j].tag                    #берем имя каждого тега на всякий случай
                result.append(temp)                 #добавляем значение в список
            except IndexError:
                t = False
                pass
                
    #for i in result:
        print(result)              #выводим всё, что распарсили
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
    if index <= 0:                                 #если в названии файла нет названия карты, то выводим --- 
        map_name = '---'
    else:        
        map_name = map_name[1:]                    #если все норм, то разворачиваем строку с названием карты, т.к. парсили с конца 
    return map_name

def main_parsing(path_root):
    files = []                                      #список файлов с полным путем
    file_names = []                                 #список названий файлов                                  
    list_of_folders = os.listdir(path_root)         #список имен папок 
    count_d = 0                                     #каунтер папок
    count_f = 0                                     #каунтер файлов
    print('Список папок в корне:')
    for dir in list_of_folders:                                         #выводим список папок в корне с нумерацией
        count_d += 1
        print(str(count_d) + '. ' + dir)

    try:
        for dir in list_of_folders:                                     #идем по каждой папке в корне
            new_path = path_root + '\\' + dir                                             
            listOfFiles = os.listdir(new_path)     
            print('Добавлена директория для парсинга ' + new_path)             

            for entry in listOfFiles:                                      #идем по каждому файлу в папке
                if fnmatch.fnmatch(entry, pattern_for_file):
                    print('Добавлен файл для парсинга ' + dir + '\\' + entry)    
                    files.append(new_path + '\\' + entry)           #создаем список файлов с полным путем
                    file_names.append(entry)                        #создаем отдельно список названий файлов
            if files == []:                                         
                print('Файлов в папке', dir, 'не найдено')
    
            for i in files:                                #парсим все каждый файл в папке         
                try:
                    xml_file = ET.parse(i)
                    print('Парсим файл', i)                    
                    print('Название карты: ' + get_map_name(i))     #выводим название карты для каждого файла
                    xml_parse(xml_file)
                    count_f += 1
                    
                except FileNotFoundError:           
                    print('Ошибка в файле ' + xml_file)         #если название файла корявое, то скипаем его         
                    pass
            files = []                                          #обнуляем список файлов

    except FileNotFoundError:    
        print('Такой дериктории не найдено')

    print('Пропарсено папок: ' + str(count_d))
    print('Пропарсено файлов: ' + str(count_f))
    print("за %s seconds" % (time.time() - start_time))


start_time = time.time()                          #засекаем время
path = "C:\\testttttt"                            #задаем корневаю папку (тут будет инфа от GUI)
pattern_for_file = '*.btl'                        #задаем расширение файлов, которые будем парсить
main_parsing(path)






