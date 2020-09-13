from constants import *

def sample_d():
    zeta=np.random.random()
    return lambda_r*np.log(2)*-1*np.log(zeta)

def interact(logs, stack, particle, last_id, interact, cherenkov):

    logs.append(particle)
    for cher in cherenkov:
        logs.append(cher)

    if not interact:
        stack.append(particle)
        return logs, stack, last_id

    theta=particle[6]+m/particle[2]*np.random.randint(2)
    phi=np.random.random()*2*np.pi

    x=particle[3]
    y=particle[4]
    z=particle[5]

    if particle[2]/2<crit:
        # logs.append([particle[0], particle[1], particle[2]/2, x, y, z, particle[6], particle[7]])
        # logs.append([last_id+1, "photon", particle[2]/2, x, y, z, theta, phi])
        pass
    else:
        stack.append([particle[0], particle[1], particle[2]/2, z, y, z, particle[6], particle[7], np.nan])
        stack.append([last_id+1, "photon", particle[2]/2, z, y, z, theta, phi, np.nan])

        logs.append([particle[0], particle[1], particle[2]/2, z, y, z, particle[6], particle[7], np.nan])
        logs.append([last_id+1, "photon", particle[2]/2, z, y, z, theta, phi, np.nan])

    return logs, stack, last_id+1
