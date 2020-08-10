import particle as pcl
import Interactions.interactions as interact
import Transport.transport as tp
import constants as const
import numpy as np
import pandas as pd



el=pcl.Particle("electron", 10**6, [1,2,3], [15,20])
ph=pcl.Particle("photon", 10**3, [1,2,3], [15,20])

particle=el

particle_stack=[particle]
print([particle.id, particle.name, particle.energy, particle.position, particle.direction])
rows=[[particle.id, particle.name, particle.energy, particle.position.copy(), particle.direction.copy(), "PRIMARY"]]

i=0

while len(particle_stack)>0 and i<11:
    i+=1
    particle = particle_stack[0]
    particle_stack = particle_stack[1:]
    print(particle)
    particle, dx, interaction_bool=tp.move(particle)
    print("MOVE")
    if (particle.energy<const.AE and particle.charge!=0) or (particle.energy<const.AP and particle.charge==0):
        pass
    else:
        rows.append([particle.id, particle.name, particle.energy, particle.position.copy(), particle.direction.copy(), "MOVE"])

        if interaction_bool:
            if particle.charge==0:
                p1, p2 = interact.pair_production(particle)
                print("--- PAIR PRODUCTION")
                if p1.energy>const.AE:
                    particle_stack.append(p1)
                    rows.append([p1.id, p1.name, p1.energy, p1.position.copy(), p1.direction.copy(), "PAIR PRODUCTION"])
                if p2.energy>const.AE:
                    particle_stack.append(p2)
                    rows.append([p2.id, p2.name, p2.energy, p2.position.copy(), p2.direction.copy(), "PAIR PRODUCTION"])
            else:
                p1, p2 = interact.bremsstrahlung(particle)
                print("--- BREMSSTRAHLUNG")
                if p1.energy>const.AE:
                    particle_stack.append(p1)
                    rows.append([p1.id, p1.name, p1.energy, p1.position.copy(), p1.direction.copy(), "BREMSSTRAHLUNG"])
                if p2.energy>const.AP:
                    particle_stack.append(p2)
                    rows.append([p2.id, p2.name, p2.energy, p2.position.copy(), p2.direction.copy(), "BREMSSTRAHLUNG"])

        else:
            print("NO INTERACTION")
            particle_stack.append(particle)


        if i==11:
            df=pd.DataFrame(data=rows, columns=["id", "particle", "energy", "position", "direction", "event"])
            print(rows)
            print(df)
            df.to_excel("./OUTPUT/data.xlsx")

    particle_stack=sorted(particle_stack, key=lambda x: x.energy)
    # print("ELECTRONS: ", len([n for n in particle_stack if n.name == "electron"]))
    # print("POSITRONS: ", len([n for n in particle_stack if n.name == "position"]))
    # print("PHOTONS: ", len([n for n in particle_stack if n.name == "photon"]))
