###dP/dt = P(f(t) - g(t))
###f(t) = f0 - f1P
###g(t) = go - g1P
###dP/dt = P * (f0 - f1P) - go )
###dP/dt = f0P - f1P2 - goP
###dP/dt = -f1P (f0 go/f1 - P)
###dP/dt = kP( M - P)

###def pop_increase(current_pop, growth_rate)

import numpy as np
import matplotlib.pyplot as plt


def lotka_volterra(t, y, alpha, beta, delta, gamma):
    rabbit_pop, fox_pop = y
    
    dR_dt = alpha * rabbit_pop - beta * rabbit_pop * fox_pop
    dF_dt = delta * rabbit_pop * fox_pop - gamma * fox_pop
    return [dR_dt, dF_dt]

#read in a file that contains yearly populations
data = np.loadtxt('population.txt', delimiter= ".", skiprows=1)
years = data[:, 0]
rabbits = data[:, 1]
foxes = data[:, 2]

#defines parameters for the lotka-volterra equation
alpha = 0.1 #Rabbit birth rate
beta = 0.02 #Rabbit death rate

delta = 0.02 #Fox birth rate
gamma = 0.1 #Fox death rate

plt.plot(years, rabbits, label="Rabbits")
plt.plot(years, foxes, label="Foxes")
plt.show()