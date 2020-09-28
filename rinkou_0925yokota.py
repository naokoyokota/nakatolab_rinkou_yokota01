# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas as pd
def read_file(path):
    lines = []
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        lines = [ln.strip(os.linesep) for ln in lines]

    return lines

# change this function that uses pandas library
#def count_lines(file_path):
#    lines = read_file(file_path)
#    return len(lines)

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    nlines = args.number
    #countlines with pandas
    df= pd.read_table(filename, encoding='utf-8',header=None) #topic１
    A=len(df) #topic1
    df.to_csv('address_space.txt', encoding='utf-8',sep=' ') #topic２

    print('file: %s' % filename)
    print('number: %d' % nlines)
    B=nlines-1 # topic3
    #len = count_lines(filename)
    print('length is {}'.format(A))
    print(filename)
    print(nlines)
    print(df.head(B)) #topic3
    print(df.tail(B)) #topic4
    C=df.iloc[B] #topic5
    print(C) #topic5
