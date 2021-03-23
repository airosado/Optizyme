#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 14:11:17 2020

@author: airosado
"""

# this is a simulation of a simple system of two types of molecs A and B
# that react reversibly to form dimers AB

import random
import matplotlib.pyplot as plt
import math


def sim():
    rc_synth = 4
    rc_diss = 8

    A = 70
    B = 50
    AB = 15

    A_sim = [A]
    B_sim = [B]
    AB_sim = [AB]
    t = 0
    t_sim = [0]
    while (t < 150):
        r_synth = rc_synth * A * B
        r_diss = rc_diss * AB
        r_total = r_synth + r_diss
        p_synth = r_synth / r_total

        r1 = random.uniform(0, 1.0)
        r2 = random.uniform(0, 1.0)

        dt = math.log(1 / r2)
        t += dt
        t_sim.append(t)

        if AB == 0 or r1 < p_synth:
            A -= 1
            B -= 1
            AB += 1
        elif A == 0 or r1 > p_synth:
            A += 1
            B += 1
            AB -= 1
        A_sim.append(A)
        B_sim.append(B)
        AB_sim.append(AB)

    ax = plt.subplot()
    plt.plot(t_sim, A_sim, color='red', label='A')
    plt.plot(t_sim, B_sim, color='blue', label='B')
    plt.plot(t_sim, AB_sim, color='purple', label='AB')


e = 0
while (e < 100):
    sim()
    e += 1
    ax = plt.subplot()
    plt.xlabel('Time(seconds)')
    plt.ylabel('Molecules')
    plt.title('AB Dimer Reaction Simulation')
    plt.legend(['A', 'B', 'AB'])
    ax.set_facecolor('#dedcdc')

plt.show()
