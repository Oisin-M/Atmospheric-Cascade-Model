from constants import *

def sample_d():
    zeta=np.random.random()
    return lambda_r*np.log(2)*-1*np.log(zeta)

def interact(logs, stack, particle, last_id, x, y, z):

    theta=particle[6]+m/particle[2]
    phi=np.random.random()*2*np.pi

    if particle[2]/2<crit:
        logs.append([last_id+1, "electron", particle[2]/2, z, y, z, theta, phi])
        logs.append([last_id+2, "positron", particle[2]/2, z, y, z, theta, 2*np.pi-phi])
    else:
        stack.append([last_id+1, "electron", particle[2]/2, z, y, z, theta, phi])
        stack.append([last_id+2, "positron", particle[2]/2, z, y, z, theta, 2*np.pi-phi])

        logs.append([last_id+1, "electron", particle[2]/2, z, y, z, theta, phi])
        logs.append([last_id+2, "positron", particle[2]/2, z, y, z, theta, 2*np.pi-phi])

    return logs, stack, last_id+2
