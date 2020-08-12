import constants as const
import numpy as np
import scipy.integrate as integrate

def E_neg(k, E_plus):

    return k-E_plus

def Delta(k_checked, E_plus_checked):

    E_neg_checked = E_neg(k_checked, E_plus_checked)

    return k_checked*const.m/(2*E_plus_checked*E_neg_checked)

def delta(Z, Delta):

    return 272*Z**(-1/3)*Delta

def delta_max(Z, k_checked):

    if k_checked>50:
        return np.exp((21.12-4/3*np.log(Z)-4*const.f_c(Z))/4.184)-0.952
    else:
        return np.exp((21.12-4/3*np.log(Z))/4.184)-0.952

def phi_1(delta):

    if delta<=1:
        return 20.867-3.242*delta+0.625*delta**2
    else:
        return 21.12-4.184*np.log(delta+0.952)

def phi_2(delta):

    if delta<=1:
        return 20.029-1.93*delta+0.086*delta**2
    else:
        return 21.12-4.184*np.log(delta+0.952)

def a(Z):

    return const.alpha*Z

def f_c(Z):

    a_ = a(Z)
    return a_**2*(1/(1+a_**2)+0.20206-0.0369*a_**2+0.0083*a_**4-0.002*a_**6)

def L_prime(Z):

    if Z==1:
        return 6.144
    elif Z==2:
        return 5.621
    elif Z==3:
        return 5.805
    elif Z==4:
        return 5.924
    else:
        return np.log(1194*Z**(-2/3))

def L(Z):

    if Z==1:
        return 5.31
    elif Z==2:
        return 4.79
    elif Z==3:
        return 4.74
    elif Z==4:
        return 4.71
    else:
        return np.log(184.15*Z**(-1/3))

def xi(Z):

    return L_prime(Z)/(L(Z)-f_c(Z))

def A_p_prime(Z, k_checked):

    return 1

def domega_dEpluschecked(Z, k_checked, E_plus_checked):

    const_factor = (A_p_prime(Z, k_checked)*const.r_0**2*const.alpha*Z*(Z+xi(Z)))/k_checked**3
    E_neg_checked = E_neg(k_checked, E_plus_checked)
    Delta_ = Delta(k_checked, E_plus_checked)
    delta_ = delta(Z, Delta_)

    # think zeroing is just for bremsstrahlung
    # if delta_>delta_max(Z, k_checked):
    #     print("ZEROED")
    #     return 0

    if k_checked>50:
        first_term = (E_plus_checked**2 + E_neg_checked**2)*(phi_1(delta_)-4/3*np.log(Z)-4*f_c(Z))
        second_term = 2/3*E_plus_checked*E_neg_checked*(phi_2(delta_)-4/3*np.log(Z)-4*f_c(Z))
    else:
        first_term = (E_plus_checked**2 + E_neg_checked**2)*(phi_1(delta_)-4/3*np.log(Z))
        second_term = 2/3*E_plus_checked*E_neg_checked*(phi_2(delta_)-4/3*np.log(Z))

    return const_factor*(first_term-second_term)

def dSigma_dEpluschecked(k_checked, E_plus_checked):

    domega_dEpluses=np.array(list(map(lambda z: domega_dEpluschecked(z, k_checked, E_plus_checked), const.Z_is)))

    return const.N_a*const.rho/const.M*((const.p_is*domega_dEpluses).sum())

def get_total_macro_cross_section(particle):

    k_checked = particle.energy

    return integrate.quad(lambda x: dSigma_dEpluschecked(k_checked, x), const.AE, k_checked - const.m)[0]
