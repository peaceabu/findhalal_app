import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Room dimensions
width = 4800  # mm
height = 5200  # mm
cell_size = 600  # mm

# Sprinkler constraints
sprinkler_radius = 1500  # mm
min_sprinkler_distance = 1200  # mm
max_sprinkler_distance = 1500  # mm
wall_clearance = 500  # mm

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

# Place lights and draw illuminated areas
for i in range(1, num_cells_x, 3):  # Space lights to prevent adjacency
    for j in range(1, num_cells_y, 3):
        # Light position (center of the cell)
        light_x = (i * cell_size) + 600
        light_y = (j * cell_size) + 600
        light_positions.append((light_x - cell_size/2, light_y - cell_size/2))

        # Draw the illuminated area (8 surrounding cells in yellow)
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                # Skip the center cell where the light is placed
                if dx != 0 or dy != 0:
                    illuminated_x = light_x + dx * cell_size
                    illuminated_y = light_y + dy * cell_size
                    # Ensure the illuminated cell edge is within room bounds
                    if illuminated_x - cell_size < width and illuminated_y - cell_size < height:
                        illuminated_cell = patches.Rectangle((illuminated_x - cell_size, illuminated_y - cell_size),
                                                             cell_size, cell_size, linewidth=1, edgecolor='yellow', facecolor='yellow', alpha=0.5)
                        ax.add_patch(illuminated_cell)

        ax.plot(light_x - cell_size/2, light_y - cell_size/2, 'ys')

# Function to check if a new sprinkler is placed with valid spacing and away from lights
def is_valid_sprinkler_position(x, y, existing_positions):
    for (ex_x, ex_y) in existing_positions:
        distance = np.sqrt((x - ex_x) ** 2 + (y - ex_y) ** 2)
        if distance < min_sprinkler_distance or distance > max_sprinkler_distance:
            return False
    return True

# Sprinklers placement
sprinkler_positions = []

for i in range(2, num_cells_x, 3):  # Adjusting spacing for sprinklers
    for j in range(2, num_cells_y, 3):
        # Sprinkler position (center of the cell)
        sprinkler_x = (i * cell_size) + 300
        sprinkler_y = (j * cell_size) + 300

        # Check if sprinkler is at least 500mm from the walls and not in the same cell as lights
        if (
            sprinkler_x >= wall_clearance and sprinkler_x <= (width - wall_clearance) and
            sprinkler_y >= wall_clearance and sprinkler_y <= (height - wall_clearance)
        ):
            # Ensure sprinkler is not placed in the same cell as a light
            is_conflicting = any(np.linalg.norm(np.array([light_x, light_y]) - np.array([sprinkler_x, sprinkler_y])) < cell_size for light_x, light_y in light_positions)
            if not is_conflicting and is_valid_sprinkler_position(sprinkler_x, sprinkler_y, sprinkler_positions):
                # Add sprinkler position to the list
                sprinkler_positions.append((sprinkler_x, sprinkler_y))

                # Draw sprinkler (red dot)
                ax.plot(sprinkler_x, sprinkler_y, 'ro')

                # Draw sprinkler coverage (blue circle)
                coverage_circle = patches.Circle((sprinkler_x, sprinkler_y), radius=sprinkler_radius, linewidth=1, edgecolor='blue', facecolor='none')
                ax.add_patch(coverage_circle)

# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Set limits for the plot
ax.set_xlim(0, width)
ax.set_ylim(0, height)

# Label the plot
ax.set_title('Hall Layout with Lights and Sprinklers')
ax.set_xlabel('Width (mm)')
ax.set_ylabel('Height (mm)')

# Show the plot
plt.show()
