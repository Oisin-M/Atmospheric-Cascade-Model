from constants import *

def sample_d():
    zeta=np.random.random()
    return lambda_r*np.log(2)*-1*np.log(zeta)

def move(particle):

    d=sample_d()

    x=particle[3]+d*np.sin(particle[6])*np.cos(particle[7])
    y=particle[4]+d*np.sin(particle[6])*np.sin(particle[7])
    z=particle[5]+d*np.cos(particle[7])

    return x, y, z
