import matplotlib.pyplot as plt
import numpy as np

# Room dimensions in mm (assuming from the document and general room size)
room_width = 4800  # Room width in mm
room_length = 5200  # Room length in mm

# Tile size
tile_size = 600  # Each ceiling tile is 600x600 mm

# Calculate the number of tiles along width and length
num_tiles_width = room_width // tile_size
num_tiles_length = room_length // tile_size

# Plot initialization
fig, ax = plt.subplots(figsize=(12, 10))
ax.set_xlim(0, room_width)
ax.set_ylim(0, room_length)
ax.set_aspect('equal')
ax.set_title("Room Layout with Sprinklers and Lights")

# Draw the grid
for i in range(num_tiles_width + 1):
    ax.plot([i * tile_size, i * tile_size], [0, room_length], color='gray')
for i in range(num_tiles_length + 1):
    ax.plot([0, room_width], [i * tile_size, i * tile_size], color='gray')


# List to store the positions of lights
lights = []

# Iterate over grid cells to place lights
for i in range(0, num_tiles_width, 2):  # Skipping adjacent cells
    for j in range(0, num_tiles_length, 2):
        # Place a light at the center of the tile
        light_x = (i + 0.5) * tile_size
        light_y = (j + 0.5) * tile_size
        
        # Add light to the list
        lights.append((light_x, light_y))
        
        # Draw the light as a yellow square
        ax.add_patch(plt.Rectangle((light_x - tile_size/2, light_y - tile_size/2), tile_size, tile_size, color='yellow', alpha=0.3))

# Plot the lights' positions
for (lx, ly) in lights:
    ax.plot(lx, ly, 'ys')  # Yellow square at the center


# List to store the positions of sprinklers
sprinklers = []

# Minimum distance from walls (in mm) and other sprinklers
min_wall_distance = 500
min_sprinkler_distance = 1200
max_sprinkler_distance = 1500

# Iterate over the grid to place sprinklers
for i in range(1, num_tiles_width - 1):
    for j in range(1, num_tiles_length - 1):
        # Calculate the center of the current tile
        sprinkler_x = (i + 0.5) * tile_size
        sprinkler_y = (j + 0.5) * tile_size
        
        # Check the minimum distance requirements
        if sprinkler_x > min_wall_distance and sprinkler_x < room_width - min_wall_distance and \
           sprinkler_y > min_wall_distance and sprinkler_y < room_length - min_wall_distance:
            # Ensure this sprinkler is not too close to another one
            too_close = False
            for (sx, sy) in sprinklers:
                distance = np.sqrt((sprinkler_x - sx)**2 + (sprinkler_y - sy)**2)
                if distance < min_sprinkler_distance or distance > max_sprinkler_distance:
                    too_close = True
                    break

            if not too_close:
                # Place the sprinkler
                sprinklers.append((sprinkler_x, sprinkler_y))
                
                # Draw the sprinkler as a red dot
                ax.plot(sprinkler_x, sprinkler_y, 'ro')
                # Draw the sprinkler coverage as a blue circle
                coverage_radius = 1500  # mm
                sprinkler_circle = plt.Circle((sprinkler_x, sprinkler_y), coverage_radius, color='blue', fill=False, linestyle='--')
                ax.add_patch(sprinkler_circle)

# Show the plot
plt.show()
