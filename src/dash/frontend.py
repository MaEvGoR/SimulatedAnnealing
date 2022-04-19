from dash import html, dcc, dash_table
from src.dash.config import layout_names

layout = html.Div(
    [
        html.Button(
            'Step',
            id=layout_names['step_button'],
            n_clicks=0
        ),
        html.Button(
            'Init',
            id=layout_names['init_button'],
            n_clicks=0
        ),
        html.Button(
            'Solve',
            id=layout_names['solve_button'],
            n_clicks=0
        ),
        html.H1(
            title='Hello Dash',
            id=layout_names['placeholder']
        ),
        dcc.Graph(
            id=layout_names['map_graph']
        )
    ]
)
