import particle as pcl
import Transport.transport as tp
import constants as const
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

el=pcl.Particle("electron", 10**6, [1,2,3], [15,20])
ph=pcl.Particle("photon", 10**3, [1,2,3], [15,20])

photon_times = [0]
electron_times = [0]
photon_dx = [0]
electron_dx = [0]
photon_positions = [list(ph.position)]
electron_positions = [list(el.position)]
electron_energies = [el.energy]

print("\n---PHOTON---\n")
for i in range(5):
    ph, dx, interaction_bool=tp.move(ph)
    print("INTERACTION (not handled by code yet)")
    photon_positions.append(list(ph.position))
    photon_dx.append(photon_dx[-1]+dx)
    photon_times.append(photon_times[-1]+dx/const.c)


print("\n---ELECTRON---\n")
for i in range(20):
    el, dx, interaction_bool=tp.move(el)
    if interaction_bool:
        print("INTERACTION (not handled by code yet)")
    else:
        print("NO INTERACTION")
    electron_positions.append(list(el.position))
    electron_energies.append(el.energy)
    electron_dx.append(electron_dx[-1]+dx)
    gamma = el.energy/const.m
    v = const.c*np.sqrt(1-(gamma)**(-2))
    electron_times.append(electron_times[-1]+dx/v)

print("ARRAYS")
print("photon_times")
print(photon_times)
print("photon_dx")
print(photon_dx)
print("photon_positions")
print(photon_positions)
print("electron_times")
print(electron_times)
print("electron_dx")
print(electron_dx)
print("electron_positions")
print(electron_positions)
print("electron_energies")
print(electron_energies)


fig = plt.figure(figsize=(10,10))
ax = plt.axes(projection='3d')
ax.view_init(azim=45, elev=0)
ax.set_title("Electron Position", fontsize=25)
ax.set_xlabel("X (cm)", fontsize=15)
ax.set_ylabel("Y (cm)", fontsize=15)
ax.set_zlabel("Z (cm)", fontsize=15)

zdata = list(map(lambda x: x[2], electron_positions))
xdata = list(map(lambda x: x[0], electron_positions))
ydata = list(map(lambda x: x[1], electron_positions))
ax.scatter3D([xdata[0]], [ydata[0]], [zdata[0]], c='y', s=50)
ax.scatter3D(xdata[1:], ydata[1:], zdata[1:], c='r', s=50)
ax.plot3D(xdata, ydata, zdata, c='b')

plt.show()
