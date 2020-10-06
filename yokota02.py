# importするライブラリは冒頭にまとめて記述
import os
import sys
import argparse
import pandas as pd

#def read_file(path):
#    lines = []
#    with open(path, "r", encoding="utf-8") as f:
#        lines = f.readlines()
#        lines = [ln.strip(os.linesep) for ln in lines]

#    return lines

#change this function that uses pandas library
def read_file(file_path):
#    lines = read_file(file_path)
    #countlines with pandas
    df= pd.read_table(file_path, encoding='utf-8',header=None,names=["city", "town"])
    return df

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    #parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    #nlines = args.number

    print('file: %s' % filename)
    #print('number: %d' % nlines)
    df = read_file(filename)
# save as a file with space
    df.to_csv('address_space.txt', encoding='utf-8',sep=' ')


#    print('length is {}'.format(len)) #topic1
