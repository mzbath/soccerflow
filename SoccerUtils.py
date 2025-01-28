import plotly.graph_objects as go

class Soccer():
    def __init__(self):
        pass

    def draw_soccer_pitch(self):

        # Define pitch dimensions
        pitch_length = 120
        pitch_width = 80
        half_length = pitch_length / 2
        half_width = pitch_width / 2

        # Create the figure
        fig = go.Figure()

        # Add the pitch outline
        fig.add_shape(type="rect",
                    x0=0, y0=0, x1=pitch_length, y1=pitch_width,
                    line=dict(color="black", width=2))

        # Add the half-line
        fig.add_shape(type="line",
                    x0=half_length, y0=0, x1=half_length, y1=pitch_width,
                    line=dict(color="black", width=2))

        # Add center circle
        fig.add_shape(type="circle",
                    x0=half_length - 10, y0=half_width - 10,
                    x1=half_length + 10, y1=half_width + 10,
                    line=dict(color="black", width=2))

        # Add penalty areas (example dimensions)
        penalty_area_length = 18
        penalty_area_width = 44

        # Left penalty area
        fig.add_shape(type="rect",
                    x0=0, y0=(pitch_width - penalty_area_width) / 2,
                    x1=penalty_area_length, y1=(pitch_width + penalty_area_width) / 2,
                    line=dict(color="black", width=2))

        # Right penalty area
        fig.add_shape(type="rect",
                    x0=pitch_length - penalty_area_length, y0=(pitch_width - penalty_area_width) / 2,
                    x1=pitch_length, y1=(pitch_width + penalty_area_width) / 2,
                    line=dict(color="black", width=2))

        # Add goals
        goal_width = 8
        goal_depth = 2

        # Left goal
        fig.add_shape(type="rect",
                    x0=-goal_depth, y0=(pitch_width - goal_width) / 2,
                    x1=0, y1=(pitch_width + goal_width) / 2,
                    line=dict(color="black", width=2))

        # Right goal
        fig.add_shape(type="rect",
                    x0=pitch_length, y0=(pitch_width - goal_width) / 2,
                    x1=pitch_length + goal_depth, y1=(pitch_width + goal_width) / 2,
                    line=dict(color="black", width=2))

        # Customize layout
        fig.update_layout(
            # title="Soccer Pitch",
            xaxis=dict(
                range=[-5, pitch_length + 5],
                showgrid=False,
                zeroline=False,
                showticklabels=False
            ),
            yaxis=dict(
                range=[-5, pitch_width + 5],
                showgrid=False,
                zeroline=False,
                showticklabels=False
            ),
            width=800,
            height=600,
            plot_bgcolor="white",
            margin=dict(l=10, r=10, t=30, b=10),
        )

        # return the pitch
        return fig

