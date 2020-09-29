import os
import sys
import argparse
import numpy as np
import pandas as pd
df= pd.read_table('address.txt', encoding='utf-8',header=None)
df.to_csv('address_space.txt', encoding='utf-8',sep=' ')
