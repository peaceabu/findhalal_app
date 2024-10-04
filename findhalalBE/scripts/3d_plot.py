import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
fig.suptitle("3D Cylindrical Plot", fontsize=16)
ax = fig.add_subplot(111, projection='3d')


theta = np.linspace(0, 2 * np.pi, 12) 
x = np.linspace(-12, 12, 6)  
r = 6 

for i in x:
    y = r * np.cos(theta)  
    z = r * np.sin(theta) 
    x_vals = np.ones_like(theta) * i 
    ax.scatter(x_vals, y, z, color=np.random.rand(3,), s=100)  
    ax.plot(x_vals, y, z, color=np.random.rand(3,))

for i in range(len(theta)):
    ax.plot(x, 
            [r * np.cos(theta[i])] * len(x), 
            [r * np.sin(theta[i])] * len(x), 
            color=np.random.rand(3,))


ax.set_xlim([-18, 18])
ax.set_ylim([-7, 7])
ax.set_zlim([-7, 7])

plt.show()
