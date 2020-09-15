import constants as const
import scipy.optimize as opt
import numpy as np

lambd = 2
mu = 1
g_2_Norm = 1.8
g_3_Norm = 4.05

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

def get_B(particle, t):
    gamma = particle[2]/const.m
    beta = np.sqrt(1 - gamma**(-2))
    b_c = const.b_c
    omega_0 = b_c*t/(beta**2)
    b = np.log(omega_0)

    if b <= 2 - np.log(2):
        return 2/(2-np.log(2)) * b
    else:
        ans = opt.fsolve(lambda x: x-np.log(x)-b, 2)
        return ans[ans>=1][0]

def get_X_c(particle, t):
    gamma = particle[2]/const.m
    beta = np.sqrt(1 - gamma**(-2))
    X_cc = const.X_cc
    E_MS = particle[2]

    return X_cc*np.sqrt(t)/(E_MS*beta**2)

def find_phi(particle):

    return np.random.random()*2*np.pi #completely random

def find_Theta(particle, t, lambd=lambd):
    # print("Finding Theta")

    B = get_B(particle, t)
    X_c = get_X_c(particle, t)

    zeta_1 = np.random.random()
    zeta_3 = np.random.random()
    alphas = get_alphas(lambd, B, X_c)

    if alphas[0]+alphas[1] < zeta_1 * alphas.sum():
        #i=3
        theta = sample_f3(lambd, B, X_c)
        # print("THETA", theta)
        if zeta_3 < g_3(theta, lambd, B, X_c):
            return theta
        else:
            return find_Theta(particle, t, lambd)
    elif alphas[0] < zeta_1 * alphas.sum():
        #i=2
        theta = sample_f2()
        if zeta_3 < g_2(theta, lambd, B, X_c):
            return theta
        else:
            return find_Theta(particle, t, lambd)
    else:
        #i=1
        theta = sample_f1()
        if zeta_3 < g_1(theta, lambd, B, X_c):
            return theta
        else:
            return find_Theta(particle, t, lambd)
