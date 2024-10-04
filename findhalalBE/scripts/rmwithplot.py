import numpy as np
import matplotlib.pyplot as plt

# Room dimensions
width_1 = 1800  # Kitchen width
height_1 = 1200  # Kitchen height
width_2 = 4800  # Hall width
height_2 = 3000  # Hall height (assumed for the example)

# Cell size for grid
cell_size = 100  # For the grid lines

# Create the plot with a single layout
fig, ax = plt.subplots(figsize=(12, 12))

# Total width includes both rooms side by side
total_width = width_1 + width_2
total_height = max(height_1, height_2) + 1200  # Height adjusted to fit both rooms

# Room 1 (kitchen) grid
for x in np.arange(0, width_1 + cell_size, cell_size):
    ax.axvline(x=x, color='black', linestyle='-', linewidth=1)

for y in np.arange(0, height_1 + cell_size, cell_size):
    ax.axhline(y=y, color='black', linestyle='-', linewidth=1)

# Room 2 (hall) grid - offset by the width of Room 1 and starting at 1200 mm height
for x in np.arange(width_1, width_1 + width_2 + cell_size, cell_size):
    ax.axvline(x=x, color='black', linestyle='-', linewidth=1)

for y in np.arange(1200, 1200 + height_2 + cell_size, cell_size):
    ax.axhline(y=y, color='black', linestyle='-', linewidth=1)

# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Set limits for the plot
ax.set_xlim(0, total_width)
ax.set_ylim(0, total_height)

# Label the plot
ax.set_title('House Plot: Kitchen (1800 mm) on Left and Hall (4800 mm) on Right')
ax.set_xlabel('Width (mm)')
ax.set_ylabel('Height (mm)')

# Show the plot
plt.tight_layout()
plt.show()
