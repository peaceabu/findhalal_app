import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Room dimensions
width = 4800  # mm
height = 5200  # mm
cell_size = 600  # mm


# room_dimensions = [(0, 0), (4000, 0), (4000, 4800), (5200, 4800), (5200, 4000), (8000, 4000), (8000, 0), (4000, 0)]
# room_dimensions = [(4000, 4800), (5200, 4800), (5200, 4200), (8000, 4200), (8000, 0),(5200,0),(5200,1800),(4000,1800)]

# room_dimensions = [(0, 0), (4800, 0), (4800, 5200), (0, 5200)]
room_dimensions = [(0, 0), (4800, 0), (4800, 5200), (0, 5200),(0,4000),(3080,4000),(3080,2800),(0,2800)]
grid_size = 600

# fig, ax = plt.subplots(figsize=(10, 7))
fig, ax = plt.subplots()

room_boundary = patches.Polygon(room_dimensions, closed=True, linewidth=3, edgecolor='red', facecolor='none')
ax.add_patch(room_boundary)

# Number of cells in each direction
num_cells_x = width // cell_size
num_cells_y = height // cell_size

# Create the plot


# Generate grid lines
for x in np.arange(0, width + cell_size, cell_size):
    ax.axvline(x=x, color='black', linestyle='-', linewidth=1)

for y in np.arange(0, height + cell_size, cell_size):
    ax.axhline(y=y, color='black', linestyle='-', linewidth=1)

# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Set limits for the plot
ax.set_xlim(0, width)
ax.set_ylim(0, height)

# Label the plot
ax.set_title('Hall')
ax.set_xlabel('Width (mm)')
ax.set_ylabel('Height (mm)')

# Show the plot
plt.show()
