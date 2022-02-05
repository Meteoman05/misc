l = [int(i) for i in input().split(' ')]

mean = sum(l) / len(l)

if len(l) % 2 == 1:
    med = l[len(l) // 2]
else:
    med = (l[(len(l) // 2) - 1] + l[len(l) // 2]) / 2

g = 1

for i in l:
    g *= i

geom = g ** (1 / len(l))

disp = sum([(i - mean) ** 2 for i in l]) / len(l)

print(f'Среднее арифмитическое - {mean}\n'+
      f'Медиана - {med}\n'+
      f'Среднее геометрическое - {geom}\n'+
      f'Дисперсия - {disp}')
