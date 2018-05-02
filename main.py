from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# time points
t = [x for x in range(0, 25)]
t_straight = [x for x in range(25)]


def model(N, t):
    """
    :param y
    :param t
    :return: dN/dt
    """
    a = -0.056
    b = 0.0004
    dNdt = a * N + b * N ** 2
    return dNdt


# start points
N0_case_1 = 100
N0_case_2 = 180

N_straight = []
for x in range(25):
    N_straight.append(100)

# Population in 2,5 years
Case_1 = odeint(model, N0_case_1, [0, 2.5])[1][0]
Case_2 = odeint(model, N0_case_2, [0, 2.5])[1][0]
print('Population in a 2,5 years (Case 1): {}'.format(Case_1))
print('Population in a 2,5 years (Case 2): {}'.format(Case_2))

# solve ODE
N_case_1 = odeint(model, N0_case_1, t)
N_case_2 = odeint(model, N0_case_2, t)
# plot results
plt.plot(t, N_case_1, label='N=100')
plt.plot(t_straight, N_straight, label='Straight line N=100')
plt.plot(t, N_case_2, label='N=180')
plt.xlabel('time')
plt.ylabel('N(t)')
plt.legend()
plt.show()
