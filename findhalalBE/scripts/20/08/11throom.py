import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches

# Room 1 dimensions
width1 = 4800  # mm
height1 = 5200  # mm

# Cell size for grid
cell_size = 600  # mm

# Sprinkler constraints
sprinkler_radius = 1500  # mm
min_sprinkler_distance = 1500  # mm
max_sprinkler_distance = 1500  # mm
wall_clearance = 500  # mm (distance from walls)

# Define L-shaped room and hall layout
room1_dimensions = [(0, 0), (width1, 0), (width1, height1), (0, height1), 
                    (0, 4000), (3080, 4000), (3080, 2800), (-1800, 2800), 
                    (-1800, 6800), (0, 6800), (0, 4000)]

# Function to check if a point is inside the L-shaped room
def is_inside_room(x, y):
    if (-1800 <= x <= 3080 and 2800 <= y <= 6800):  # L-shaped part check
        return True
    if (0 <= x <= width1 and 0 <= y <= 5200):  # Full room check
        return True

    return False

# Create plot
fig, ax = plt.subplots()

# Plot room boundary
room1_boundary = patches.Polygon(room1_dimensions, closed=True, linewidth=1.8, edgecolor='black', facecolor='none')
ax.add_patch(room1_boundary)

# Add grid lines to visualize the space
for x in np.arange(-1800, width1 + cell_size, cell_size):
    ax.axvline(x=x, color='grey', linestyle='-', linewidth=0.5)
for y in np.arange(-1800, height1 + cell_size + 1200, cell_size):
    ax.axhline(y=y, color='grey', linestyle='-', linewidth=0.5)

light_positions = []
sprinkler_positions = []

# Place lights and draw illuminated areas in room 1
for i in range(-3, (width1 // cell_size) + 3, 3):  # Adjust light spacing
    for j in range(-3, (height1 // cell_size) + 3, 3):
        light_x = i * cell_size + 900
        light_y = j * cell_size + 900
        if is_inside_room(light_x, light_y):  # Ensure light is placed inside the room
            light_positions.append((light_x, light_y))
            ax.plot(light_x, light_y, 'ys')  # Yellow square for lights

            # Illuminate the 8 adjacent cells
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx != 0 or dy != 0:  # Exclude the center cell where the light is
                        illuminated_x = light_x + dx * cell_size
                        illuminated_y = light_y + dy * cell_size
                        if is_inside_room(illuminated_x, illuminated_y):  # Ensure illumination is inside the room
                            illuminated_cell = patches.Rectangle(
                                (illuminated_x - cell_size / 2, illuminated_y - cell_size / 2),
                                cell_size, cell_size, linewidth=1, edgecolor='yellow', facecolor='yellow', alpha=0.3
                            )
                            ax.add_patch(illuminated_cell)

# Function to check if a sprinkler is placed with valid spacing and away from lights
def is_valid_sprinkler_position(x, y, existing_positions):
    for (ex_x, ex_y) in existing_positions:
        distance = np.sqrt((x - ex_x) ** 2 + (y - ex_y) ** 2)
        if distance < min_sprinkler_distance:
            return False
    return True

# Place sprinklers with spacing and conflict check
for i in range(-3, (width1 // cell_size) + 3, 3):
    for j in range(-3, (height1 // cell_size) + 3, 3):
        sprinkler_x = i * cell_size + cell_size / 2
        sprinkler_y = j * cell_size + cell_size / 2
        if is_inside_room(sprinkler_x, sprinkler_y):  # Ensure sprinkler is inside the room
            is_conflicting = any(np.linalg.norm(np.array([light_x, light_y]) - np.array([sprinkler_x, sprinkler_y])) < cell_size for light_x, light_y in light_positions)
            if not is_conflicting and is_valid_sprinkler_position(sprinkler_x, sprinkler_y, sprinkler_positions):
                sprinkler_positions.append((sprinkler_x, sprinkler_y))
                ax.plot(sprinkler_x, sprinkler_y, 'ro')  # Red circle for sprinklers
                coverage_circle = patches.Circle((sprinkler_x, sprinkler_y), radius=sprinkler_radius, linewidth=1, edgecolor='blue', facecolor='none')
                ax.add_patch(coverage_circle)

# Set aspect and limits
ax.set_aspect('equal')
ax.set_xlim(-2000, 6000)
ax.set_ylim(-2000, 7000)

ax.set_title('L-Shaped Room Layout with Lights and Sprinklers')
ax.set_xlabel('Width (mm)')
ax.set_ylabel('Height (mm)')

plt.show()
