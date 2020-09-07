from constants import *

def sample_d():
    zeta=np.random.random()
    return lambda_r*np.log(2)*-1*np.log(zeta)

def interact(logs, stack, particle, last_id, d):

    if particle[2]/2<crit:
        logs.append([particle[0], particle[1], particle[2]/2, particle[3]+d])
        logs.append([particle[0], "photon", particle[2]/2, particle[3]+d])
    else:
        stack.append([particle[0], particle[1], particle[2]/2, particle[3]+d])
        stack.append([last_id+1, "photon", particle[2]/2, particle[3]+d])

        logs.append([particle[0], particle[1], particle[2]/2, particle[3]+d])
        logs.append([last_id+1, "photon", particle[2]/2, particle[3]+d])

    return last_id+1
