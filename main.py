from asyncore import read
import csv
import create 
import write
import read
import os
import separator

os.remove('tel.csv')
n = int(input('Введите количество контактов, которые хотите внести:'))
separ = int(input("Выберите разделитель (1 =\ n) (2=:) (3=-) (4=*): "))
separ = separator.get_separ(separ)
# separ = "\n"
file = 'tel.csv'
for i in range(n):
    create.get_data()
    text = create.a
    write.writer(text, file, separ)
read.reader(file,separ)
