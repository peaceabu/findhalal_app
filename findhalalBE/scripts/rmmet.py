import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Room dimensions in mm
room1_dimensions = [(0, 0), (4000, 0), (4000, 4800), (0, 4800)]
room2_dimensions = [(5200, 0), (8000, 0), (8000, 4000), (5200, 4000)]

# Grid size in mm
grid_size = 600

# Create a figure and axis
fig, ax = plt.subplots(figsize=(12, 7))

# Draw room boundaries
room1_boundary = patches.Polygon(room1_dimensions, closed=True, linewidth=2, edgecolor='black', facecolor='none')
room2_boundary = patches.Polygon(room2_dimensions, closed=True, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(room1_boundary)
ax.add_patch(room2_boundary)

# Define min and max x/y based on room dimensions
min_x = min([point[0] for point in room1_dimensions + room2_dimensions])
max_x = max([point[0] for point in room1_dimensions + room2_dimensions])
min_y = min([point[1] for point in room1_dimensions + room2_dimensions])
max_y = max([point[1] for point in room1_dimensions + room2_dimensions])

# Draw grid
for i in range(min_x // grid_size, max_x // grid_size + 1):
    ax.plot([i * grid_size, i * grid_size], [min_y, max_y], color='gray', linestyle='--', linewidth=0.5)
for j in range(min_y // grid_size, max_y // grid_size + 1):
    ax.plot([min_x, max_x], [j * grid_size, j * grid_size], color='gray', linestyle='--', linewidth=0.5)

# Function to place lights and sprinklers
def place_lights_and_sprinklers():
    lights = []
    sprinklers = []
    grid_lights = np.zeros(((max_x - min_x) // grid_size + 1, (max_y - min_y) // grid_size + 1), dtype=int)
    grid_sprinklers = np.zeros(((max_x - min_x) // grid_size + 1, (max_y - min_y) // grid_size + 1), dtype=int)

    for i in range(min_x // grid_size, max_x // grid_size + 1):
        for j in range(min_y // grid_size, max_y // grid_size + 1):
            x_center = (i + 0.5) * grid_size
            y_center = (j + 0.5) * grid_size

            # Ensure placement follows room boundary
            if (room1_boundary.contains_point((x_center, y_center)) or 
                room2_boundary.contains_point((x_center, y_center))):

                # Place lights
                if (i + j) % 2 == 0 and grid_lights[i - min_x // grid_size, j - min_y // grid_size] == 0:
                    lights.append((x_center, y_center))
                    grid_lights[i - min_x // grid_size, j - min_y // grid_size] = 1
                    # Draw light and illuminated area
                    light_square = patches.Rectangle((x_center - grid_size / 2, y_center - grid_size / 2), grid_size, grid_size, linewidth=1, edgecolor='yellow', facecolor='yellow', alpha=0.3)
                    ax.add_patch(light_square)
                    ax.plot(x_center, y_center, 'ys')

                # Place sprinklers
                if (i + j) % 3 == 0 and grid_sprinklers[i - min_x // grid_size, j - min_y // grid_size] == 0:
                    # Ensure sprinklers are at least 500 mm from the walls
                    if x_center >= min_x + 500 and x_center <= max_x - 500 and y_center >= min_y + 500 and y_center <= max_y - 500:
                        # Check spacing between sprinklers
                        sprinkler_placed = False
                        for sprinkler in sprinklers:
                            distance = np.sqrt((x_center - sprinkler[0])**2 + (y_center - sprinkler[1])**2)
                            if distance < 1200:
                                sprinkler_placed = True
                                break
                        if not sprinkler_placed:
                            sprinklers.append((x_center, y_center))
                            grid_sprinklers[i - min_x // grid_size, j - min_y // grid_size] = 1
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
