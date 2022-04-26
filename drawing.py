import plotly.graph_objs as go

HEIGHT = 950
WIDTH = 1200


def get_formula(f_t):
    formula = ""
    if f_t.amplitude != 1:
        formula += str(f_t.amplitude)
    formula += "sin("
    formula += str(f_t.frequency)
    formula += "t"
    if f_t.phase_shift != 0:
        formula += " + " + str(f_t.phase_shift)
    formula += ")"
    return formula


def draw(x_list, y_list, x_t, y_t):
    x_form = get_formula(x_t)
    y_form = get_formula(y_t)

    scatter = go.Scatter(x=x_list, y=y_list)

    fig = go.Figure()

    fig.add_trace(scatter)
    fig.update_traces(
        marker=dict(color="Black"),
        mode="lines",
        showlegend=True,
        name="x(t) = " + x_form + "<br>" + "y(t) = " + y_form
    )

    fig.update_layout(
        height=HEIGHT,
        width=WIDTH,
        yaxis_range=(-1*y_t.amplitude, y_t.amplitude),
        xaxis_range=(-1*x_t.amplitude, x_t.amplitude),
        title=dict(font=dict(size=30, family="Times New Roman", color="Black"), text="Lissajous Figures Model"),
        margin=dict(b=30, l=100, r=150, t=90),
        plot_bgcolor="White",
        paper_bgcolor="White",
        legend=dict(font=dict(size=30, family="Times New Roman")),
        updatemenus=[dict(buttons=[dict(
            args=[None, {"frame": {"duration": 1, "redraw": False}}],
            label="Play",
            method="animate")],
            type='buttons',
            y=1,
            x=-0.1,
            xanchor='left',
            yanchor='top')]
    )

    frames = [go.Frame(data=[go.Scatter(x=x_list[:i], y=y_list[:i])]) for i in range(0, len(x_list))]
    fig.update(frames=frames)

    fig.show()


