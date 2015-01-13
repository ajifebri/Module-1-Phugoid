import math
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.size'] = 16

# model parameters
g = 9.81
ms = 50.
rho = 1.091
r = 0.5
A = math.pi * r * r
ve = 325.
Cd = 0.15

# initial conditions
h0 = 0.
v0 = 0.
mp0 = 100.


def f(u):
    h = u[0]
    v = u[1]
    mp = u[2]
    mpdot = 20.
    if mp <= 0.0:
        mp = 0.0
        mpdot = 0.0
    return np.array([v,
                     (1/(ms+mp)) * (-(ms+mp)*g + mpdot*ve - 0.5*rho*v*abs(v)*A*Cd),
                     -mpdot])

def euler_step(u, f, dt):
    return u + dt * f(u)

T = 40.0
dt = 0.1
N = int(T/dt) + 1
t = np.linspace(0.0, T, N)

# initialize the array containing the solution for each time-step
u = np.empty((N,3))
u[0] = np.array([h0, v0, mp0])

for n in range(N-1):
    u[n+1] = euler_step(u[n], f, dt)

h = u[:,0]
v = u[:,1]

# visualization of the path
plt.figure()
plt.grid()
plt.xlabel(r't', fontsize=18)
plt.ylabel(r'h or v', fontsize=18)
plt.title('Rocket flight trajectory and speed')
plt.plot(t,h,lw=2)
plt.plot(t,v,lw=2)

plt.legend(['Flight trajectory', 'Rocket speed'])
plt.show()
