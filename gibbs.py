import numpy as np

disasters_array = np.array([4, 5, 4, 0, 1, 4, 3, 4, 0, 6, 3, 3, 4, 0, 2, 6,
                         3, 3, 5, 4, 5, 3, 1, 4, 4, 1, 5, 5, 3, 4, 2, 5,
                         2, 2, 3, 4, 2, 1, 3, 2, 2, 1, 1, 1, 1, 3, 0, 0,
                         1, 0, 1, 1, 0, 0, 3, 1, 0, 3, 2, 2, 0, 1, 1, 1,
                         0, 1, 0, 1, 0, 0, 0, 2, 1, 0, 0, 0, 1, 1, 0, 2,
                         3, 3, 1, 1, 2, 1, 1, 1, 1, 2, 4, 2, 0, 0, 1, 4,
                         0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1])
# Function to draw random gamma variate
rgamma = np.random.gamma
# Function to draw random categorical variate
rcategorical = lambda probs, n=None: np.array(probs).cumsum().searchsorted(np.random.sample(n
dgamma = lambda lam, a, b: lam**(a-1) * np.exp(-b*lam)
alpha, beta = 1., 10

# Specify number of iterations
n_iterations = 1000
# Initialize trace of samples
lambda1, lambda2, tau = np.empty((3, n_iterations+1))

lambda1[0] = 6
lambda2[0] = 2
tau[0] = 50

# Sample from conditionals
for i in range(n_iterations):
    
    # Sample early mean
    lambda1[i+1] = rgamma(disasters_array[:int(tau[i])].sum() + alpha, 1./(tau[i] + beta))
    
    # Sample late mean
    lambda2[i+1] = rgamma(disasters_array[int(tau[i]):].sum() + alpha, 
                          1./(n_count_data - tau[i] + beta))
    
    # Sample changepoint
    p = np.array([dgamma(lambda1[i+1], disasters_array[:t].sum() + alpha, t + beta)*
             dgamma(lambda2[i+1], disasters_array[t:].sum() + alpha, n_count_data - t + beta)
             for t in range(n_count_data)])
    tau[i+1] = rcategorical(p/p.sum())
