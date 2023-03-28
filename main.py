# задание 1
from random import randint
# импортировал fsum, но по условию задачи можно было и встроенный sum() использовать, так целые числа.
from math import fsum
from statistics import fmean, median, stdev

# oбъединил 2 и 4 задание
numbers = []
for i in range(0, 10):
    numbers.append(randint(1, 100))

# 3 задание
print("Список:{0}\n"
      "Сумма элементов:{1}\n"
      "Среднее значение элементов:{2}\n"
      "Медиана:{3}\n"
      "Стандартное отклонение:{4}".format(numbers, fsum(numbers), fmean(numbers), median(numbers), stdev(numbers)))
