import numpy as np
import Transport.scattering_pdf as pdf
import Transport.pdf_constants as pdf_const

def find_phi(particle):

    return np.random.random()*2*np.pi #completely random

def find_Theta(particle, t, lambd):
    # print("Finding Theta")

    B = pdf_const.get_B(particle, t)
    X_c = pdf_const.get_X_c(particle, t)

    zeta_1 = np.random.random()
    zeta_3 = np.random.random()
    alphas = pdf.get_alphas(lambd, B, X_c)

    if alphas[0]+alphas[1] < zeta_1 * alphas.sum():
        #i=3
        theta = pdf.sample_f3(lambd, B, X_c)
        # print("THETA", theta)
        if zeta_3 < pdf.g_3(theta, lambd, B, X_c):
            return theta
        else:
            return find_Theta(particle, t, lambd)
    elif alphas[0] < zeta_1 * alphas.sum():
        #i=2
        theta = pdf.sample_f2()
        if zeta_3 < pdf.g_2(theta, lambd, B, X_c):
            return theta
        else:
            return find_Theta(particle, t, lambd)
    else:
        #i=1
        theta = pdf.sample_f1()
        if zeta_3 < pdf.g_1(theta, lambd, B, X_c):
            return theta
        else:
            return find_Theta(particle, t, lambd)
