import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

room_dimensions = [(0, 0), (4000, 0), (4000, 4800), (5200, 4800), (5200, 4000), (8000, 4000), (8000, 0), (4000, 0)]

grid_size = 600

fig, ax = plt.subplots(figsize=(10, 7))

room_boundary = patches.Polygon(room_dimensions, closed=True, linewidth=2, edgecolor='black', facecolor='none')
ax.add_patch(room_boundary)

min_x = min([point[0] for point in room_dimensions])
max_x = max([point[0] for point in room_dimensions])
min_y = min([point[1] for point in room_dimensions])
max_y = max([point[1] for point in room_dimensions])

for i in range(min_x // grid_size, max_x // grid_size + 1):
    ax.plot([i * grid_size, i * grid_size], [min_y, max_y], color='gray', linestyle='--', linewidth=0.5)
for j in range(min_y // grid_size, max_y // grid_size + 1):
    ax.plot([min_x, max_x], [j * grid_size, j * grid_size], color='gray', linestyle='--', linewidth=0.5)

def place_lights_and_sprinklers():
    lights = []
    sprinklers = []
    grid_lights = np.zeros(((max_x - min_x) // grid_size, (max_y - min_y) // grid_size), dtype=int)
    # print((max_x - min_x) )
    # print((max_y - min_y) // grid_size)
    # print(grid_lights,"grid_lights")
    
    for i in range(min_x // grid_size, max_x // grid_size):
            # j = i
            # print("j",j)
        for j in range(min_y // grid_size, max_y // grid_size):
            x_center = (i + 0.2) * grid_size
            y_center = (j + 0.2) * grid_size

           
            if patches.Polygon(room_dimensions).contains_point((x_center, y_center)):
                if (i + j) % 2 == 0 and grid_lights[i, j] == 0:
                    if x_center >= min_x + 500 and x_center <= max_x - 500 and y_center >= min_y + 500 and y_center <= max_y - 500:
                        lights.append((x_center, y_center))
                        # print("lights",lights)
                        grid_lights[i, j] = 1                    
                        light_square = patches.Rectangle((x_center - grid_size / 2, y_center - grid_size / 2), grid_size, grid_size, linewidth=1, edgecolor='orange', facecolor='yellow', alpha=0.3)
                        print("light_square",light_square)
                        ax.add_patch(light_square)
                        ax.plot(x_center, y_center, 'ys')

                
                if (i + j) % 3 == 0 and grid_lights[i, j] == 0:
                    if x_center >= min_x + 500 and x_center <= max_x - 500 and y_center >= min_y + 500 and y_center <= max_y - 500:
                        sprinklers.append((x_center, y_center))
                        grid_lights[i, j] = 2                    
                        sprinkler_dot = patches.Circle((x_center, y_center), radius=50, color='red')
                        coverage_circle = patches.Circle((x_center, y_center), radius=1500, linewidth=1, edgecolor='blue', facecolor='none')
                        # ax.add_patch(sprinkler_dot)
                        ax.plot(x_center, y_center, 'ro')
                        ax.add_patch(coverage_circle)

    return lights, sprinklers

lights, sprinklers = place_lights_and_sprinklers()

ax.set_xlim(min_x - grid_size, max_x + grid_size)
ax.set_ylim(min_y - grid_size, max_y + grid_size)
ax.set_aspect('equal')

plt.show()
