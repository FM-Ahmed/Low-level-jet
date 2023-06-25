import numpy as np
import matplotlib.pyplot as plt

z = np.linspace(10, 570, 113) # height array, zr should be in array
alpha = 0.11 # shear exponent
zj = 150 # jet height
Cs = 1 # Gaussian function shape parameter
zref = 150 # reference height
uref = 9 # reference velocity
umax = 5 # jet maximum velocity

def single_LLJ(z, alpha, zj, Cs, zref, uref, umax):
  brackets = 1 - np.tanh(Cs*(z-zj)/zj)**2
  u = (umax*(brackets))*((z/zref)**alpha) + uref*(z/zref)**alpha
  return u, z

plt.figure(figsize = [4, 6])
plt.plot(u, z)
plt.grid(True, 'both')
