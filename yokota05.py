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

# mainéæをåç (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file", help="file path", type=str)
    #parser.add_argument("number", help="number of lines", type=int)

    args = parser.parse_args()

    filename = args.file
    #nlines = args.number
    #print count of the first column removed duplicates with pandas
    df= pd.read_table(filename, encoding='utf-8',header=None) #topic5
    for index, value in df[0].value_counts().iteritems(): #topic5
        print(index, ': ', value) #topic5
