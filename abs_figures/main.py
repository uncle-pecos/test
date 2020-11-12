from circle import Circle
from rectangle import Rectangle
from square import Square
from triangle import Triangle

print('Введите количество углов фигуры (от 0 до 4)')
corner = int(input())
if corner == 0:
      print('Введите радиус круга')
      size = int(input()) 
      krug = Circle('krug', size)
      print ('Площадь фигуры равна ' + str(krug.sq(size)))
elif corner == 3:
      print('Введите длину стороны (треугольник будет равносторонним)')
      size = int(input())
      treugolnik = Triangle('treugolnik', size)
      print ('Площадь фигуры равна ' + str(treugolnik.sq(size)))
elif corner == 4:
      print('Квадрат или прямоугольник? (введите "кв" или "пр")')      
      four = str(input())
      i = 5
      while four != 'кв' or four != 'пр':
          if four == 'кв' or four == 'пр':
              break
          else:
              i -= 1
          if i>1:
            print('Ты как-то коряво ввёл. Го еще раз. У тебя', i, 'попытки')
            four = str(input())
          elif i == 1:
            print('Ты как-то коряво ввёл. Го еще раз. У тебя', i, 'попытка')
            four = str(input())
          elif i == 0:
            print('Ты рили такой корявый? Никакой тебе площади. Считай сам.')
            break
      if four == 'кв':
          print('Введите длину стороны квадрата')
          size = int(input())
          kvadrat = Square('kvadrat', size)
          print ('Площадь фигуры равна ' + str(kvadrat.sq(size)))
      elif four == 'пр':
          print('Введите длину прямоугольника')
          size1 = int(input())
          print('Введите ширину прямоугольника')
          size2 = int(input())
          if size1 == size2:
            print('Это квадрат бл*ть')
            kvadrat = Square('kvadrat', size1)
            print ('Площадь фигуры равна ' + str(kvadrat.sq(size1)))
          else:
            pryamougolnik = Rectangle('pryamougolnik', size1, size2)
            print ('Площадь фигуры равна ' + str(pryamougolnik.sq(size1, size2)))
elif corner == 1 or corner ==2:
  print('Такой фигуры быть не может')
else: 
  print('Ну алло, я ж просил от 0 до 4')