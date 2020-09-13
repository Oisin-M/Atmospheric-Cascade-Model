import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from constants import E_0, X_crit
import Interactions.bremsstrahlung as brem
import Interactions.pair_production as pair
import Transport.charged as charged
import Transport.photon as photon

cols=["id","name", "energy", "x", "y", "z", "theta", "phi", "count"] #want this to become ["id","name", "energy", "position", "direction"]
primary=[1, "photon", E_0, 0, 0, 0, 0, 0, np.nan]
stack=[primary]

logs=[primary]

last_id=1

d_init=37.15*np.log(2)

while len(stack)>0:
    particle=stack[0]
    print(len(stack))
    print(particle)
    stack=stack[1:]
    print("d_init: ", d_init)

    if particle[1]=="photon":
        particle=photon.move(particle)
        logs, stack, last_id=pair.interact(logs, stack, particle, last_id)
    else:
        particle, interact, cherenkov=charged.move(particle)
        logs, stack, last_id=brem.interact(logs, stack, particle, last_id, interact, cherenkov)

print(last_id)

df=pd.DataFrame(data=logs, columns=cols)

df["d"] = np.linalg.norm(df[["x", "y", "z"]], axis=1)
# df['d']=df['z']

df.to_excel("./output.xlsx", index=False)

table=pd.pivot_table(df, values="id", index="d", aggfunc="count")

#binned=pd.cut(df['d'], bins=10).value_counts().sort_index()

fig,ax=plt.subplots() #figsize=(14,14)
n, bins, patches=ax.hist(df['d'], np.array(list(range(22)))*d_init)
ax.plot(np.ones(100)*X_crit, np.linspace(0,n.max(), 100), 'r--', label="Critical Distance")
ax.set_title("Particle Shower")
ax.set_xlabel("Distance Travelled (cm)")
ax.set_ylabel("Particle Count")
plt.legend()
plt.show()
