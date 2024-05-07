# This code is designed to calculate the population change in a given year
# based on the population change of rabbits and foxes. This implements an equation
# called Lotka-Volterra function, and it takes an initial population, a growth rate,
# and a death rate as inputs. It then calculates the population change for the next year and
# returns the result.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.integrate import odeint


def lotka_volterra(y, _, alpha, beta, gamma, delta):
    # alpha, beta, gamma, delta = parameters
    rabbit_pop, fox_pop = y
    rabbit_time_rate = alpha * rabbit_pop - beta * rabbit_pop * fox_pop
    fox_time_rate = delta * rabbit_pop * fox_pop - gamma * fox_pop
    return [rabbit_time_rate, fox_time_rate]


# read in a file that contains yearly populations
data = np.loadtxt('population.txt', delimiter=",", skiprows=1)
years = data[:, 0]
rabbits = data[:, 1]
foxes = data[:, 2]

# Fit Lotka-Volterra model to data
fit_result = curve_fit(lotka_volterra, (rabbits[:-1],
                                        foxes[:-1]), (rabbits[1:], foxes[1:]),
                       bounds=(0, np.inf))

optimal_parameters = fit_result[0]
covariance_matrix = fit_result[1]

print("Optimal Parameters:", optimal_parameters)
print("Covariance Matrix:", covariance_matrix)

initial_populations = [rabbits[0], foxes[0]]

# plt.plot(years, rabbits, label="Rabbits")
# plt.plot(years, foxes, label="Foxes")
# plt.show()

t = np.linspace(0, len(years), len(years) * 10)
solution = odeint(lotka_volterra, initial_populations, t, args=tuple(optimal_parameters))
rabbit_solution = solution[:, 0]
fox_solution = solution[:, 1]

# plot results
plt.figure(figsize=(10, 6))
plt.plot(years, rabbits, 'ro', label='Rabbits')
plt.plot(years, foxes, 'bo', label='Foxes')

# Generate model from fitted parameters
plt.plot(t, rabbit_solution, 'r-', label='Rabbit Model')
plt.plot(t, fox_solution, 'b-', label='Fox Model')
plt.title('Population Dynamics of Rabbits and Foxes')
plt.xlabel('Year')
plt.ylabel('Population')

plt.grid(True)

# start_year, stop_year = 2023, 2040
# number_of_years = stop_year - start_year
# years = np.linspace(start_year, stop_year, number_of_years)

# current_population = np.array(initial_populations)
# populations_by_year = [current_population]

# populations_by_year = np.array(populations_by_year)
# years = np.append(years, years[-1] + 1)
# plt.plot(years, populations_by_year[:,0], years, populations_by_year[:,1])
plt.legend()
plt.show()

# print("Optimized parameter values")
# print("Alpha", optimal_parameters[0])
# print("Beta", optimal_parameters[1])
# print("Gamma", optimal_parameters[2])
# print("Delta", optimal_parameters[3])
