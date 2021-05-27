import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

all_options = {
    'America': ['Newyork','Sanfransisco','Cincinati'],
    'Canada': ['Montreal', 'Toronto', 'Ottawa']}

saerch_bar = dbc.Row([
    dbc.Col(dbc.Input(type='search', placeholder='Search')),
    dbc.Col(dbc.Button('Search', color='primary',className='ml-2'), width='auto')],
    no_gutters=True,
    className='ml-auto flex-nowrap mt-3 mt-md-0',
    align='center')

app.layout = html.Div([
    dcc.RadioItems(
        id='countries-radio',
        options=[{'label':k, 'value':k} for k in all_options.keys()],
        value='America'
    ),

    html.Hr(),

    dcc.RadioItems(id='cities-radio'),

    html.Hr(),
    html.Div(id='display-selected-values')
])

@app.callback(Output('navbar-collapse', 'is_open'),
              [Input('navbar-toggler','n_clicks')],
              [State('navbar-collapse', 'is_open')])
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output('cities-radio', 'options'),
    Input('countries-radio', 'value'))
def set_cities_options(selected_country):
    return [{'label':i, 'value':i} for i in all_options[selected_country]]

@app.callback(
    Output('cities-radio', 'value'),
    Input('cities-radio', 'options'))
def set_cities_value(available_options):
    return available_options[0]['value']

@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'))
def set_display_children(selected_country, selected_city):
    return f'{selected_city} is a city in {selected_country}'

if __name__ =='__main__':
    app.run_server()