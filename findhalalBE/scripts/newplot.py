import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Room 1 dimensions
width_1 = 4800  # mm
height_1 = 5200  # mm

# Room 2 dimensions
width_2 = 1800  # mm
height_2 = 4000  # mm

# Cell size
cell_size = 600  # mm
# Create the plot with a single layout (one next to the other as in a house plan)
fig, ax = plt.subplots(figsize=(12, 12))

# Total width includes both rooms side by side
total_width = width_1 + width_2
total_height = max(height_1, height_2)  # The height is the taller of the two rooms


room_dimensions = [(4000, 4800), (5200, 4800), (5200, 4200), (8000, 4200), (8000, 0),(5200,0),(5200,1800),(4000,1800)]


grid_size = 600

fig, ax = plt.subplots(figsize=(10, 7))

room_boundary = patches.Polygon(room_dimensions, closed=True, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(room_boundary)

# Room 1 (left) grid
for x in np.arange(0, width_1 + cell_size, cell_size):
    ax.axvline(x=x, color='black', linestyle='-', linewidth=1)

for y in np.arange(0, height_1 + cell_size, cell_size):
    ax.axhline(y=y, color='black', linestyle='-', linewidth=1)

# Room 2 (right) grid - offset by the width of Room 1
for x in np.arange(width_1, width_1 + width_2 + cell_size, cell_size):
    ax.axvline(x=x, color='black', linestyle='-', linewidth=1)

for y in np.arange(0, height_2 + cell_size, cell_size):
    ax.axhline(y=y, color='black', linestyle='-', linewidth=1)

# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Set limits for the plot
ax.set_xlim(0, total_width)
ax.set_ylim(0, total_height)

# Label the plot
ax.set_title('House Plot:')
ax.set_xlabel('Width (mm)')
ax.set_ylabel('Height (mm)')

# Show the plot
plt.tight_layout()
plt.show()

