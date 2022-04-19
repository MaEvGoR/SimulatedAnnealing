from dash import Input, Output

from src.dash.frontend import layout
from src.dash.config import app, layout_names
from src.dash.callbacks import registerClick

# maybe app creation should be right on this line

def get_app():
    app.callback(
        Output(layout_names['map_graph'], 'figure'),
        Output(layout_names['placeholder'], 'children'),
        Input(layout_names['step_button'], 'n_clicks'),
        Input(layout_names['solve_button'], 'n_clicks'),
        Input(layout_names['init_button'], 'n_clicks'),
    )(registerClick)

    app.layout = layout
    return app
