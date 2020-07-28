import numpy as np
import scipy.special as specfunc
import scipy.integrate as integrate
import Transport.pdf_constants as pdf_const

B = pdf_const.get_B(particle, t)
X_c = pdf_const.get_X_c(particle, t)

mu=pdf_const.mu
g_2_Norm=pdf_const.g_2_Norm
g_3_Norm=pdf_const.g_3_Norm

def func_to_integrate(n, theta, u):

    return u*specfunc.jv(0, theta*u)*np.exp(-0.25*u**2)*(0.25*u**2*np.log(0.25*u**2))**n

def f_to_the_n(n, theta):

    return 1/np.math.factorial(n)*integrate.quad(lambda x: func_to_integrate(n, theta, x), 0, np.inf)[0]

def alpha_1(lambd):

    return 1-lambd/B

def alpha_2(lambd):

    return 1-mu*g_2_Norm/B

def alpha_3(lambd):

    return 1-g_3_Norm/(2*mu**2*B)

def f_1(theta, lambd):

    return 2*np.exp(-theta**2)*theta

def f_2(theta, lambd):

    return 1/mu

def f_3(theta, lambd):

    return 2*mu**2*theta**(-3)

def g_1(theta, lambd):

    return 1

def g_2(theta, lambd):

    return theta/g_2_Norm * (lambd*f_to_the_n(0, theta)+f_to_the_n(1, theta)+f_to_the_n(2, theta)/B)

def g_3(theta, lambd):

    return theta**4/g_3_Norm * (lambd*f_to_the_n(0, theta)+f_to_the_n(1, theta)+f_to_the_n(2, theta)/B)


def theta_to_Theta(theta):

    return theta*X_c*np.sqrt(B)
