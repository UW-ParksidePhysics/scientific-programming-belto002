"""
Simulates a population of prey and predators (rabbits and foxes)

Equations of interest:
dP/dt = P(f(t) - g(t))
f(t) = f0 - f1P
g(t) = go - g1P
dP/dt = P * (f0 - f1P) - go )
dP/dt = f0P - f1P2 - goP
dP/dt = -f1P (f0 go/f1 - P)
dP/dt = kP( M - P)
"""

import numpy as np
import matplotlib.pyplot as plt

import matplotlib

matplotlib.use('macosx')


def lotka_volterra(y, parameters):
    alpha, beta, gamma, delta = parameters
    rabbit_pop, fox_pop = y
    rabbit_time_rate = alpha * rabbit_pop - beta * rabbit_pop * fox_pop
    fox_time_rate = delta * rabbit_pop * fox_pop - gamma * fox_pop
    return np.array([rabbit_time_rate, fox_time_rate])


# read in a file that contains yearly populations
data = np.loadtxt('population.txt', delimiter=".", skiprows=1)
years = data[:, 0]
rabbits = data[:, 1]
foxes = data[:, 2]

# defines parameters for the lotka-volterra equation
equation_parameters = [
    0.002,   # Rabbit birth rate (alpha)
    0.0002,  # Rabbit death rate (beta)
    0.001,  # Fox birth rate (gamma)
    0.0001,   # Fox death rate (delta)
]

initial_populations = [rabbits[0], foxes[0]]


start_year, stop_year = 2023, 2040
number_of_years = stop_year - start_year
years = np.linspace(start_year, stop_year, number_of_years)

current_population = np.array(initial_populations)
populations_by_year = [current_population]

for year in years:
    #print(f'R_i, F_i = {current_population}')
    change_rates = lotka_volterra(current_population, equation_parameters)
    #print(f'dR/dt, dF/dt = {change_rates}')
    current_population = current_population + change_rates # * current_population
    #print(f'R_i+1, F_i+1 = {current_population}')
    populations_by_year.append(current_population)
    #print()



populations_by_year = np.array(populations_by_year)
years = np.append(years, years[-1]+1)
plt.plot(years, populations_by_year[:,0], years, populations_by_year[:,1])
plt.show()
