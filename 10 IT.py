import random
import pprint

left = [i for i in input('Введите отсутствующих людей\n').split()]

IT = [['Дереник', 'Паша З', 'Гриша', 'Вова', 'Дамир'],
      ['Дима', 'Эмир', 'Никита', 'Артём', 'Нарек'],
      [None, 'Коля', 'Миша Х', 'Миша П', 'Петя'],
      ['Максим', 'Саша Кол', None, None, None],
      ['Федя', 'Ярик', None, 'Ева', 'Полина'],
      ['Саша Коч', 'Илья', 'Глеб', 'Паша А', 'Венера']]


for i in range(len(IT)):
      for j in range(len(IT[i])):
            for g in left:
                  if g == IT[i][j]:
                        IT[i][j] = None
                  


#ch = int(input('Введите номер ряда >>>'))
#v = int(input('Введите номер варианта >>>'))

pprint.pprint(IT)
      
