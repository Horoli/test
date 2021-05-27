import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"
df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

def generate_table(dataframe, max_rows=5):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns]) ),
        html.Tbody([
            html.Tr([ html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                      ]) for i in range(min(len(dataframe), max_rows)) ]) ])

SIDEBAR_STYLE = {
    'position':'fixed',
    'top':0,
    'left':0,
    'bottom':0,
    'width':'16rem',
    'padding':'4rem 1rem',
    'background-color':'primary'
}

CONTENT_STYLE = {
    'margin-left':'18rem',
    'margin-right':'2rem',
    'padding':'2rem 1rem'
}

sidebar = html.Div([
    html.H2('OOOA', className='display-4'),
    html.Hr(),
    html.P('Number of students per education', className='lead'),
    dbc.Nav([
        dbc.NavLink('Home', href='/', active='exact'),
        dbc.NavLink('page1', href='/page-1', active='exact'),
        dbc.NavLink('page2', href='/page-2', active='exact'),
        dbc.NavLink('page3', href='/page-3', active='exact'),
        dbc.NavLink('Dataframe', href='/dataframe', active='exact')
    ],
    vertical=True,
    pills=True),
],
style=SIDEBAR_STYLE)

search_bar = dbc.Row([
    dbc.Col(dbc.Input(type='search', placeholder='Search')),
    dbc.Col(dbc.Button('Search', color='primary',className='ml-2'), width='auto')],
    no_gutters=True,
    className='ml-auto flex-nowrap mt-3 mt-md-0',
    align='center')

navbar = html.Div([
    dbc.Navbar([
       html.A(
           dbc.Row([
               dbc.Col(html.Img(src=PLOTLY_LOGO, height='30px')),
               dbc.Col(dbc.NavbarBrand('Navbar', className='ml-2')),
           ], align='center', no_gutters=True),
           href='https://plot.ly',
       ),
        dbc.NavbarToggler(id='navbar-toggler'),
        # dbc.Collapse(search_bar, id='navbar-collapse', navbar=True),
    ])
])

content = html.Div(id='page-content', children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id='url'),
    navbar,
    sidebar,
    content
])

@app.callback(
    Output('page-content','children'),
    [Input('url','pathname')])
def render_page_content(pathname):
    # 최초경로 출력
    if pathname =='/':
        return [
            dbc.Jumbotron([

            ])
        ]
    elif pathname =='/page-1':
        return [
                html.H1('kindergarten in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                          figure=px.bar(df, barmode='group', x='Years',
                                        y=['Girls Kindergarten', 'Boys Kindergarten']))
        ]
    # 페이지1 출력
    elif pathname == '/page-2':
        return [
                html.H1('Grad School in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                          figure=px.bar(df, barmode='group', x='Years',
                                        y=['Girls Grade School', 'Boys Grade School']))

        ]
    # 페이지2 출력
    elif pathname == '/page-3':
        return [
                html.H1('High School in Iran',
                        style={'textAlign':'center'}),
                dcc.Graph(id='bargraph',
                          figure=px.bar(df, barmode='group', x='Years',
                                        y=['Girls High School', 'Boys High School']))
        ]

    elif pathname == '/dataframe':
        return [
                html.Div([
                    dbc.Button('Download CSV', id='btn_csv', color='primary', style={'margin':'1rem'}),
                    dcc.Download(id='download-dataframe-csv'),
                dbc.Table(generate_table(df),
                          bordered=True,
                          dark=True,
                          hover=True,
                          responsive=True,
                          striped=True),
                ])
        ]
    # 에러메세지 발생
    return dbc.Jumbotron([
        html.H1('404:not found', className='text-danger'),
        html.Hr(),
        html.P(f'The pathname {pathname} was not recognised..')
    ])
# dataframe csv 다운로드
@app.callback(
    Output('download-dataframe-csv', 'data'),
    Input('btn_csv', 'n_clicks'),
    prevent_initial_call=True)
def download(n_clicks):
    return dcc.send_data_frame(df.to_csv, 'mydf.csv')

if __name__ =='__main__':
    app.run_server()