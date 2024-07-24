import plotly.graph_objects as go
import numpy as np

def create_random_chart():
    #create chart
    np.random.seed(1)

    N = 100
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    sz = np.random.rand(N) * 30

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="markers",
        marker=go.scatter.Marker(
            size=sz,
            color=colors,
            opacity=0.6,
            colorscale="Viridis"
        )
    ))

    return fig

def create_gauge_chart(measured_value, title, reference_value, lower_limit, upper_limit, first_deviation, second_deviation, third_deviation):
    first_lower = reference_value * (1 - first_deviation)
    first_upper = reference_value * (1 + first_deviation)
    second_lower = reference_value * (1 - second_deviation)
    second_upper = reference_value * (1 + second_deviation)
    third_lower =  reference_value * (1 - third_deviation)
    third_upper =  reference_value * (1 + third_deviation)


    fig = go.Figure(go.Indicator(
    domain = {'x': [0, 1], 'y': [0, 1]},
    value = measured_value,
    mode = "gauge+number+delta",
    title = {'text': title, 'font': {'size': 24}},
    delta = {'reference': reference_value},
    gauge = {'axis': {'range': [lower_limit, upper_limit], 'tickwidth': 1, 'tickcolor': "black"},
             'bar': {'color': "black"},
             'steps' : [
                 {'range': [lower_limit, upper_limit], 'color': "darkred"},
                 {'range': [third_lower, third_upper], 'color': "red"},
                 {'range': [second_lower, second_upper], 'color': "yellow"},
                 {'range': [first_lower, first_upper], 'color': "limegreen"}],
             }))
  
    return fig