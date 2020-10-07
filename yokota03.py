import os
import sys
import argparse
import pandas as pd

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    nlines = args.number

    #countlines with pandas
    df = pd.read_table(filename, encoding='utf-8',header=None)

    print('file: %s' % filename)
    print('number: %d' % nlines)

    num_lines = nlines # topic3
    print(filename)
    print(nlines)
    print(df.head(num_lines)) #topic3
