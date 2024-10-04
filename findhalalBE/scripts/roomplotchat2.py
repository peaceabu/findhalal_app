import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Room dimensions in mm (based on the L-shaped layout from the PDF)
room_dimensions = [(0, 0), (4000, 0), (4000, 4800), (5200, 4800), (5200, 4000), (8000, 4000), (8000, 0), (4000, 0)]

# Grid size in mm
grid_size = 600

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 7))

# Draw the L-shaped room boundary using a Polygon
room_boundary = patches.Polygon(room_dimensions, closed=True, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(room_boundary)

# Define min and max x/y based on room dimensions
min_x = min([point[0] for point in room_dimensions])
max_x = max([point[0] for point in room_dimensions])
min_y = min([point[1] for point in room_dimensions])
max_y = max([point[1] for point in room_dimensions])

# Draw the grid inside the room boundary
for i in range(min_x // grid_size, max_x // grid_size + 1):
    ax.plot([i * grid_size, i * grid_size], [min_y, max_y], color='gray', linestyle='--', linewidth=0.5)
for j in range(min_y // grid_size, max_y // grid_size + 1):
    ax.plot([min_x, max_x], [j * grid_size, j * grid_size], color='gray', linestyle='--', linewidth=0.5)

# Function to place lights and sprinklers
def place_lights_and_sprinklers():
    lights = []
    sprinklers = []
    grid_lights = np.zeros(((max_x - min_x) // grid_size, (max_y - min_y) // grid_size), dtype=int)
    
    for i in range(min_x // grid_size, max_x // grid_size):
        for j in range(min_y // grid_size, max_y // grid_size):
            x_center = (i + 0.5) * grid_size
            y_center = (j + 0.5) * grid_size

            # Ensure placement follows room boundary and no adjacent lights
            if patches.Polygon(room_dimensions).contains_point((x_center, y_center)):
                # Place lights in alternate grid cells
                if (i + j) % 2 == 0 and grid_lights[i, j] == 0:
                    lights.append((x_center, y_center))
                    grid_lights[i, j] = 1
                    # Draw light and illuminated area
                    light_square = patches.Rectangle((x_center - grid_size / 2, y_center - grid_size / 2), grid_size, grid_size, linewidth=1, edgecolor='yellow', facecolor='yellow', alpha=0.3)
                    ax.add_patch(light_square)
                    ax.plot(x_center, y_center, 'ys')
                
                # Place sprinklers with proper distance from walls and spacing
                if (i + j) % 3 == 0 and grid_lights[i, j] == 0:
                    # Ensure sprinklers are at least 500 mm from the walls
                    if x_center >= min_x + 500 and x_center <= max_x - 500 and y_center >= min_y + 500 and y_center <= max_y - 500:
                        sprinklers.append((x_center, y_center))
                        grid_lights[i, j] = 2
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
