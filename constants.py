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

#comp by volume is same as comp by mole
atmosphere_comp_by_volume={
'O': 0.7809,
'N': 0.2095,
'Ar': 0.0093
} #from https://en.wikipedia.org/wiki/Atmosphere_of_Earth for now.
#Note: sum is 0.9997

new_percs=np.array([atmosphere_comp_by_volume['O']*2,
                    atmosphere_comp_by_volume['N']*2,
                    atmosphere_comp_by_volume['Ar']*1])
new_percs*=1/new_percs.sum()

p_is = {
'O': new_percs[0],
'N': new_percs[1],
'Ar': new_percs[2]
}

A_is = {
'O': 15.999,
'N': 14.007,
'Ar': 39.948
}

Z_is = {
'O': 8,
'N': 7,
'Ar': 18
}

new_percs=np.array([p_is['O']*A_is['O'],
                    p_is['N']*A_is['N'],
                    p_is['Ar']*A_is['Ar']])
new_percs*=1/new_percs.sum()

rho_is = {
'O': new_percs[0],
'N': new_percs[1],
'Ar': new_percs[2]
}

I_adj_is = {
'O': 95,
'N': 82,
'Ar': 188
} #eV

M = (np.array(list(p_is.values()))*np.array(list(A_is.values()))).sum()
C_M = (np.array(list(p_is.values()))*np.array(list(Z_is.values()))).sum()
n = N_a*rho*C_M/M

I_adj = np.exp( (np.array(list(p_is.values()))*np.array(list(Z_is.values()))*np.log( np.array(list(p_is.values())) )).sum() / C_M)

#values for air
I_adj = 85.7 #eV
a=0.2466
m_s=2.879
x_0=1.742
x_1=4
C=-10.595

Z_S = (np.array(list(p_is.values()))*np.array(list(Z_is.values()))*(np.array(list(Z_is.values()))+eps_MS)).sum()
Z_E = (np.array(list(p_is.values()))*np.array(list(Z_is.values()))*(np.array(list(Z_is.values()))+eps_MS)*np.log(np.array(list(Z_is.values()))**(-2/3))).sum()
Z_X = (np.array(list(p_is.values()))*np.array(list(Z_is.values()))*(np.array(list(Z_is.values()))+eps_MS)*np.log(1+3.34*(alpha*np.array(list(Z_is.values())))**2)).sum()

b_c = _6680_*rho*Z_S*np.exp(Z_E/Z_S)/(M*np.exp(Z_X/Z_S))

X_cc = _22pt9_ * np.pi/180 * np.sqrt(rho*Z_S/M)
