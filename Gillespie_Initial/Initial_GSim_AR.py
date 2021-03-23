print("Hello, world.")
# imports made; may need replication (math, random, mpl)
import matplotlib.pyplot as plt
import random as rand
import math as math

fig = plt.figure(figsize=(20, 10))

e = 0
# Enzyme constants
k1 = 5487804
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

numstep = 100

# initial amts
S1 = 1000  # PET
S2 = 0  # Terepthalic Acid
S3 = 0  # Dihydroxycyclohexa...dicarboxylate
S4 = 0  # Protocatechuate
S5 = 0  # Catechol

E1 = 10  # PETase
E2 = 50  # Terpthalate dioxygenase
E3 = 10  # ...dehydrogenase
E4 = 10  # Protocatechuate decarboxylase
# Enzyme substrate complexes
ES1 = 0
ES2 = 0
ES3 = 0
ES4 = 0

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

H1 = []
H2 = []
H3 = []
H4 = []
H5 = []
H6 = []
H7 = []
H8 = []
H9 = []
H10 = []
H11 = []
H12 = []

A1 = []
A2 = []
A3 = []
A4 = []
A5 = []
A6 = []
A7 = []
A8 = []
A9 = []
A10 = []
A11 = []
A12 = []

A0 = []  # this is new
time = 0
MCTime = [0]  # Hola Michelle this is new
MCCounter = 0  # this is new

# propensities
avocado = 6.022 * (10 ** 23)
v_number = 1.66058 * (10 ** (-21))
C1 = k1 / (avocado * v_number)
C2 = kneg1
C3 = ka
C4 = k2 / (avocado * v_number)
C5 = kneg2
C6 = kb
C7 = k3 / (avocado * v_number)
C8 = kneg3
C9 = kc
C10 = k4 / (avocado * v_number)
C11 = kneg4
C12 = kd

