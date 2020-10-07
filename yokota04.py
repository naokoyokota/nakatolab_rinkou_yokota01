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

    #read a file with pandas
    df = pd.read_table(filename, encoding='utf-8',header=None)

    print('file: %s' % filename)
    print('number: %d' % nlines)

    print(filename)
    print(nlines)
    #extract n lines from tail and save into a file
    df=df.tail(nlines)
    prefix = os.path.splitext(filename)[0]
    output3 = '{}_nlines_tail.txt'.format(prefix)
    df.to_csv(output3, encoding='utf-8',columns=None, header=None, index=None,sep="\t")
     #topic3
