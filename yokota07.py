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
    #parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    #nlines = args.number
    #countlines with pandas
    df= pd.read_table(filename, encoding='utf-8',header=None) #topic１
    #A=len(df) #topic1
    #df.to_csv('address_space.txt', encoding='utf-8',sep=' ') #topic２
    print('file: %s' % filename)
    #１列目だけ抽出する
    df=df[0]
    df.drop_duplicates( keep='last', inplace=True)
    A=len(df)
    print(A)

    df.to_csv('address_noduplicate.txt', encoding='utf-8',sep='\t')