while (e < numstep):


    H1.append(numS1[MCCounter] * numE1[MCCounter])
    H2.append(numES1[MCCounter])
    H3.append(numES1[MCCounter])
    H4.append(numS2[MCCounter] * numE2[MCCounter])
    H5.append(numES2[MCCounter])
    H6.append(numES2[MCCounter])
    H7.append(numS3[MCCounter] * numE3[MCCounter])
    H8.append(numES3[MCCounter])
    H9.append(numES3[MCCounter])
    H10.append(numS4[MCCounter] * numE4[MCCounter])
    H11.append(numES4[MCCounter])
    H12.append(numES4[MCCounter])

    A1.append(H1[MCCounter] * C1)
    A2.append(H2[MCCounter] * C2)
    A3.append(H3[MCCounter] * C3)
    A4.append(H4[MCCounter] * C4)
    A5.append(H5[MCCounter] * C5)
    A6.append(H6[MCCounter] * C6)
    A7.append(H7[MCCounter] * C7)
    A8.append(H8[MCCounter] * C8)
    A9.append(H9[MCCounter] * C9)
    A10.append(H10[MCCounter] * C10)
    A11.append(H11[MCCounter] * C11)
    A12.append(H12[MCCounter] * C12)

    A0.append(A1[MCCounter] + A2[MCCounter] + A3[MCCounter] \
              + A4[MCCounter] + A5[MCCounter] + A6[MCCounter] \
              + A7[MCCounter] + A8[MCCounter] + A9[MCCounter] \
              + A10[MCCounter] + A11[MCCounter] + A12[MCCounter])

    numS1.append(numS1[MCCounter])
    numS2.append(numS2[MCCounter])
    numS3.append(numS3[MCCounter])
    numS4.append(numS4[MCCounter])
    numS5.append(numS5[MCCounter])

    numE1.append(numE1[MCCounter])
    numE2.append(numE2[MCCounter])
    numE3.append(numE3[MCCounter])
    numE4.append(numE4[MCCounter])

    numES1.append(numES1[MCCounter])
    numES2.append(numES2[MCCounter])
    numES3.append(numES3[MCCounter])
    numES4.append(numES4[MCCounter])

    r1 = rand.uniform(0, 1.0)
    r2 = rand.uniform(0, 1.0)
    dt = (1 / A0[MCCounter]) * (math.log(1 / r1))
    time += dt
    MCTime.append(time)
    MuObject = r2 * A0[MCCounter]

    A1ref = A1[MCCounter]
    A2ref = A1[MCCounter] + A2[MCCounter]
    A3ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter]
    A4ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter]
    A5ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter] + A5[MCCounter]
    A6ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter] + A5[MCCounter] + A6[MCCounter]
    A7ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter] + A5[MCCounter] + A6[MCCounter] + A7[
        MCCounter]
    A8ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter] + A5[MCCounter] + A6[MCCounter] + A7[
        MCCounter] + A8[MCCounter]
    A9ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter] + A5[MCCounter] + A6[MCCounter] + A7[
        MCCounter] + A8[MCCounter] + A9[MCCounter]
    A10ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter] + A5[MCCounter] + A6[MCCounter] + A7[
        MCCounter] + A8[MCCounter] + A9[MCCounter] + A10[MCCounter]
    A11ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter] + A5[MCCounter] + A6[MCCounter] + A7[
        MCCounter] + A8[MCCounter] + A9[MCCounter] + A10[MCCounter] + A11[MCCounter]
    A12ref = A1[MCCounter] + A2[MCCounter] + A3[MCCounter] + A4[MCCounter] + A5[MCCounter] + A6[MCCounter] + A7[
        MCCounter] + A8[MCCounter] + A9[MCCounter] + A10[MCCounter] + A11[MCCounter] + A12[MCCounter]


    if MuObject < A1ref:
        Mu = 1
    if A1ref < MuObject < A2Ref:
        Mu = 2
    if A2ref < MuObject < A3Ref:
        Mu = 3
    if A3ref < MuObject < A4Ref:
        Mu = 4
    if A4ref < MuObject < A5Ref:
        Mu = 5
    if A5ref < MuObject < A6Ref:
        Mu = 6
    if A6ref < MuObject < A7Ref:
        Mu = 7
    if A7ref < MuObject < A8Ref:
        Mu = 8
    if A8ref < MuObject < A9Ref:
        Mu = 9
    if A9ref < MuObject < A10Ref:
        Mu = 10
    if A10ref < MuObject < A11Ref:
        Mu = 11
    if A11ref < MuObject < A12Ref:
        Mu = 12

    if Mu == 1:
        E1 -= 1
        S1 -= 1
        ES1 += 1
    if Mu == 2:
        E1 += 1
        S1 += 1
        ES1 -= 1
    if Mu == 3:
        E1 += 1
        S2 += 1
        ES1 -= 1
    if Mu == 4:
        E2 -= 1
        S2 -= 1
        ES2 += 1
    if Mu == 5:
        E2 += 1
        S2 += 1
        ES2 -= 1
    if Mu == 6:
        E3 += 1
        S2 += 1
        ES2 -= 1
    if Mu == 7:
        E3 -= 1
        S3 -= 1
        ES3 += 1
    if Mu == 8:
        E3 += 1
        S3 += 1
        ES3 -= 1
    if Mu == 9:
        E3 += 1
        S4 += 1
        ES3 -= 1
    if Mu == 10:
        E4 -= 1
        S4 -= 1
        ES4 += 1
    if Mu == 11:
        E4 += 1
        S4 += 1
        ES4 -= 1
    if Mu == 12:
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
    e += 1

ax = plt.subplot()
plt.plot(MCTime, numS1, color='#a1490b', label='PET')
plt.plot(MCTime, numS2, color='blue', label='S2')
plt.plot(MCTime, numS3, color='#b08f0c', label='S3')
plt.plot(MCTime, numS4, color='#6f0ca8', label='S4')
plt.plot(MCTime, numS5, color='#12e6de', label='catechol')
plt.ylabel('Molecules')
plt.xlabel('Time(s)')
plt.title('PET degradation to catechol over time')
ax.set_facecolor('#e3e3e3')

plt.show()
