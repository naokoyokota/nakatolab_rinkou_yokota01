import os
import sys
import argparse
import numpy as np
import pandas as pd
df= pd.read_table('address.txt', encoding='utf-8',header=None)
#課題１
print(len(df))
