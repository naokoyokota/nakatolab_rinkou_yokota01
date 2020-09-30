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
    parser.add_argument("min_number", help="minimum number of lines", type=int)
    parser.add_argument("max_number", help="maximum number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    nlines = args.min_number
    mlines = args.max_number
    #countlines with pandas
    df= pd.read_table(filename, encoding='utf-8',header=None)
    A=len(df) #topic1

    print('file: %s' % filename)
    print('min_number: %d' % nlines)
    print('max_number: %d' % mlines)
    B=nlines
    C=mlines+1
    print('length is {}'.format(A))
    print(filename)
    print(nlines)
    print(mlines)
    print(df[B:C]) #topic6
