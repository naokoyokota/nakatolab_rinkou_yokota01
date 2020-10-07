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

    #extract n lines from head and save into a file
    df_nlines = df.head(nlines)
    prefix = os.path.splitext(filename)[0]
    output2 = '{}_nlines.txt'.format(prefix)
    df_nlines.to_csv(output2, encoding='utf-8', columns=None, header=None, index=None, sep='\t')
