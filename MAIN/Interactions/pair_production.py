from constants import *
from .secondary_energy.pair import sample_secondary_energy

def sample_d():
    zeta=np.random.random()
    return lambda_r*np.log(2)*-1*np.log(zeta)

def interact(logs, stack, particle, last_id):

    logs.append(particle)

    theta=particle[6]+m/particle[2]*np.random.randint(2)
    phi=np.random.random()*2*np.pi

    x=particle[3]
    y=particle[4]
    z=particle[5]

    E_neg_checked = pair_pdf.sample_secondary_energy(particle[2])
    E_plus_checked = particle[2] - E_neg_checked

    if particle[2]/2<crit:
        # logs.append([last_id+1, "electron", particle[2]/2, z, y, z, theta, phi])
        # logs.append([last_id+2, "positron", particle[2]/2, z, y, z, theta, 2*np.pi-phi])
        pass
    else:
        stack.append([last_id+1, "electron", E_neg_checked, z, y, z, theta, phi, np.nan])
        stack.append([last_id+2, "positron", E_plus_checked, z, y, z, theta, 2*np.pi-phi, np.nan])

        logs.append([last_id+1, "electron", E_neg_checked, z, y, z, theta, phi, np.nan])
        logs.append([last_id+2, "positron", E_plus_checked, z, y, z, theta, 2*np.pi-phi, np.nan])

    return logs, stack, last_id+2
