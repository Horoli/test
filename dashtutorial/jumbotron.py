import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    dbc.Jumbotron([
        html.H1('Jumbotron', className='display-3'),
        html.P('asdasdasdasdasdasdasdasdasdasdasd'
               'asdasdasdasdasdasdasdasdasdasdasd',
               className='lead'),
        html.Hr(className='my-2'),
        html.P('asdasdasdasdasdasdasdasdasdasdasd'
               'asdasdasdasdasdasdasdasdasdasdasd'),
        html.P(dbc.Button('Learn more', color='primary', className='lead'))],
        style={'width': '48%', 'background-color': 'primary', 'padding': '50px'}),
])


if __name__ =='__main__':
    app.run_server()