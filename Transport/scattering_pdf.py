import numpy as np
import scipy.special as specfunc
import scipy.integrate as integrate
import Transport.pdf_constants as pdf_const

mu=pdf_const.mu
g_2_Norm=pdf_const.g_2_Norm
g_3_Norm=pdf_const.g_3_Norm

def func_to_integrate(n, theta, u, B, X_c):

    return u*specfunc.jv(0, theta*u)*np.exp(-0.25*u**2)*(0.25*u**2*np.log(0.25*u**2))**n

def f_to_the_n(n, theta, B, X_c):

    return 1/np.math.factorial(n)*integrate.quad(lambda x: func_to_integrate(n, theta, x, B, X_c), 0, np.inf)[0]

def alpha_1(lambd, B, X_c):

    if B < lambd:
        return 0
    else:
        return 1-lambd/B

def alpha_2(lambd, B, X_c):

    return 1-mu*g_2_Norm/B

def alpha_3(lambd, B, X_c):

    return 1-g_3_Norm/(2*mu**2*B)

def get_alphas(lambd, B, X_c):

    return np.array([alpha_1(lambd, B, X_c), alpha_2(lambd, B, X_c), alpha_3(lambd, B, X_c)])

def f_1(theta, lambd, B, X_c):

    return 2*np.exp(-theta**2)*theta

def f_2(theta, lambd, B, X_c):

    return 1/mu

def f_3(theta, lambd, B, X_c):

    return 2*mu**2*theta**(-3)

def f_eta_3(eta, lambd, B, X_c):

    return 2*mu**2*eta

def g_1(theta, lambd, B, X_c):

    return 1

def g_2(theta, lambd, B, X_c):

    return theta/g_2_Norm * (lambd*f_to_the_n(0, theta, B, X_c)+f_to_the_n(1, theta, B, X_c)+f_to_the_n(2, theta, B, X_c)/B)

def g_3(theta, lambd, B, X_c):
    # print("g3")
    # print("theta", theta)
    # print("lambd", lambd)
    # print("B", B)
    # print("X_c", X_c)
    return theta**4/g_3_Norm * (lambd*f_to_the_n(0, theta, B, X_c)+f_to_the_n(1, theta, B, X_c)+f_to_the_n(2, theta, B, X_c)/B)

def g_eta_3(eta, lambd, B, X_c):
    theta=1/eta
    return eta**(-4)/g_3_Norm *(lambd*f_to_the_n(0, theta, B, X_c)+f_to_the_n(1, theta, B, X_c)+f_to_the_n(2, theta, B, X_c)/B)

def theta_to_Theta(theta, B, X_c):

    return theta*X_c*np.sqrt(B)

def sample_f1():
    # print("--- sampling f1")
    return np.sqrt(-np.log(np.random.random()))

def sample_f2():
    # print("--- sampling f2")
    return np.random.random()

def sample_f_eta_3():
    return np.max([np.random.random(), np.random.random()])

def sample_f3(lambd, B, X_c):
    # print("--- sampling f3")
    eta = sample_f_eta_3()
    # print("eta", eta)
    zeta_3 = np.random.random()
    # print("zeta_3", zeta_3)
    #
    # print("comp", g_eta_3(eta, lambd, B, X_c))

    if zeta_3 < g_eta_3(eta, lambd, B, X_c):
        # print("theta", 1/eta)
        return 1/eta
    else:
        return sample_f3(lambd, B, X_c)
