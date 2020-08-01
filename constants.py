import numpy as np

#from https://en.wikipedia.org/wiki/Density_of_air for now
rho = 1.225 * 10**3/(100**3) #g/cm^3

AE = 1 #charged particles energy cut-off
AP = 0.1 #photon

eps_MS = 0 #fudge factor, ignoring since value not given

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
_22pt9_ = 22.696
_6680_ = 6702.33
N_e = 3 #approximating that air has 3 elements only: O, N & Ar

T_E=AE-m #charged particles energy cut-off

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

new_percs=p_is*A_is
new_percs*=1/new_percs.sum()

rho_is=new_percs

I_adj_is=np.array([95, 82, 188]) #eV

M = (p_is*A_is).sum()
C_M = (p_is*Z_is).sum()
n = N_a*rho*C_M/M

I_adj = np.exp( (p_is*Z_is*np.log( p_is )).sum() / C_M)

#values for air
I_adj = 85.7 #eV
a=0.2466
m_s=2.879
x_0=1.742
x_1=4
C=-10.595

Z_S = (p_is*Z_is*(Z_is+eps_MS)).sum()
Z_E = (p_is*Z_is*(Z_is+eps_MS)*np.log(Z_is**(-2/3))).sum()
Z_X = (p_is*Z_is*(Z_is+eps_MS)*np.log(1+3.34*(alpha*Z_is)**2)).sum()

b_c = _6680_*rho*Z_S*np.exp(Z_E/Z_S)/(M*np.exp(Z_X/Z_S))

X_cc = _22pt9_ * np.pi/180 * np.sqrt(rho*Z_S/M)
