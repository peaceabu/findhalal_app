import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Room dimensions in meters (converted to mm)
room_dimensions = [(0, 0), (4000, 0), (4000, 4800), (5200, 4800), (5200, 0), (8000, 0), (8000, 4000), (0, 4000)]

# Grid size in mm
grid_size = 600

# Create a figure and axis
fig, ax = plt.subplots()

# Draw the room boundary
room_boundary = patches.Polygon(room_dimensions, closed=True, linewidth=1, edgecolor='black', facecolor='none')
ax.add_patch(room_boundary)

# Draw the grid within the room boundary
min_x = min([point[0] for point in room_dimensions])
max_x = max([point[0] for point in room_dimensions])
min_y = min([point[1] for point in room_dimensions])
max_y = max([point[1] for point in room_dimensions])

for i in range(min_x // grid_size, max_x // grid_size + 1):
    ax.plot([i * grid_size, i * grid_size], [min_y, max_y], color='gray', linestyle='--', linewidth=0.5)
for j in range(min_y // grid_size, max_y // grid_size + 1):
    ax.plot([min_x, max_x], [j * grid_size, j * grid_size], color='gray', linestyle='--', linewidth=0.5)

# Function to place lights and sprinklers
def place_lights_and_sprinklers():
    lights = []
    sprinklers = []
    
    for i in range(min_x // grid_size, max_x // grid_size):
        for j in range(min_y // grid_size, max_y // grid_size):
            x_center = (i + 0.5) * grid_size
            y_center = (j + 0.5) * grid_size
            
            # Check if the center is within the room boundary
            if plt.Polygon(room_dimensions).contains_point((x_center, y_center)):
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
ax.set_xlim(min_x - grid_size, max_x + grid_size)
ax.set_ylim(min_y - grid_size, max_y + grid_size)
ax.set_aspect('equal')

# Show plot
plt.show()
