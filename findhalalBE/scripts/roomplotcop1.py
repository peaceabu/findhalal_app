import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

# Room dimensions in meters (converted to mm)
room_dimensions = [
    [(0, 0), (4000, 0), (4000, 4800), (5200, 4800), (5200, 0), (8000, 0), (8000, 4000), (0, 4000)],
    [(0, 0), (4000, 0), (4000, 4800), (5200, 4800), (5200, 0), (8000, 0), (8000, 4000), (0, 4000)]
]

# Grid size in mm
grid_size = 600

# Create a figure and axis
fig, axs = plt.subplots(1, 2, figsize=(15, 7))

for ax, room in zip(axs, room_dimensions):
    # Draw the room boundary
    room_boundary = patches.Polygon(room, closed=True, linewidth=1, edgecolor='black', facecolor='none')
    ax.add_patch(room_boundary)

    # Draw the grid within the room boundary
    min_x = min([point[0] for point in room])
    max_x = max([point[0] for point in room])
    min_y = min([point[1] for point in room])
    max_y = max([point[1] for point in room])

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

                # Check if the center is within the room boundary
                if patches.Polygon(room).contains_point((x_center, y_center)):
                    # Ensure no lights are adjacent
                    if (i + j) % 2 == 0 and grid_lights[i, j] == 0:
                        lights.append((x_center, y_center))
                        # Mark the light on the grid
                        grid_lights[i, j] = 1
                        # Draw light and illuminated area
                        light_square = patches.Rectangle((x_center - grid_size / 2, y_center - grid_size / 2), grid_size, grid_size, linewidth=1, edgecolor='yellow', facecolor='yellow', alpha=0.3)
                        ax.add_patch(light_square)
                        ax.plot(x_center, y_center, 'ys')
                    
                    # Place sprinklers at least 500mm from walls and spaced apart
                    if (i + j) % 3 == 0 and grid_lights[i, j] == 0:
                        sprinklers.append((x_center, y_center))
                        # Mark sprinkler placement
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
