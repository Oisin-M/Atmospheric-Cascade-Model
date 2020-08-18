import numpy as np
import pandas as pd

import json

import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

c = 2.997925*10**10 #cm/s
m_e = 9.1091*10**(-28) #g
e_mks = 1.6021*10**(-19) #C
erg_mev = e_mks*10**(13) #ergs
m = (m_e*c**2)/(erg_mev)

size=1/2

pd.set_option('display.max_rows', 999)
pd.set_option('display.max_columns', 999)

# np.sqrt(1-df['energy']/m**(-2))*c

df=pd.read_excel("./OUTPUT/data.xlsx")
print(df.head())
# df['vel']=np.where(df['particle']=="photon", c, c*np.sqrt(1-(df['energy']/m)**(-2)))
# print(df)

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.view_init(azim=45, elev=0)
ax.set_title("Particle Positions", fontsize=25)
ax.set_xlabel("X (cm)", fontsize=15)
ax.set_ylabel("Y (cm)", fontsize=15)
ax.set_zlabel("Z (cm)", fontsize=15)

for id in np.unique(df['id']):
    df_id = df[df['id']==id]

    df_ph = df_id

    zdata_ph = np.array(df_ph['position_z']).astype('float')
    xdata_ph = np.array(df_ph['position_x']).astype('float')
    ydata_ph = np.array(df_ph['position_y']).astype('float')

    if list(df_ph['particle'])[0]=="photon":
        col="y"
    elif list(df_ph['particle'])[0]=="electron":
        col="r"
    else:
        col="b"
    ax.scatter3D([xdata_ph[0]], [ydata_ph[0]], [zdata_ph[0]], c=col, s=size)
    if len(xdata_ph)>1:
        ax.scatter3D(xdata_ph[1:], ydata_ph[1:], zdata_ph[1:], c=col, s=size)
        ax.plot3D(xdata_ph, ydata_ph, zdata_ph, c=col)

plt.show()

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.view_init(azim=45, elev=0)
ax.set_title("Photon Positions", fontsize=25)
ax.set_xlabel("X (cm)", fontsize=15)
ax.set_ylabel("Y (cm)", fontsize=15)
ax.set_zlabel("Z (cm)", fontsize=15)


for id in np.unique(df[df['particle']=="photon"]['id']):
    df_id = df[df['id']==id]

    df_ph = df_id

    zdata_ph = np.array(df_ph['position_z']).astype('float')
    xdata_ph = np.array(df_ph['position_x']).astype('float')
    ydata_ph = np.array(df_ph['position_y']).astype('float')

    ax.scatter3D([xdata_ph[0]], [ydata_ph[0]], [zdata_ph[0]], c='g', s=size)
    if len(xdata_ph)>1:
        ax.scatter3D(xdata_ph[1:], ydata_ph[1:], zdata_ph[1:], c="y", s=size)
        ax.plot3D(xdata_ph, ydata_ph, zdata_ph, c="y")

plt.show()

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.view_init(azim=45, elev=0)
ax.set_title("Electron Positions", fontsize=25)
ax.set_xlabel("X (cm)", fontsize=15)
ax.set_ylabel("Y (cm)", fontsize=15)
ax.set_zlabel("Z (cm)", fontsize=15)

for id in np.unique(df[df['particle']=="electron"]['id']):
    df_id = df[df['id']==id]

    df_ph = df_id

    zdata_ph = np.array(df_ph['position_z']).astype('float')
    xdata_ph = np.array(df_ph['position_x']).astype('float')
    ydata_ph = np.array(df_ph['position_y']).astype('float')

    ax.scatter3D([xdata_ph[0]], [ydata_ph[0]], [zdata_ph[0]], c='g', s=size)
    if len(xdata_ph)>1:
        ax.scatter3D(xdata_ph[1:], ydata_ph[1:], zdata_ph[1:], c="r", s=size)
        ax.plot3D(xdata_ph, ydata_ph, zdata_ph, c="r")

plt.show()

fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.view_init(azim=45, elev=0)
ax.set_title("Positron Positions", fontsize=25)
ax.set_xlabel("X (cm)", fontsize=15)
ax.set_ylabel("Y (cm)", fontsize=15)
ax.set_zlabel("Z (cm)", fontsize=15)

for id in np.unique(df[df['particle']=="positron"]['id']):
    df_id = df[df['id']==id]

    df_ph = df_id

    zdata_ph = np.array(df_ph['position_z']).astype('float')
    xdata_ph = np.array(df_ph['position_x']).astype('float')
    ydata_ph = np.array(df_ph['position_y']).astype('float')

    ax.scatter3D([xdata_ph[0]], [ydata_ph[0]], [zdata_ph[0]], c='g', s=size)
    if len(xdata_ph)>1:
        ax.scatter3D(xdata_ph[1:], ydata_ph[1:], zdata_ph[1:], c="b", s=size)
        ax.plot3D(xdata_ph, ydata_ph, zdata_ph, c="b")

plt.show()
