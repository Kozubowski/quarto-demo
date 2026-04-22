import numpy as np
import matplotlib.pyplot as plt


def create_wave_plot():
    # Generate data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    y2 = np.cos(x)

    # Create the figure and axis objects
    fig, ax = plt.subplots(figsize=(8, 4))

    # Plot the data
    ax.plot(x, y, color="blue", label="sin(x)", linewidth=2)
    ax.plot(x, y2, color="red", label="cos(x)", linestyle="dashed", linewidth=2)

    # Customize the plot
    ax.set_title("Sine and Cosine Waves (From External Module)")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.legend()
    ax.grid(True, alpha=0.5)

    # Return the figure object
    return fig
