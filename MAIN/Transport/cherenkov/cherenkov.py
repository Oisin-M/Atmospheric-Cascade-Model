import numpy as np
from constant import alpha, c
import scipy.integrate as integrate

def cherenkov_emission(particle, distance, n, lambda_0, lambda_1):

    gamma = particle[2]/m
    beta = np.sqrt(1 - gamma**(-2))

    if beta*n>1:
        theta_c=np.arccos(1/(n*beta))

        return 2*np.pi*alpha*distance*integrate.quad(lambda k: k**(-2)*(np.sin(theta_c))**2, lambda_0, lambda_1)[0], theta_c
    else:
        return False, False
