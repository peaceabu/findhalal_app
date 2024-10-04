import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Room dimensions in mm (example dimensions, can be adjusted)
room_length = 6000
room_width = 4000

# Grid size in mm
grid_size = 600

# Calculate number of grids
num_grids_x = room_length // grid_size
num_grids_y = room_width // grid_size

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the room boundary
room_boundary = patches.Rectangle((0, 0), room_length, room_width, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(room_boundary)

# Draw the grid
for i in range(num_grids_x + 1):
    ax.plot([i * grid_size, i * grid_size], [0, room_width], color='gray', linestyle='--', linewidth=0.5)
for j in range(num_grids_y + 1):
    ax.plot([0, room_length], [j * grid_size, j * grid_size], color='gray', linestyle='--', linewidth=0.5)

# Function to place lights and sprinklers
def place_lights_and_sprinklers():
    lights = []
    sprinklers = []
    
    for i in range(num_grids_x):
        for j in range(num_grids_y):
            x_center = (i + 0.5) * grid_size
            y_center = (j + 0.5) * grid_size
            
            # Place lights at the center of the grid cells
            if (i + j) % 2 == 0:
                lights.append((x_center, y_center))
                # Draw light and illuminated area
                light_square = patches.Rectangle((x_center - grid_size / 2, y_center - grid_size / 2), grid_size, grid_size, linewidth=1, edgecolor='yellow', facecolor='yellow', alpha=0.3)
                ax.add_patch(light_square)
                ax.plot(x_center, y_center, 'ys')
            
            # Place sprinklers at the center of the grid cells
            if (i + j) % 3 == 0:
                sprinklers.append((x_center, y_center))
                # Draw sprinkler and coverage area
                sprinkler_dot = patches.Circle((x_center, y_center), radius=50, color='red')
                coverage_circle = patches.Circle((x_center, y_center), radius=1500, linewidth=1, edgecolor='blue', facecolor='none')
                ax.add_patch(sprinkler_dot)
                ax.add_patch(coverage_circle)
    
    return lights, sprinklers

# Place lights and sprinklers
lights, sprinklers = place_lights_and_sprinklers()

# Set plot limits and aspect ratio
ax.set_xlim(0, room_length)
ax.set_ylim(0, room_width)
ax.set_aspect('equal')

# Show plot
plt.show()
