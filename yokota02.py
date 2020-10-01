import os
import sys
import argparse
import numpy as np
import pandas as pd
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    nlines = args.number

    print('file: %s' % filename)
    print('number: %d' % nlines)
    #len = count_lines(filename)

    #countlines with pandas
df= pd.read_table('address.txt', encoding='utf-8',header=None)
df.to_csv('address_space.txt', encoding='utf-8',sep=' ')


