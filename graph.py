# produced with ChatGPT 5.3
import numpy as np
import plotly.graph_objects as go


def create_wave_plot():
    # Generate data
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    y2 = np.cos(x)

    # Create Plotly figure
    fig = go.Figure()

    # Add sine wave
    fig.add_trace(
        go.Scatter(
            x=x, y=y, mode="lines", name="sin(x)", line=dict(color="blue", width=2)
        )
    )

    # Add cosine wave
    fig.add_trace(
        go.Scatter(
            x=x,
            y=y2,
            mode="lines",
            name="cos(x)",
            line=dict(color="red", width=2, dash="dash"),
        )
    )

    # Layout customization
    fig.update_layout(
        title="Sine and Cosine Waves (From External Module)",
        xaxis_title="X-axis",
        yaxis_title="Y-axis",
        template="plotly_white",
        legend=dict(title="Functions"),
    )

    # Optional grid styling
    fig.update_xaxes(showgrid=True, gridwidth=0.5)
    fig.update_yaxes(showgrid=True, gridwidth=0.5)

    return fig
