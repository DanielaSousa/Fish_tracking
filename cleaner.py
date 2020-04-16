import csv
import os
import glob
import pandas as pd

def map_val (x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

folder = "B.5c.16h20"
path = "./Files/"
def create_clean_file():

    f_x = open( path +folder+folder+"Tracking_0.txt", "r")
    xx = pd.read_csv(f_x, header=None, delim_whitespace=True)
    # print(xx)

    new = xx[[3,4]].copy()
    new.columns = ["xx", "yy"]
    #new.to_csv( "./Files/"+folder+"/combined.csv", index=False, encoding='utf-8-sig')

    #print(new['xx'].min(), new['xx'].max(), new['yy'].min(), new['yy'].max())
    print(path +folder+folder[:-1]+"_Arena.txt")
    arena = open(path +folder+folder[:-1]+"_Arena.txt", "r")
    line = arena.readline()
    line = arena.readline().split('\n')
    #print(line)

    l= line[0].split('\t')

    xi, yi, xr, yr = int(l[0]),int(l[1]),int(l[2]),int(l[3])
    # print(xi, xf, yi, yf)


    altura_y = 70 #mm
    largura_x = 160 #mm

    x_mm = map_val(34.2, 125.0, 311.0-125.0, 0.0, 160.0) #mm
    new['xx_mm'] = new.apply(lambda row: map_val(row.xx, 0.0, float(xr), 0.0, 160.0), axis=1)
    new['yy_mm'] = new.apply(lambda row: map_val(row.yy, 0.0, float(yr), 0.0, 70.0), axis=1)
    #new['xx_mm','yy_mm'].to_csv( "./Files/"+folder+"/combined.csv", index=False, encoding='utf-8-sig')
    new.to_csv( path + folder +folder+"/combined.csv", mode='w', columns=['xx_mm','yy_mm'], index=False, encoding='utf-8-sig')
    #print(new)
    # df['c'] = df.apply(lambda row: row.a + row.b, axis=1)
    # df