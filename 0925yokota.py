import os
import sys
import argparse
import numpy as np
import pandas as pd
df= pd.read_table('address.txt', encoding='utf-8',header=None)
#課題１
print(len(df))
#課題２
df.to_csv('address_space.txt', encoding='utf-8',sep=' ')
#課題3
num= input('Enter your num: ')
a=int(num)
df.head(a)
#課題4
df.tail(a)
#課題５
#pd.df.count((axis=0,level=None,numeric_only=False)
