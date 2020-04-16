
import csv
import os
import glob
import pandas as pd

xx_file = "./Files/1/FileX.csv"
yy_file = "./Files/1/filey.csv"

f_x = open(xx_file, "r")
f_y = open(yy_file, "r")

width = 1980
hieght = 460
x = 970
y = 1700

xx = pd.read_csv(f_x, header=None)
yy = pd.read_csv(f_y, header=None)
#combine all files in the list

final = pd.concat([xx, yy], axis=1)
final.columns = ["xx", "yy"]
# print(final)
#export to csv
final.to_csv( "./Files/1/combined.csv", index=False, encoding='utf-8-sig')
