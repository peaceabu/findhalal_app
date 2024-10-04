import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Room dimensions
width = 4800  # mm
height = 5200  # mm
cell_size = 600  # mm

# Sprinklers parameters
sprinkler_radius = 1500  # mm
min_sprinkler_distance = 1200  # mm

# Create the plot
fig, ax = plt.subplots()

# Define room boundaries
room_dimensions = [(0, 0), (4800, 0), (4800, 5200), (0, 5200), (0, 4000), (3080, 4000), (3080, 2800), (0, 2800)]
room_boundary = patches.Polygon(room_dimensions, closed=True, linewidth=3, edgecolor='red', facecolor='none')
ax.add_patch(room_boundary)

# Number of cells in each direction
num_cells_x = width // cell_size
num_cells_y = height // cell_size

# Generate grid lines
for x in np.arange(0, width + cell_size, cell_size):
    ax.axvline(x=x, color='black', linestyle='-', linewidth=1)
for y in np.arange(0, height + cell_size, cell_size):
    ax.axhline(y=y, color='black', linestyle='-', linewidth=1)

# Lights and sprinklers positions
light_positions = []

# Place lights and sprinklers
for i in range(1, num_cells_x, 3):  # Space lights to prevent adjacency
    for j in range(1, num_cells_y, 3):
        # Light position (center of the cell)
        light_x = (i * cell_size)+600
        light_y = (j * cell_size)+600 
        light_positions.append((light_x+600, light_y+600))

        # Draw the light cell (green square)
        light_cell = patches.Rectangle((light_x - cell_size, light_y - cell_size), 
                                       cell_size, cell_size, linewidth=4, edgecolor='yellow', facecolor='white')
        ax.add_patch(light_cell)
        print(light_x - cell_size/2, light_y - cell_size/2)
        ax.plot(light_x - cell_size/2, light_y - cell_size/2, 'ys')


# Highlight illuminated area (8 surrounding cells in yellow)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:  # Exclude the light cell itself
                    illuminated_x = light_x + dx * cell_size
                    illuminated_y = light_y + dy * cell_size
                    print("illl",illuminated_x,illuminated_y)
                    if 0 <= illuminated_x <= width and 0 <= illuminated_y <= height:
                        illuminated_area = patches.Rectangle((illuminated_x - cell_size*2, illuminated_y - cell_size*2), 
                                                            cell_size, cell_size, linewidth=1, edgecolor='yellow', facecolor='blue', alpha=1)
                        ax.add_patch(illuminated_area)



# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Set limits for the plot
ax.set_xlim(0, width)
ax.set_ylim(0, height)

# Label the plot
ax.set_title('Hall Layout with Lights and Light Fixtures')
ax.set_xlabel('Width (mm)')
ax.set_ylabel('Height (mm)')

# Show the plot
plt.show()
