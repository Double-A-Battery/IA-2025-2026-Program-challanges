import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Constants
g = 9.8  # gravity (m/s^2)

# Initial parameters
vx0 = 30  # initial x speed (m/s)
vy0 = 0  # initial y speed (m/s)
vz0 = 30  # initial z speed (m/s)
u = 30
theta_deg = 15  # elevation angle in degrees
phi_deg = 10  # azimuth angle in degrees
Am = -1 #Acceleration due to magnus

# Convert angles to radians
theta = np.radians(theta_deg)
phi = np.radians(phi_deg)

# Time of flight
t_flight = 2 * vz0 * np.sin(theta) / g

# Time points
t = np.linspace(0, t_flight, num=500)

# Parametric equations for position
x = u * np.cos(theta) * np.cos(phi) * t
y = u * np.cos(theta) * np.sin(phi) * t + 0.5 * Am * t**2
z = u * np.sin(theta) * t - 0.5 * g * t**2

# Plotting
fig = plt.figure(figsize=(10,7))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label='Rugby Ball Trajectory', color='b')

# Labels and title
ax.set_xlabel('X position (m)')
ax.set_ylabel('Y position (m)')
ax.set_zlabel('Z position (m)')
ax.set_title('3D Projectile Motion of a Rugby Ball')
ax.legend()

# Set limits for better visualization
ax.set_xlim([0, 50])
ax.set_ylim([0, 50])
ax.set_zlim([0, 25])

plt.show()
