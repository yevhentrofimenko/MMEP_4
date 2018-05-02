import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math


def roots_cubic_function():
    a = -18
    b = 45
    c = 0
    Q = (pow(a, 2) - 3 * b) / 9
    R = (2 * pow(a, 3) - 9 * a * b + 27 * c) / 54
    S = pow(Q, 3) - pow(R, 2)
    if S > 0:
        x1 = -2 * pow(Q, 0.5) * math.cos(1 / 3 * math.acos(R / pow(pow(Q, 3), 0.5))) - a / 3
        x2 = -2 * pow(Q, 0.5) * math.cos(1 / 3 * math.acos(R / pow(pow(Q, 3), 0.5)) + 2 / 3 * math.pi) - a / 3
        x3 = -2 * pow(Q, 0.5) * math.cos(1 / 3 * math.acos(R / pow(pow(Q, 3), 0.5)) - 2 / 3 * math.pi) - a / 3
        roots = [root for root in [x1, x2, x3] if root != 0]
        return roots


roots = roots_cubic_function()


def population_equation(N, t):
    b = 128
    d = 90
    p = 2
    dNdt = b * (pow(N, 2) / 1 + N) - d * N - p * pow(N, 2)
    return dNdt


t = [t*0.0001 for t in range(0, 5)]

# less than half the lower critical limit
Population_case_1 = odeint(population_equation, roots[1] / 2 - 2.4, t)

# bigger than half the lower critical limit
Population_case_2 = odeint(population_equation, roots[1] / 2 + 2.4, t)

#  lower critical limit
Population_case_3 = odeint(population_equation, roots[1], t)

# between lower and upper critical limit
Population_case_4 = odeint(population_equation, roots[0] - roots[1], t)

# upper critical limit
Population_case_5 = odeint(population_equation, roots[0], t)

# bigger than upper critical limit
Population_case_6 = odeint(population_equation, roots[0] + 2.4, t)

plt.plot(t, Population_case_1, label='less than half the lower critical limit')
plt.plot(t, Population_case_2, label='bigger than half the lower critical limit')
plt.plot(t, Population_case_3, label='lower critical limit')
plt.plot(t, Population_case_4, label='between lower and upper critical limit')
plt.plot(t, Population_case_5, label='upper critical limit')
plt.plot(t, Population_case_6, label='bigger than upper critical limit')
plt.xlabel('time')
plt.ylabel('N(t)')
plt.legend()
plt.show()
