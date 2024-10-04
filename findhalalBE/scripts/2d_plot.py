import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

def draw_cube(ax, center=(0, 0, 0), size=2, face_color='cyan', edge_color='r'):
    """
    Draws a 3D cube on the provided axes.
    
    Parameters:
    - ax: The 3D axes to draw the cube on.
    - center: A tuple (x, y, z) representing the center of the cube.
    - size: The length of the sides of the cube.
    - face_color: The color of the cube's faces.
    - edge_color: The color of the cube's edges.
    """
    # Half size of the cube for positioning vertices around the center
    half_size = size / 2

    # Calculate vertices based on center and size
    vertices = np.array([
        [center[0] - half_size, center[1] - half_size, center[2] - half_size],  # Vertex 0
        [center[0] + half_size, center[1] - half_size, center[2] - half_size],  # Vertex 1
        [center[0] + half_size, center[1] + half_size, center[2] - half_size],  # Vertex 2
        [center[0] - half_size, center[1] + half_size, center[2] - half_size],  # Vertex 3
        [center[0] - half_size, center[1] - half_size, center[2] + half_size],  # Vertex 4
        [center[0] + half_size, center[1] - half_size, center[2] + half_size],  # Vertex 5
        [center[0] + half_size, center[1] + half_size, center[2] + half_size],  # Vertex 6
        [center[0] - half_size, center[1] + half_size, center[2] + half_size]   # Vertex 7
    ])

    # Define the six faces of the cube using the vertices
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],  # Bottom face
        [vertices[4], vertices[5], vertices[6], vertices[7]],  # Top face
        [vertices[0], vertices[1], vertices[5], vertices[4]],  # Front face
        [vertices[2], vertices[3], vertices[7], vertices[6]],  # Back face
        [vertices[1], vertices[2], vertices[6], vertices[5]],  # Right face
        [vertices[0], vertices[3], vertices[7], vertices[4]]   # Left face
    ]

    # Draw the cube using Poly3DCollection
    ax.add_collection3d(Poly3DCollection(faces, facecolors=face_color, linewidths=1, edgecolors=edge_color, alpha=0.5))

# Create a figure and 3D axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_title("3D Dynamic Cube Plot")

# Draw a cube with dynamic parameters
draw_cube(ax, center=(0, 0, 0), size=4, face_color='lightblue', edge_color='black')

# Set limits to provide a good view of the cube
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Display the plot
plt.show()
