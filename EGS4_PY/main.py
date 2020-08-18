import particle as pcl
import Interactions.interactions as interact
import Transport.transport as tp
import constants as const
import numpy as np
import pandas as pd



el=pcl.Particle("electron", 10**6, [0,0,0], [15,20])
ph=pcl.Particle("photon", 10**9, [0,0,0], [15,20])

particle=ph

particle_stack=[particle]
print([particle.id, particle.name, particle.energy, particle.position, particle.direction])
pos=particle.position.copy()
rows=[[particle.id, particle.name, particle.energy, pos[0], pos[1], pos[2], particle.direction.copy(), "PRIMARY"]]

i=0
i_max=500

import time
start_time = time.time()

while len(particle_stack)>0:
    i+=1
    print(i)
    particle = particle_stack[0]
    print(particle.name, particle.energy)

    particle_stack = particle_stack[1:]
    # print(particle)
    particle, dx, interaction_bool=tp.move(particle)
    print("MOVE")
    if (particle.energy<const.AE and particle.charge!=0) or (particle.energy<const.AP and particle.charge==0):
        pass
    else:
        pos=particle.position.copy()
        rows.append([particle.id, particle.name, particle.energy, pos[0], pos[1], pos[2], particle.direction.copy(), "MOVE"])

        if interaction_bool:
            if particle.charge==0:
                p1, p2 = interact.pair_production(particle)
                print("--- PAIR PRODUCTION")
                if p1.energy>const.AE:
                    particle_stack.append(p1)
                    pos=p1.position.copy()
                    rows.append([p1.id, p1.name, p1.energy, pos[0], pos[1], pos[2], p1.direction.copy(), "PAIR PRODUCTION"])
                if p2.energy>const.AE:
                    particle_stack.append(p2)
                    pos=p2.position.copy()
                    rows.append([p2.id, p2.name, p2.energy, pos[0], pos[1], pos[2], p2.direction.copy(), "PAIR PRODUCTION"])
            else:
                p1, p2 = interact.bremsstrahlung(particle)
                print("--- BREMSSTRAHLUNG")
                if p1.energy>const.AE:
                    particle_stack.append(p1)
                    pos=p1.position.copy()
                    rows.append([p1.id, p1.name, p1.energy, pos[0], pos[1], pos[2], p1.direction.copy(), "BREMSSTRAHLUNG"])
                if p2.energy>const.AP:
                    particle_stack.append(p2)
                    pos=p2.position.copy()
                    rows.append([p2.id, p2.name, p2.energy, pos[0], pos[1], pos[2], p2.direction.copy(), "BREMSSTRAHLUNG"])

        else:
            print("NO INTERACTION")
            particle_stack.append(particle)

    particle_stack=sorted(particle_stack, key=lambda x: x.energy)

    print(list(map(lambda x: [x.name, x.id, x.energy], particle_stack)))

    el_count=len([n for n in particle_stack if n.name == "electron"])
    pos_count=len([n for n in particle_stack if n.name == "positron"])
    phot_count=len([n for n in particle_stack if n.name == "photon"])
    print("ELECTRONS: {}, POSITRONS: {}, PHOTONS: {}".format(el_count, pos_count, phot_count))
    print("ENERGY LEFT: {}".format(np.array(list(map(lambda x: x.energy, particle_stack))).sum()))

    if i==i_max:
        print("I_MAX REACHED")


df=pd.DataFrame(data=rows, columns=["id", "particle", "energy", "position_x", "position_y", "position_z", "direction", "event"])
# print(rows)
# print(df)
df.to_excel("./OUTPUT/data.xlsx")

energy_left = np.array(list(map(lambda x: x.energy, particle_stack))).sum()
time_elapsed = time.time()-start_time
energy_used_percentage = (10**9-energy_left)/10**9
print("ESTIMATE: {} days".format(time_elapsed/energy_used_percentage * 1/(60*60*24)))

import Plotting.plotting
