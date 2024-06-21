# mycolors/__init__.py
from .palette import CUSTOM_PALETTE as forest_colors

def register_custom_colors():
    import matplotlib.pyplot as plt

    # Registering custom color dictionary
    plt.rcParams[f'axes.prop_cycle'] = plt.cycler(color=forest_colors.values())


def set_custom_color_scheme():
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=forest_colors.values())
