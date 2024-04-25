###This code is designed to calculate the population change in a given year based on the population change of rabbits and foxes. This implements an equation called Lotka-Volterra function, and it takes an initial popukation, a growth rate, and a death rate as inputs. It then calculates the population change for the next year and returns the result.


import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

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

initial_population = [rabbits[0], foxes[0]]
t = np.linspace(0, len(years), len(years)*10)
solution = odeint(lotka_volterra, initial_population, t, args=(alpha, beta, delta, gamma))
rabbit_solution, fox_solution = solution.T

plt.figure(figsize=(10,6))
plt.plot(years, rabbits, 'ro', label='Rabbits')
plt.plot(years, foxes, 'bo', label='Foxes')
plt.plot(years, rabbit_solution, 'r-', label='Rabbit Model')
plt.plot(years, fox_solution, 'b-', label='Fox Model')
plt.title('Population Dynamics of Rabbits and Foxes')
plt.xlabel('Year')
plt.ylabel('Population')
plt.legend()
plt.grid(True)
plt.show()
