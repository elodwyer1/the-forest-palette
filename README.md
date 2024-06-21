# the-forest-palette

`the-forest-palette` is a Python package that provides custom color palettes for use with Matplotlib. If you are inspired by
the beautiful, foresty greens of Ireland, you might be interested in using this palette.

# The Colors

![Color Grid](../color_grid.png)

## Installation

pip install the-forest-palette

## Usage

    import matplotlib.pyplot as plt
    from the_forest_palette import register_custom_colors, set_custom_color_scheme, forest_colors

    # Register custom colors
    register_custom_colors()

    # Set custom color scheme
    set_custom_color_scheme()

    # Create a plot
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()



