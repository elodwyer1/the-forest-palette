# mycolors/__init__.py
from .palette import CUSTOM_PALETTE

def register_custom_colors():
    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    # Registering custom color dictionary
    for name, color in CUSTOM_PALETTE.items():
        plt.rcParams[f'axes.prop_cycle'] = plt.cycler(color=CUSTOM_PALETTE.values())


def set_custom_color_scheme():
    import matplotlib.pyplot as plt
    plt.style.use('ggplot')
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=CUSTOM_PALETTE.values())
