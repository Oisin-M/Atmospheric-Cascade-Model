import particle as pcl
import Transport.transport as tp

ph=pcl.Particle("photon", 100, [1,2,3], [15,20])
print("\n---PHOTON---\n")
for i in range(5):
    ph=tp.move(ph)

el=pcl.Particle("electron", 100, [1,2,3], [15,20])
print("\n---ELECTRON---\n")
for i in range(5):
    el=tp.move(el)
