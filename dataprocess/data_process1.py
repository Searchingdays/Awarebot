
# taking the data out of text file to python 

# for analysing the data

from pathlib import Path

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

from sklearn.impute import SimpleImputer

arr = []

fig, ax = plt.subplots(nrows=2, ncols=2, sharex=False, sharey=False)

file_path = Path("../rawdata/arduino_output1.txt")

data = np.genfromtxt(file_path, usecols=[0,1,2,3,4], delimiter='\t', skip_header=1, missing_values="nan")

# column 0 has temperature data, 1 has humidity, 2 has sound, 3 has magnetic sensor

print(data.shape)

data = pd.DataFrame(data)

data.drop(data.index[1191:], inplace=True)

data.drop(data.index[0:115])

imputer = SimpleImputer(strategy="mean")

temp = np.reshape(data[0], newshape=(-1,1))

temp = imputer.fit_transform(temp)

sound = np.reshape(data[2], newshape=(-1,1))

mag = data[3]

mag = (mag*5)/1023   # analog value to volts

mag = mag - 3.145   # difference from 6.29V/2

mag = mag* 1000      # in mV

mag = mag/1.7      # the column is now in gauss

sound = imputer.fit_transform(sound)

#print(sound)

print(mag.mean())

x = np.linspace(0,10,len(sound))

print(mag.mode())

#data[2].plot.box()

ax[0,0].plot(sound)

#ax[0,1].plot(temp)

#ax[0,1].set_xlabel("reading")

#ax[0,1].set_ylabel("temperature(C)")

ax[1,0].plot(mag)

ax[1,0].set_xlabel("reading")

ax[1,0].set_ylabel("Magnetic Field (gauss)")

## combining all three columns in one plot to identify the parts where

# z score calculation 

ax[0,0].plot(x, [sound.mean()]*len(x), color = "orange")

ax[0,0].plot(x, [sound.std()]*len(x), color = "purple")

#sound_z = (sound - sound.mean() ) / sound.std()


sound_clear = sound[(sound.mean() - sound < 0)]   # cleared some of the outliers

ax[1,1].plot(sound_clear)

print(len(sound_clear))

#calculate moving average for sound

s =0 

for i in range(20):
    arr.append(sound_clear[i])
    s = s+ arr[i]

arr.pop(0)

mavg = [s/20]

s=0

for i in range(21,len(sound_clear)):
    arr.pop(0)

    arr.append(sound_clear[i])

    mavg.append(sum(arr)/ 20)

    s =0 

print(len(mavg))

ax[1,1].plot(mavg, color= "orange")








plt.show()


