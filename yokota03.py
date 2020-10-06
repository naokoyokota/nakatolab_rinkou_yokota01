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
def read_file(file_path):
#    lines = read_file(file_path)
    #countlines with pandas
    df= pd.read_table(file_path, encoding='utf-8',header=None,names=["city", "town"])
    return len(df)

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    nlines = args.number
    #countlines with pandas
    df= pd.read_table(filename, encoding='utf-8',header=None)
    num=len(df) #topic1

    print('file: %s' % filename)
    print('number: %d' % nlines)
    num_lines=nlines # topic3
    #len = count_lines(filename)
    #print('length is {}'.format(A))
    print(filename)
    print(nlines)
    print(df.head(num_lines)) #topic3
