import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Room 1 dimensions
width1 = 4800  # mm
height1 = 5200  # mm

# Room 2 dimensions
width2 = 3000  # mm
height2 = 4000  # mm

cell_size = 600  # mm
fine_cell_size = 600  # mm (You can adjust this to make it even finer)

# Sprinkler constraints
sprinkler_radius = 1500  # mm
min_sprinkler_distance = 1200  # mm
max_sprinkler_distance = 1500  # mm
wall_clearance = 500  # mm (distance from walls)

# Create the plot
fig, ax = plt.subplots()

# Define room 1 boundaries
room1_dimensions = [(0, 0), (width1, 0), (width1, height1), (0, height1), (0, 4000), (3080, 4000), (3080, 2800), (-1800, 2800), (-1800, 6800), (0, 6800), (0, 4000)]
room1_boundary = patches.Polygon(room1_dimensions, closed=True, linewidth=3, edgecolor='red', facecolor='none')
ax.add_patch(room1_boundary)

# Generate grid lines within the red area
for x in np.arange(-1800, 4800 + cell_size, cell_size):
    ax.axvline(x=x, color='black', linestyle='-', linewidth=1)
for y in np.arange(2800, 6800 + cell_size, cell_size):
    ax.axhline(y=y, color='black', linestyle='-', linewidth=1)

# Overlay finer grid within the red area
for x in np.arange(-1800, 4800 + fine_cell_size, fine_cell_size):
    ax.axvline(x=x, color='gray', linestyle='--', linewidth=0.5)
for y in np.arange(2800, 6800 + fine_cell_size, fine_cell_size):
    ax.axhline(y=y, color='gray', linestyle='--', linewidth=0.5)

# Lights and sprinklers positions for room 1
light_positions = []
sprinkler_positions = []

# Place lights and draw illuminated areas within the red area
for i in range(1, (width1 + 1800) // cell_size, 3):  # Space lights to prevent adjacency
    for j in range(1, (height1 - 2800) // cell_size, 3):
        light_x = (i * cell_size) + 600
        light_y = (j * cell_size) + 2800
        light_positions.append((light_x - cell_size / 2, light_y - cell_size / 2))

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx != 0 or dy != 0:
                    illuminated_x = light_x + dx * cell_size
                    illuminated_y = light_y + dy * cell_size
                    if -1800 <= illuminated_x - cell_size < 4800 and 2800 <= illuminated_y - cell_size < 6800:
                        illuminated_cell = patches.Rectangle((illuminated_x - cell_size, illuminated_y - cell_size),
                                                             cell_size, cell_size, linewidth=1, edgecolor='yellow', facecolor='yellow', alpha=0.5)
                        ax.add_patch(illuminated_cell)

        ax.plot(light_x - cell_size / 2, light_y - cell_size / 2, 'ys')

# Function to check if a new sprinkler is placed with valid spacing and away from lights
def is_valid_sprinkler_position(x, y, existing_positions):
    for (ex_x, ex_y) in existing_positions:
        distance = np.sqrt((x - ex_x) ** 2 + (y - ex_y) ** 2)
        if distance < min_sprinkler_distance or distance > max_sprinkler_distance:
            return False
    return True

# Sprinklers placement for room 1 within the red area
for i in range(2, (width1 + 1800) // cell_size, 3):  # Adjusting spacing for sprinklers
    for j in range(2, (height1 - 2800) // cell_size, 3):
        sprinkler_x = (i * cell_size) + 300
        sprinkler_y = (j * cell_size) + 2800

        if (
                -1800 + wall_clearance <= sprinkler_x <= (width1 - wall_clearance) and
                2800 + wall_clearance <= sprinkler_y <= (height1 - wall_clearance)
        ):
            is_conflicting = any(np.linalg.norm(np.array([light_x, light_y]) - np.array([sprinkler_x, sprinkler_y])) < cell_size for light_x, light_y in light_positions)
            if not is_conflicting and is_valid_sprinkler_position(sprinkler_x, sprinkler_y, sprinkler_positions):
                sprinkler_positions.append((sprinkler_x, sprinkler_y))
                ax.plot(sprinkler_x, sprinkler_y, 'ro')
                coverage_circle = patches.Circle((sprinkler_x, sprinkler_y), radius=sprinkler_radius, linewidth=1, edgecolor='blue', facecolor='none')
                ax.add_patch(coverage_circle)

# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Set limits for the plot
ax.set_xlim(-2000, 6000)  # Adjusting limits to fit both rooms
ax.set_ylim(-2000, 7000)

# Label the plot
ax.set_title('Room Layout with Two Rooms, Lights, and Sprinklers')
ax.set_xlabel('Width (mm)')
ax.set_ylabel('Height (mm)')

# Show the plot
plt.show()