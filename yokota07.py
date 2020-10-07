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
    return df
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
    df = read_file(filename)

    #df.to_csv('address_space.txt', encoding='utf-8',sep=' ') #topic２
    print('file: %s' % filename)
    #１列目だけ抽出する
    df=df["town"]
    df.drop_duplicates( keep='last', inplace=True)
    prefix = os.path.splitext(filename)[0]
    output = '{}_col2.txt'.format(prefix)
    df.to_csv(output, encoding='utf-8',sep='\t')
    
