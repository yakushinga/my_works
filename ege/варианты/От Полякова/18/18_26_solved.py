"""
нужно максимизировать количество заявок в расписании
основная идея таких задач - сортировка по времени окончания.
После сортировки имеем самую раннюю задачу.
start - время начала относительно последней добавленной
finish - время окончания относительно последней добавленной


"""

f = open('26-142.txt')
n = int(f.readline())
lst = [[int(y) for y in x.split()] for x in f]
print(lst[:10])
lst.sort(key=lambda x: x[1])
print(lst[:10])
start = 0
finish = 0
mx = 0
count = 0
for item in lst:
    if finish <= item[0]:
        #если текущая заявка может быть обработана
        #т.е. ее время начала позже текущего времени окончания
        count = count + 1
        #заменяем start <==> finish
        start = finish
        finish = item[1] + 10
        #считаем время простоя
        mx = item[0] - start + 10
    #выбор заявки с более ранним началом
    if start <= item[0]:
        mx = max(mx, item[0] - start + 10)
print(count, mx)