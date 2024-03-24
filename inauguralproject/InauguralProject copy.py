from types import SimpleNamespace

class InauguralProjectClass:

    def __init__(self):

        par = self.par = SimpleNamespace()

        # a. preferences
        par.alpha = 1/3
        par.beta = 2/3

        # b. endowments
        par.w1A = 0.8
        par.w2A = 0.3
        par.w1B = 1 - par.w1A
        par.w2B = 1 - par.w2A

    # Utility functions
    def utility_A(self,x1A,x2A):
        return x1A**self.par.alpha * x2A**(1-self.par.alpha)

    def utility_B(self,x1B,x2B):
        return x1B**self.par.beta * x2B**(1-self.par.beta)

    # Demand functuons
    def demand_A(self,p1):
        par = self.par
        
        # The numeraire is set to p2 = 1
        p2 = 1

        # For simplicity, we define the income/budget for consumer A
        IncomeA = p1 * par.w1A + p2 * par.w2A

        # The demand functions of consumer A is given by
        x1A = (par.alpha * IncomeA) / p1
        x2A = ((1-par.alpha) * IncomeA) / p2
        return x1A, x2A

    def demand_B(self,p1):
        par = self.par

        # The numeraire is set to p2 = 1
        p2 = 1

        # For simplicity, we define the income/budget for consumer B
        IncomeB = p1 * par.w1B + p2 * par.w2B

        # The demand functions of consumer B is given by
        x1B = (par.beta * IncomeB) / p1
        x2B = ((1-par.beta) * IncomeB) / p2
        return x1B, x2B

    # Market clearing function
    def check_market_clearing(self,p1):
        par = self.par

        x1A,x2A = self.demand_A(p1)
        x1B,x2B = self.demand_B(p1)

        eps1 = x1A-par.w1A + x1B-par.w1B
        eps2 = x2A-par.w2A + x2B-par.w2B

        return eps1,eps2