from dash import Dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = Dash(external_stylesheets=external_stylesheets)

layout_names = {
    'step_button': 'step_button',
    'map_graph': 'map_graph',
    'solve_button': 'solve_button',
    'init_button': 'init_button',
    'placeholder': 'placeholder'
}
