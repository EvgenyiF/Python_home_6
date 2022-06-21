import csv
def writer(text, file, separ):
    with open(file,'a', newline="") as f:
        file_writer = csv.writer(f, delimiter = separ, lineterminator="\r")
        file_writer.writerow (text)