import math
import random as rand
import matplotlib.pyplot as plt

fig = plt.figure(figsize=(20, 10))

e = 1  # number of times that the simulation is run
while (e < 100):
    rc_AB = 1   # reaction chain
    rc_BC = 1
    rc_CD = 1
    rc_DE = 1
    rc_EF = 1

    # Set initial numbers of molecules
    A = 150
    B = 0
    C = 0
    D = 0
    E = 0
    F = 0
    total_molecs = A + B + C + D + E + F
    # ???
    A_sim = [
        A]  # each start with initial value; each new reaction means appending the new number of molecuels to that list
    B_sim = [B]  # brackets denote lists
    C_sim = [C]
    D_sim = [D]
    E_sim = [E]
    F_sim = [F]

    t = 0
    t_sim = [0]
    while (t < 10000):  # number of seconds that the reaction is running

        r_AB = rc_AB * A
        r_BC = rc_BC * B
        r_CD = rc_CD * C
        r_DE = rc_DE * D
        r_EF = rc_EF * E

        r_total = r_AB + r_BC + r_CD + r_DE + r_EF

        if r_total == 0:
            break
        else:
            None

        p_AB = r_AB / r_total  # probabilities
        p_BC = r_BC / r_total
        p_CD = r_CD / r_total
        p_DE = r_DE / r_total

        r1 = rand.uniform(0, 1.0)
        r2 = rand.uniform(0, 1.0)

        if r1 <= p_AB:
            A -= 1
            B += 1
        elif p_AB < r1 <= (p_AB + p_BC):
            B -= 1
            C += 1
        elif (p_AB + p_BC) < r1 <= (p_AB + p_BC + p_CD):
            C -= 1
            D += 1
        elif (p_AB + p_BC + p_CD) < r1 <= (p_AB + p_BC + p_CD + p_DE):
            D -= 1
            E += 1
        elif r1 > (p_AB + p_BC + p_CD + p_DE):
            E -= 1
            F += 1
        if A + B + C + D + E + F > total_molecs:  # total number of molecules can't be higher than the original number of molecules
            break
        A_sim.append(A)  # thing in parentheses gets appended
        B_sim.append(B)
        C_sim.append(C)
        D_sim.append(D)
        E_sim.append(E)
        F_sim.append(F)

        dt = math.log(1 / r2)  # from Lecca paper
        t += dt
        t_sim.append(t)

    ax = plt.subplot()
    plt.plot(t_sim, A_sim, color='red', label='A')
    plt.plot(t_sim, B_sim, color='blue', label='B')
    plt.plot(t_sim, C_sim, color='purple', label='C')
    plt.plot(t_sim, D_sim, color='yellow', label='D')
    plt.plot(t_sim, E_sim, color='green', label='E')
    plt.plot(t_sim, F_sim, color='orange', label='F')
    plt.xlabel('Time(seconds)')
    plt.ylabel('Molecules')
    plt.title('ABCDEF Linear Reaction Chain Sim')
    plt.legend(['A', 'B', 'C', 'D', 'E', 'F'])
    ax.set_facecolor('#dedcdc')

    e += 1  # adding 1 to e (R equivalent )

plt.show()
