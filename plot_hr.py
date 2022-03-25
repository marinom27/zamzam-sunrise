import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import json


SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12
BIGG = 14

plt.rc('font', size=BIGGER_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=BIGG)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title


df = pd.read_json('./data/hrate.json')

var = np.zeros(len(df["value"]))
for i in range(4,len(df["value"])-1):
    min = np.min([df["value"].iloc[j] for j in range(i-4,i+1)])
    max = np.max([df["value"].iloc[j] for j in range(i-4,i+1)])
    var[i] = max-min

df["variability"] = var

mov_av = np.zeros(len(df["value"]))
for i in range(20,len(df["value"])-1):
    mean = np.mean([df["variability"].iloc[j] for j in range(i-20,i+1)])
    mov_av[i]=mean
df["mov_av"] = mov_av


plt.plot(df.iloc[:1079]["date"],df.iloc[:1079]["value"],label="Heart-rate")
plt.plot(df.iloc[:1079]["date"],df.iloc[:1079]["variability"],label="HRV")
plt.plot(df.iloc[:1079]["date"],df.iloc[:1079]["mov_av"],label="MA HRV")
plt.vlines([df["date"].iloc[173],df["date"].iloc[420]],-5,175,color='black')
plt.locator_params(axis='x', numticks=5)
plt.legend()
plt.savefig('morning.png')
plt.show()

plt.plot(df.iloc[1080:]["date"],df.iloc[1080:]["value"],label="Heart-rate")
plt.plot(df.iloc[1080:]["date"],df.iloc[1080:]["variability"],label="HRV")
plt.plot(df.iloc[1080:]["date"],df.iloc[1080:]["mov_av"],label="MA HRV")
plt.vlines([df["date"].iloc[1080],df["date"].iloc[1779]],-5,120,color='black')
plt.locator_params(axis='x', nbins=5)
plt.legend()
plt.savefig('afternoon.png')
plt.show()
