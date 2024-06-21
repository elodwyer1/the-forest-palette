# the-forest-palette

`the-forest-palette` is a Python package that provides custom color palettes for use with Matplotlib. If you are inspired by
the beautiful, foresty greens of Ireland, you might be interested in using this palette.

# The Colors
"deepestgreen": "#080C07",
"richdarkgreen": "#284021",
"mintyforest": "#658F59",
"softapple": "#9FD390",
"cooldarkgreen": "#405947",
"brightmint": "#B7E6D4",
"softmint": "#8EB8A8",
"curiousapple": "#76BE5E",
"ashmint"

## Installation

pip install the-forest-palette

python
Copy code

## Usage

    python
    import matplotlib.pyplot as plt
    from the_forest_palette import register_custom_colors, set_custom_color_scheme

    # Register custom colors
    register_custom_colors()

    # Set custom color scheme
    set_custom_color_scheme()

    # Create a plot
    plt.plot([1, 2, 3], [4, 5, 6])
    plt.show()



