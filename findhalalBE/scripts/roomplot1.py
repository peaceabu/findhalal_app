import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 8))

# Add the outer walls using Rectangle (L-shaped room layout)
outer_wall_1 = patches.Rectangle((0, 0), 4.8, 4, edgecolor='black', facecolor='none', linewidth=2)
outer_wall_2 = patches.Rectangle((4.8, 2.8), 1.2, 2.4, edgecolor='black', facecolor='none', linewidth=2)

# Add the inner wall to separate rooms
inner_wall = patches.Rectangle((0, 1.2), 4.8, 1.6, edgecolor='black', facecolor='none', linewidth=2)

# Add the room elements like sprinklers and lights
# Sprinkler (drawn as a circle)
sprinkler = patches.Circle((1.8, 3.2), 0.6, edgecolor='blue', facecolor='none', linewidth=1.5)
sprinkler_center = patches.Circle((1.8, 3.2), 0.05, color='red')  # Center of the sprinkler

# Light (drawn as a square)
light = patches.Rectangle((4.2, 2.4), 0.6, 0.6, edgecolor='black', facecolor='yellow', alpha=0.3)
light_center = patches.Rectangle((4.5, 2.7), 0.1, 0.1, color='black')  # Center of the light

# Add patches to the plot
ax.add_patch(outer_wall_1)
ax.add_patch(outer_wall_2)
ax.add_patch(inner_wall)
ax.add_patch(sprinkler)
ax.add_patch(sprinkler_center)
ax.add_patch(light)
ax.add_patch(light_center)

# Add text annotations
ax.text(1.8, 3.8, 'WALL', ha='center', va='center')
ax.text(1.8, 2.0, 'CEILING', ha='center', va='center')
ax.text(4.2, 1.4, 'CEILING', ha='center', va='center')
ax.text(1.8, 3.2, 'sprinkler', ha='center', va='center', fontsize=8)
ax.text(4.5, 2.7, 'light', ha='center', va='center', fontsize=8)

# Set limits and aspect ratio
ax.set_xlim(-1, 7)
ax.set_ylim(-1, 7)
ax.set_aspect('equal')

# Display grid lines to represent the ceiling tiles
ax.grid(True, which='both', linestyle='--', linewidth=0.5)

# Add axis labels
ax.set_xlabel('Width (meters)')
ax.set_ylabel('Height (meters)')

# Hide axis ticks
ax.set_xticks([])
ax.set_yticks([])

# Show the plot
plt.show()
