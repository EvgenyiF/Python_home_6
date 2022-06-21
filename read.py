from cgitb import text
import csv
import string
import textwrap
def reader(file,separ):
    with open(file, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file,delimiter=separ)
        count = 0
        i=0
        resalt = []
        if separ == "\n":
            for row in file_reader:
                resalt.append(row[0])
            print(resalt)
            count += 1
            
        else:
            for row in file_reader:
                print(f'{row[0]} {row[1]} тел. {row[2]} {row[3]}.')
                count += 1