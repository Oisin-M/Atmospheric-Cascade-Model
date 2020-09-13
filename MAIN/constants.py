import numpy as np

#from https://en.wikipedia.org/wiki/Density_of_air for now
rho = 1.225 * 10**3/(100**3) #g/cm^3

lambda_0=529*10**-9

lambda_1=600*10**-9

def rho_func(h):

    return 1 #just for now

def n_func(h1,h2):

    return 1 + 0.000283*(rho_func(h2)/rho_func(h1))

eps_MS = 0 #fudge factor, ignoring since value not given

lambda_r=37.15

E_0=30*10**3 #500*10**3
crit=22.4 #85
AE=22.4
AP=22.4

X_crit = lambda_r*np.log(E_0/crit)

# EGS4 CONSTANTS
c = 2.997925*10**10 #cm/s
m_e = 9.1091*10**(-28) #g
h_bar = 1.0545*10**(-27) #erg-sec
h = h_bar*2*np.pi
e_cgs = 4.80298*10**(-10) #esu
e_mks = 1.6021*10**(-19) #C
N_a = 6.02252*10**(23) #mole^-1
raddeg = 180/np.pi
alpha = (e_cgs**2)/(h_bar*c)
erg_mev = e_mks*10**(13) #ergs
r_0 = (e_cgs**2)/(m_e*c**2)
m = (m_e*c**2)/(erg_mev)

T_E=AE-m #charged particles energy cut-off

#values for air
I_adj = 85.7 #eV
a_const=0.2466
m_s=2.879
x_0=1.742
x_1=4
C=-10.595

elements=['O', 'N', 'Ar']

#comp by volume is same as comp by mole
atmosphere_comp_by_volume=np.array([0.7809, 0.2095, 0.0093]) #from https://en.wikipedia.org/wiki/Atmosphere_of_Earth for now.
#Note: sum is 0.9997

new_percs=np.array([atmosphere_comp_by_volume[0]*2,
                    atmosphere_comp_by_volume[1]*2,
                    atmosphere_comp_by_volume[2]*1])
new_percs*=1/new_percs.sum()

p_is=new_percs

A_is=np.array([15.999, 14.007, 39.948])

Z_is=np.array([8, 7, 18])

M = (p_is*A_is).sum()
C_M = (p_is*Z_is).sum()
n = N_a*rho*C_M/M

#from https://www-physics.lbl.gov/~gilg/PixelUpgradeMechanicsCooling/Material/Radiationlength.pdf
X_0s=np.array([34.2, 38, 16.65])
X_0=37.1

E_checked_s = 21.2
eps_P_max = 0.3
