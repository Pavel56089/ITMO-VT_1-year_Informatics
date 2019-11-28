# _*_ coding: utf-8 _*_
#-*-coding:utf8-*-
import codecs
def ConvertToInt(n):
    c=0
    if len(n) == 3:
        c = 100
    elif len(n) == 2:
        c = (ord(n[0])-48)*10 + (ord(n[1])-48)
    elif len(n) == 1:
        c = (ord(n[0])-48)
    return c


file = codecs.open( "input.txt", "r", "utf-8" )
data = file.read()
print(data)
#разбиваем строки
length = data.split('\n')
NewData = [None] * len(length)
#находим средний балл каждого
for i in range(len(length)):
    item = length[i].split(' ')
    print(item)
    SumOfPoints = (ConvertToInt(item[4])+ConvertToInt(item[5])+ConvertToInt(item[6]))/3
    NewData[i] = item[0] + ' ' + item[1] + ' | ' + item[2] + ' | ' + item[3] + ' | ' + item[4] + ' ' + item[5] + ' ' + item[6] + ' -> ' + str(SumOfPoints), item[0]

NewData = sorted(NewData, key=lambda x: x[1])
print("sorted")
print(NewData)
print("ВЫВОД:")
NewData[0][0]
NewData[1][0]
print("ВОТ")
for i in NewData:
    print(i[0])

file.close()