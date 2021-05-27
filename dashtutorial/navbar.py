import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

search_bar = dbc.Row([
    dbc.Col(dbc.Input(type='search', placeholder='Search')),
    dbc.Col(dbc.Button('Search', color='primary',className='ml-2'), width='auto')],
    no_gutters=True,
    className='ml-auto flex-nowrap mt-3 mt-md-0',
    align='center')

app.layout = html.Div([
    dbc.Navbar([
       html.A(
           dbc.Row([
               dbc.Col(html.Img(src=PLOTLY_LOGO, height='30px')),
               dbc.Col(dbc.NavbarBrand('Navbar', className='ml-2')),
           ], align='center', no_gutters=True),
           href='https://plot.ly',
       ),
        dbc.NavbarToggler(id='navbar-toggler'),
        dbc.Collapse(search_bar, id='navbar-collapse', navbar=True),
    ])
])

if __name__ =='__main__':
    app.run_server()