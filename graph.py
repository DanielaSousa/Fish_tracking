#!/usr/bin/python
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import math
#from cleaner import folder, create_clean_file, path
import cleaner
WRITE = 1

def fish_path(df):
    # plot
    plt.plot('xx_mm', 'yy_mm', data=df, linestyle='-', color='green', marker='+')
    plt.xlabel("xx (mm)")
    plt.ylabel("yy (mm)")
    plt.title("Fish path")
    plt.ylim(70, 0)  # decreasing time # TODO read from arena the max yy
    plt.xlim(0, 160)  # decreasing time # TODO read from arena the max yy
    plt.plot([0,160],[10, 10], linestyle='--', color='grey')
    #plt.plot([0, 160], [35, 35], linestyle='--', color='cyan')
    plt.axhspan(0, 35, facecolor='plum', alpha=0.5)
    plt.axhspan(35, 70, facecolor='skyblue', alpha=0.5)
    # for i in range(0, 70, 35):
    #     plt.axhspan(i, i + 35, facecolor='0.2', alpha=0.5)
    #     #plt.axvspan(i, i + .5, facecolor='b', alpha=0.5)
    if WRITE:
        plt.savefig(cleaner.path + cleaner.folder+ cleaner.folder+"fish_path.png")

    plt.show()


# data
# f = open("./Files/"+folder+"/combined.csv", "r")
# df = pd.read_csv(f)
# fish_path(df)

period = 1/30  # s
#cm
#14x16
# altura = 0.07 #m
# largura = 0.16

## arena
# altura 125 311
# largura 881 378
# TODO read from file arena
txt = ""

def mean_velocity(df):
    ## velocidade
    xi = 0
    yi = 0
    mean_vel = 0
    dist_total = 0
    time_total = 0
    i = 0


    for index, row in df.iterrows():
        #print(index, row['xx'], row['yy'])
        if index > 0:
            dist = math.sqrt(((xi - row['xx_mm']) ** 2) + ((yi - row['yy_mm']) ** 2))
            dist_total += abs(dist)
            vel = abs(dist) /period
            if vel > 0:
                time_total+=period
            # print("vel ", vel )# m/s TODO ver os metros
            mean_vel+= vel
            i+=1

        xi = row['xx_mm']
        yi = row['yy_mm']
    #velocidade , distancia total, tempo total a nadar
    #print("mean velocity (mm/s)", mean_vel/i)
    global txt
    txt += "mean velocity (mm/s): " +  str( dist_total/time_total) + '\n' + "total distance (mm): " + str( dist_total) + '\n' + "total time (s): " +str(time_total)
    return mean_vel/i, dist_total, time_total

# print(mean_velocity(df) )
# # tempo à supreficie (1cm)
# surf_time = df[df['yy_mm'] < 10.0]['yy_mm'].count()#[df["yy"] > 200.0].count()
# print("surface time (s)", surf_time * period)
#
# # Tempo em que esta em cima ou em baixo
# upper = df[df["yy_mm"] <=35.0]['yy_mm'].count()
# down = df[df["yy_mm"] >35.0]['yy_mm'].count()
# print("down time (s)", down*period, " upper time (s)", upper*period)



if __name__ == '__main__':
    import sys

    print('Number of arguments:', len(sys.argv), 'arguments.')
    print('Argument List:', str(sys.argv))
    if len(sys.argv) > 1:
        cleaner.folder = str(sys.argv[1])

    cleaner.path = "/media/daniela/BSousa/D-diazepam/"#"/media/daniela/DANIELA_4G/"#"/media/daniela/D5D6-086D/Bea/"
    A = ['A.10.15h20/','A.1.13h50/','A.3.14h10/','A.5.14h30/','A.8.15h/','A.11.15h30/','A.2.14h/','A.4.14h20/', 'A.6.14h40/',
         'A.9.15h10/']
    B = [ 'B.11c.17h30/', 'B.2d.13h20/','B.5d.13h50/','B.7c.16h45/','B.8d.14h20/',
          'B.10c.17h20/','B.11d.14h50/','B.3d.13h30/','B.6c.16h31/','B.7d.14h10/','B.9c.17h10/',
          'B.10d.14h40/','B.1d.13h10/','B.4d.13h40/','B.6d.14h/','B.8c.16h55/','B.9d.14h30/']
    C = ['C.10.12h30/',  'c.4.11h30/', 'C.11.12h40/',  'C.5.11h40/', 'C.3.11h20/',   'C.9.12h20/', 'C.2.11h10/',
         'C.8.12h10/',  'C.12.12h50/',  'C.6.11h50/']
    #l = [ 'B.1c.14h30/', 'B.2c.14h40/', 'B.3c.14h50/', 'B.4c.15h/', 'B.5c.16h20/']
    # 'D.10c.21h35/', 'D.11c.21h55/', 'D.1c.20h05a/','D.1c.20h05b/', 'D.3c.20h25/', 'D.4c.20h35/',
    #l = [ 'D.5.20h45/','D.6c.20h55/','D.7c.2105/','D.8c.21h15/','D.9c.21h25/']
    #'D.10d.18h50/', 'D.11d.19h/','D.12d.19j10/', 'D.1d.16h40/', 'D.2d.16h50/',  'D.3d.17h/', 'D.4d.17h10/',
    l = [ 'D.6d.17h30/', 'D.7d.18h20/', 'D.8d.18h30/', 'D.9d.18h40/']
    for f_tmp in l:
        txt = ""
        cleaner.folder = f_tmp
        cleaner.create_clean_file()
        #path = "./Files/"
        #print(cleaner.path + cleaner.folder + cleaner.folder+ "combined.csv")
        f = open(cleaner.path + cleaner.folder + cleaner.folder + "combined.csv", "r")
        df = pd.read_csv(f)
        fish_path(df)

        print(mean_velocity(df))
        # tempo à supreficie (1cm)
        surf_time = df[df['yy_mm'] < 10.0]['yy_mm'].count()  # [df["yy"] > 200.0].count()
        txt +="\nsurface time (s): " + str(surf_time * period)

        # Tempo em que esta em cima ou em baixo
        upper = df[df["yy_mm"] <= 35.0]['yy_mm'].count()
        down = df[df["yy_mm"] > 35.0]['yy_mm'].count()
        print("down time (s)", down * period, " upper time (s)", upper * period)

        if (WRITE):
            fp = cleaner.path +  cleaner.folder + cleaner.folder + "output.txt"
            f = open(fp, "w")
            txt += "\ndown time (s): " + str(down * period) + '\n' + "upper time (s): " + str(upper * period)
            f.write(txt)
            f.close()