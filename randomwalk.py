import numpy as np
import matplotlib.pyplot as plt

#SOME SET UP AND VARIABLES

paths = 100
steps = 100

sigma = 5.0  #volatility
mu = .05 #drift

dt = 1.0/steps
s0 = 10  #initial price

prices = np.zeros((paths, steps+1))
prices[:,0] = s0


for path in range(paths):
    for step in range(steps):
        eps = np.random.normal(0,1,1)[0]
        prices[path, step+1] = prices[path, step]*np.exp((mu-0.5*sigma**2)*dt + eps*sigma*np.sqrt(dt))


plt.plot(np.linspace(0,1,steps+1), np.percentile(prices, 95, axis = 0))
plt.title('asset price projection at 95 percentile')
plt.xlabel('t')
plt.show()
