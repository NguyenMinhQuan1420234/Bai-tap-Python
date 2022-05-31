import os
from os import path
import csv

def read_file(filename):
    dd = os.getcwd() + "\\bai11\\" + filename
    if path.exists(dd):
        f = open(dd, "r" , encoding = "utf-8")
        nd = f.read()
        f.close()
        return nd
    else:
        return "Khong co tap tin nay"

def read_report_file_cach1(filename):
    dd = os.getcwd() + "\\bai11\\" + filename
    if path.exists(dd):
        file_in = open(dd, "r" , encoding = "utf-8")
        count_lines = 0
        count_words = 0
        count_chars = 0
        str = ''

        for line in file_in:
            str = str + line
            count_lines = count_lines + 1
            for word in line.split():
                count_words = count_words + 1
            count_chars = count_chars + len(line)
        file_in.close()
        print('Content of files: ')
        print(str)
        print("Report: \n")
        print('Lines:',count_lines,', Words:',count_words, ', Chars: ', count_chars)
    else:
        print("Khong co file nay")

def read_report_file_cach2(filename):
    dd = os.getcwd() + "\\bai11\\" + filename
    if path.exists(dd):
        lines = len(open(dd, "r" , encoding = "utf-8").readlines())
        file_in = open(dd, "r" , encoding = "utf-8")
        nd = file_in.read()
        count_words = len(nd.split())
        count_chars = len(nd)

        file_in.close()
        print("Noi dung file: \n",nd)
        print("Report: \n",'Lines:', lines ,', Words:',count_words, ', Chars: ', count_chars)
    else:
        print("Khong co file nay")

def read_file_csv(filename):
    dd = os.getcwd() + "\\bai11\\" + filename
    if path.exists(dd):
        f = open(dd)
        for row in csv.reader(f):
            print(row)
        f.close()
    else:
        print("Khong co tap tin")

def write_csv_file(filename, listContent):
    dd = os.getcwd() + "\\Bai11\\" + filename
    f = open(dd, 'a', newline = '')
    for item in listContent:
        csv.writer(f).writerow(item)
    f.close()

read_report_file_cach2("baihat.txt")
read_report_file_cach1("baihat.txt")