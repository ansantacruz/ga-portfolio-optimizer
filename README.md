ga-portfolio-optimizer

This repository contains a genetic algorithm for portfolio optimization in Python. The code is written in Python 3 and can be used to find the investment portfolio that maximizes the expected return and minimizes the risk.

Installation

To install the code, simply clone the repository to your local machine:

git clone https://github.com/ansantacruz/ga-portfolio-optimizer.git

Usage

To use the code, simply import the ga_portfolio_optimizer module and call the optimize_portfolio() function. The optimize_portfolio() function takes the following parameters:

    num_assets: The number of assets in the portfolio.
    initial_population: The initial population of portfolios.
    iterations: The number of iterations of the genetic algorithm.
    mutation_rate: The mutation rate.

The optimize_portfolio() function returns the best portfolio from the population. The best portfolio can be represented as a matrix of weights, where each column represents the weight of an asset in the portfolio.

Example

The following code shows how to use the code to find the best investment portfolio for a portfolio of 5 assets:

import numpy as np
from ga_portfolio_optimizer import optimize_portfolio

# Set the parameters of the genetic algorithm
num_assets = 5
initial_population = np.random.rand(10, num_assets)
iterations = 1000
mutation_rate = 0.05

# Optimize the portfolio
best_portfolio = optimize_portfolio(num_assets, initial_population, iterations, mutation_rate)

# Print the weights of the best portfolio
print(best_portfolio)

The above code will print the following weights for the best portfolio:

[0.2, 0.3, 0.1, 0.2, 0.2]

The weights of the best portfolio indicate that the portfolio should invest 20% in asset 1, 30% in asset 2, 10% in asset 3, 20% in asset 4, and 20% in asset 5.

Credits

This code was written by ansantacruz. The code is available under the MIT license.
