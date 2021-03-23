import numpy

print("A stochastic simulation of the kinetics behind our 4-enzyme system.")
import matplotlib.pyplot as plt
import random as rand
import math as math
import numpy as np

fig = plt.figure(figsize=(20, 10))

# Enzyme constants
k1 = 5487804  #
k2 = 37384500
k3 = 218796000
k4 = 143244000
kneg1 = 25216
kneg2 = 2688.97
kneg3 = 19670.9
kneg4: float = 85856.2
ka = 27.0
kb = 2.71
kc = 20.79
kd = 90

# propensities
avogadros = 6.022 * (10 ** 23)
v_number = 1.66058 * (10 ** (-21))  # ask Pat to clarify
C1 = k1 / (avogadros * v_number)
C2 = kneg1
C3 = ka
C4 = k2 / (avogadros * v_number)
C5 = kneg2
C6 = kb
C7 = k3 / (avogadros * v_number)
C8 = kneg3
C9 = kc
C10 = k4 / (avogadros * v_number)
C11 = kneg4
C12 = kd

# initial amts
# Substrates
S1 = 100  # PET
S2 = 0  # Terepthalic Acid
S3 = 0  # Dihydroxycyclohexa...dicarboxylate
S4 = 0  # Protocatechuate
S5 = 0  # Catechol
total_molecs = S1 + S2 + S3 + S4 + S5
# Enzymes
E1 = 10  # PETase
E2 = 50  # Terpthalate dioxygenase
E3 = 10  # ...dehydrogenase
E4 = 10  # Protocatechuate decarboxylase
# Enzyme substrate complexes
ES1 = 0
ES2 = 0
ES3 = 0
ES4 = 0
# lists for progression of numbers of molecules over numstep, starting with value inside brackets
numS1 = [S1]
numS2 = [S2]
numS3 = [S3]
numS4 = [S4]
numS5 = [S5]

numE1 = [E1]
numE2 = [E2]
numE3 = [E3]
numE4 = [E4]

numES1 = [ES1]
numES2 = [ES2]
numES3 = [ES3]
numES4 = [ES4]

time = 0
MCTime = [0, ]
MCCounter = 0
numstep = 1000

while MCCounter < numstep:

    P1 = C1 * S1 * E1
    P2 = C2 * ES1
    P3 = C3 * ES1
    P4 = C4 * S2 * E2
    P5 = C5 * ES2
    P6 = C6 * ES2
    P7 = C7 * S3 * E3
    P8 = C8 * ES3
    P9 = C9 * ES3
    P10 = C10 * S4 * E4
    P11 = C11 * ES4
    P12 = C12 * ES4
    P_total = sum([P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12])

    r1 = rand.uniform(0, 1.0)
    r2 = rand.uniform(0, 1.0)
    try:
        constant = 1 / P_total
    except RuntimeWarning:
        constant = 0
    constant = 1 / P_total
    dt = constant * (math.log(1 / r1))
    time += dt
    MCTime.append(time)
    MuObject = r2 * P_total

    if MuObject <= P1:
        rxn = 1
    if P1 < MuObject <= np.sum([P1, P2]):
        rxn = 2
    if np.sum([P1, P2]) < MuObject <= np.sum([P1, P2, P3]):
        rxn = 3
    if np.sum([P1, P2, P3]) < MuObject <= np.sum([P1, P2, P3, P4]):
        rxn = 4
    if np.sum([P1, P2, P3, P4]) < MuObject <= np.sum([P1, P2, P3, P4, P5]):
        rxn = 5
    if np.sum([P1, P2, P3, P4, P5]) < MuObject <= np.sum([P1, P2, P3, P4, P5, P6]):
        rxn = 6
    if np.sum([P1, P2, P3, P4, P5, P6]) < MuObject <= np.sum([P1, P2, P3, P4, P5, P6, P7]):
        rxn = 7
    if np.sum([P1, P2, P3, P4, P5, P6, P7]) < MuObject <= np.sum([P1, P2, P3, P4, P5, P6, P7, P8]):
        rxn = 8
    if np.sum([P1, P2, P3, P4, P5, P6, P7, P8]) < MuObject <= np.sum([P1, P2, P3, P4, P5, P6, P7, P8, P9]):
        rxn = 9
    if np.sum([P1, P2, P3, P4, P5, P6, P7, P8, P9]) < MuObject <= np.sum([P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]):
        rxn = 10
    if np.sum([P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]) < MuObject <= np.sum(
            [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11]):
        rxn = 11
    if np.sum([P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11]) < MuObject <= np.sum(
            [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12]):
        rxn = 12

    if rxn == 1:
        E1 -= 1
        S1 -= 1
        ES1 += 1
    elif rxn == 2:
        E1 += 1
        S1 += 1
        ES1 -= 1
    elif rxn == 3:
        E1 += 1
        S2 += 1
        ES1 -= 1
    elif rxn == 4:
        E2 -= 1
        S2 -= 1
        ES2 += 1
    elif rxn == 5:
        E2 += 1
        S2 += 1
        ES2 -= 1
    elif rxn == 6:
        E3 += 1
        S2 += 1
        ES2 -= 1
    elif rxn == 7:
        E3 -= 1
        S3 -= 1
        ES3 += 1
    elif rxn == 8:
        E3 += 1
        S3 += 1
        ES3 -= 1
    elif rxn == 9:
        E3 += 1
        S4 += 1
        ES3 -= 1
    elif rxn == 10:
        E4 -= 1
        S4 -= 1
        ES4 += 1
    elif rxn == 11:
        E4 += 1
        S4 += 1
        ES4 -= 1
    elif rxn == 12:
        E4 += 1
        S5 += 1
        ES4 -= 1

    numE1.append(E1)
    numE2.append(E2)
    numE3.append(E3)
    numE4.append(E4)
    numES1.append(ES1)
    numES2.append(ES2)
    numES3.append(ES3)
    numES4.append(ES4)
    numS1.append(S1)
    numS2.append(S2)
    numS3.append(S3)
    numS4.append(S4)
    numS5.append(S5)

    MCCounter += 1

ax = plt.subplot()
plt.plot(MCTime, numS1, color='#a1490b', label='PET')
plt.plot(MCTime, numS2, color='blue', label='S2')
plt.plot(MCTime, numS3, color='#b08f0c', label='S3')
plt.plot(MCTime, numS4, color='#6f0ca8', label='S4')
plt.plot(MCTime, numS5, color='#12e6de', label='catechol')
plt.ylabel('Molecules')
plt.xlabel('Time(s)')
plt.title('PET degradation to catechol over time')
plt.legend()
ax.set_facecolor('#e3e3e3')

numpy.seterr(all='raise')
