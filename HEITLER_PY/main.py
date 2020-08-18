import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lambda_r=37.15
d=lambda_r*np.log(2)

E_0=30*10**3
crit=85

X_crit = lambda_r*np.log(E_0/crit)

cols=["id","name", "energy", "d"]
primary=[1, "photon", E_0, 0]
stack=[primary]

logs=[primary]

last_id=1

while len(stack)>0:
    particle=stack[0]
    print(len(stack))
    print(particle)
    stack=stack[1:]
    if particle[1]=="photon":
        if particle[2]/2<crit:
            logs.append([last_id+1, "electron", particle[2]/2, particle[3]+d])
            logs.append([last_id+2, "positron", particle[2]/2, particle[3]+d])
        else:
            stack.append([last_id+1, "electron", particle[2]/2, particle[3]+d])
            stack.append([last_id+2, "positron", particle[2]/2, particle[3]+d])

            logs.append([last_id+1, "electron", particle[2]/2, particle[3]+d])
            logs.append([last_id+2, "positron", particle[2]/2, particle[3]+d])
            last_id+=2
    else:
        if particle[2]/4<crit:
            logs.append([particle[0], particle[1], particle[2]/2, particle[3]+d])
            logs.append([particle[0], "photon", particle[2]/2, particle[3]+d])
        else:
            stack.append([particle[0], particle[1], particle[2]/2, particle[3]+d])
            stack.append([particle[0], "photon", particle[2]/2, particle[3]+d])

            logs.append([particle[0], particle[1], particle[2]/2, particle[3]+d])
            logs.append([particle[0], "photon", particle[2]/2, particle[3]+d])

print(X_crit)

df=pd.DataFrame(data=logs, columns=cols)

df.to_excel("./output.xlsx", index=False)

table=pd.pivot_table(df, values="id", index="d", aggfunc="count")

plt.plot(table.index, table, 'ro')
plt.plot(table.index, table, 'b-')
plt.plot(np.ones(100)*X_crit, np.linspace(0,np.max(table), 100), 'g', label="Critical Distance")
plt.title("Particle Shower")
plt.xlabel("Distance Travelled (cm)")
plt.ylabel("Particle Count")
plt.legend()
plt.show()
