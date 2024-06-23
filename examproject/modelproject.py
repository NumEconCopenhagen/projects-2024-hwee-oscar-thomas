from scipy import optimize
import matplotlib.pyplot as plt
import numpy as np

def solve_ss(alpha, c):
    """ Example function. Solve for steady state k. 

    Args:
        c (float): costs
        alpha (float): parameter

    Returns:
        result (RootResults): the solution represented as a RootResults object.

    """ 
    
    # a. Objective function, depends on k (endogenous) and c (exogenous).
    f = lambda k: k**alpha - c
    obj = lambda kss: kss - f(kss)

    #. b. call root finder to find kss.
    result = optimize.root_scalar(obj,bracket=[0.1,100],method='bisect')
    
    return result

class SolowModel:
    # Set parameter values
    def __init__(self, s=0.3, n=0.02, delta=0.05, alpha=0.5, L=100, K0=50, T=100):
        self.s = s  # savings rate
        self.n = n  # population growth rate
        self.delta = delta  # depreciation rate
        self.alpha = alpha  # capital share of output
        self.L = L  # labor force
        self.K0 = K0  # initial capital
        self.T = T  # number of periods
        
    def steady_state_capital(self):
        return ((self.s * self.L) / (self.delta + self.n))**(1 / (1 - self.alpha))
    
    def solow_model(self, K):
        return self.s * self.L * (K**self.alpha) - (self.delta + self.n) * K
    
    def simulate(self):
        K = np.zeros(self.T+1)
        K[0] = self.K0
        for t in range(self.T):
            K[t+1] = K[t] + self.solow_model(K[t])
        return K
    
    def plot_simulation(self, K):
        t = np.arange(self.T+1)
        plt.plot(t, K, label='Capital Stock (K)')
        plt.xlabel('Time')
        plt.ylabel('Capital Stock')
        plt.title('Solow Model Simulation')
        plt.legend()
        plt.grid(True)
        plt.show()