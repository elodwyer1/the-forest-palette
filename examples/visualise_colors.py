import matplotlib.pyplot as plt
import numpy as np
from the_forest_palette import forest_colors
import os

def plot_color_grid_with_labels(forest_colors, grid_size=None):
    # Determine the grid size if not provided
    if grid_size is None:
        num_colors = len(forest_colors)
        grid_size = int(np.ceil(np.sqrt(num_colors)))

    fig, ax = plt.subplots(figsize=(10, 10))

    # Get the total number of colors and calculate the spacing
    num_colors = len(forest_colors)
    padding = 1.5  # Increased padding to provide more space between circles
    circle_radius = 0.4
    text_offset = 0.7  # Adjust the text offset to place it well below the circle
    x, y = np.meshgrid(range(grid_size), range(grid_size))

    # Flatten the grid positions
    x = x.flatten()
    y = y.flatten()

    for i, (color_name, color_hex) in enumerate(forest_colors.items()):
        if i < len(x):
            circle = plt.Circle((x[i] * padding + padding / 2, y[i] * padding + padding / 2), circle_radius, color=color_hex, edgecolor='black')
            ax.add_patch(circle)
            # Place the text below the circle
            ax.text(x[i] * padding + padding / 2, y[i] * padding + padding / 2 - text_offset, color_name, ha='center', va='center', fontsize=10, fontweight='bold')

    ax.set_aspect('equal')
    ax.set_xlim(0, grid_size * padding)
    ax.set_ylim(0, grid_size * padding)
    ax.axis('off')

    plt.title('The Forest Palette - Color Grid with Filled Circles and Labels', fontsize=14, fontweight='bold')
    plt.tight_layout()
    save_path = os.path.join(os.path.dirname(__file__), '../color_grid.png')
    fig.savefig(save_path)


# Call the function to plot the colors
plot_color_grid_with_labels(forest_colors)

