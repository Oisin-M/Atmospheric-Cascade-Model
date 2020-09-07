from constants import *

def sample_d():
    zeta=np.random.random()
    return lambda_r*np.log(2)*-1*np.log(zeta)

def interact(logs, stack, particle, last_id, d):

    if particle[2]/2<crit:
        logs.append([last_id+1, "electron", particle[2]/2, particle[3]+d])
        logs.append([last_id+2, "positron", particle[2]/2, particle[3]+d])
    else:
        stack.append([last_id+1, "electron", particle[2]/2, particle[3]+d])
        stack.append([last_id+2, "positron", particle[2]/2, particle[3]+d])

        logs.append([last_id+1, "electron", particle[2]/2, particle[3]+d])
        logs.append([last_id+2, "positron", particle[2]/2, particle[3]+d])

    return last_id+2
