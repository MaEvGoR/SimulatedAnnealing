import plotly.express as px
from dash import callback_context

from src.algorithm.simulated_annealing import algo
from src.data.city_data import data
from src.dash.config import layout_names


def registerClick(num_click_step, num_clicks_solve, num_clicks_init):
    changed_id = [p['prop_id'] for p in callback_context.triggered][0]
    if layout_names['step_button'] in changed_id:
        return stepClick(num_click_step)
    elif layout_names['solve_button'] in changed_id:
        return solveClick(num_clicks_solve)
    elif layout_names['init_button'] in changed_id:
        return initClick(num_clicks_init)
    else:
        return defaultPlot()

def stepClick(num_clicks):
    if num_clicks == 0:
        pass
    else:
        algo.step()
        return algo.figure(), algo.summary()

def solveClick(num_clicks):
    if num_clicks == 0:
        pass
    else:
        # solve button clicked
        algo.solve()
        return algo.figure(), algo.summary()

def initClick(num_clicks):
    if num_clicks == 0:
        pass
    else:
        # init button clicked
        algo.setup(data)
        return algo.figure(), algo.summary()

def defaultPlot():
    df = px.data.gapminder().query("country=='Canada'")
    fig = px.line(df, x="year", y="lifeExp")
    return fig, 'No graph yet'
