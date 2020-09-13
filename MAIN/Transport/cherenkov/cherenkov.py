import numpy as np
from constants import alpha, c, m

def cherenkov_emission(particle, distance, n, lambda_0, lambda_1):

    gamma = particle[2]/m
    beta = np.sqrt(1 - gamma**(-2))

    if beta*n>1:
        theta_c=np.arccos(1/(n*beta))*np.random.randint(2)

        # integrate.quad(lambda k: k**(-2)*(np.sin(theta_c))**2, lambda_0, lambda_1)[0]
        no=2*np.pi*alpha*distance*(np.sin(theta_c))**2*(-1/lambda_1+1/lambda_0)
        print("Cherenkov: ", no, theta_c)
        return no, theta_c
    else:
        return False, False
