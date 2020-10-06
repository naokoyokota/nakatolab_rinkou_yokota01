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
def read_file(file_path):
#    lines = read_file(file_path)
    #countlines with pandas
    df= pd.read_table(file_path, encoding='utf-8',header=None,names=["city", "town"])
    return df
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
    df = read_file(filename)
    for index, value in df["city"].value_counts().iteritems(): #topic5
        print(index, ': ', value) #topic5
