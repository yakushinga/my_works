from re import finditer

with open("24-347.txt") as f:
    s = f.read()

'''
К сожалению без регулярных выражений написать очень сложно.
Например в строке
TTT0002332895CCYY
написанный ниже код найдет
0002332895CC
А нужно
2332895

То что получился правильный ответ это случайность
т.к. захватывает лишний символ в конце

alf = "0123456789ABCDE"
smax = [0, 0]
nonalf = "FGHIJKLMNOPQRSTUVWXYZ"
ss=""
i = 0
while i < len(s):
    l = ""
    while s[i] in alf and i < len(s):
        l += s[i]
        i += 1
    if l != "":
        n = int(l, 15)
        if n > smax[0]:
            smax = [n, i-2]
            ss=l
    i += 1

print(smax)
print(ss)
'''

"""
[1-9ABCDE][0-9ABCDE]*[05A]
[1-9ABCDE] первый символ не 0
[0-9ABCDE]* следующие любые допустимые для 15ричной
[05A] заканчивается на один из этих символов
"""

ans = []
for g in finditer(r'[1-9ABCDE][0-9ABCDE]*[05A]', s):
    ans.append(g.group(0))
m = max(len(d) for d in ans)
ans = sorted([d for d in ans if len(d) == m])
print(ans)
print(s.find(ans[0])+len(ans[0])-1)

print("------------")
# Вариант с итерацией, но с конца, потому что нужен 
# маркер начала правильной строки
alf = "0123456789ABCDE"
tail = "05A"

i=len(s)-1
ss=""
ms="0"
mx=0

while i>=0:
    # если нашли правильную цифру в конце
    if s[i] in tail:
        j=i-1
        #Ищем начало
        while s[j] in alf and j>=0:
            j=j-1
        #Вырезали кусок
        ss=s[j+1:i+1]
        # Если не просто 0
        if ss!="0":
            #Убираем ведущие 0
            while ss!="" and ss[0]=="0" :
                ss=ss[1:]
            # Поиск максимума
            if int(ss,15)>int(ms,15):
                ms=ss
                mx=i
        # Сдвиг индекса
        i=j
    else:
        i=i-1

print(ms)#Числов
print(mx)#Искомый индекс

         