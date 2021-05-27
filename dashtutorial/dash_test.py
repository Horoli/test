import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_table
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from wordcloud import WordCloud

df = pd.read_csv('../dashboard/concat_df.csv', index_col='Unnamed: 0')

# 데이터프레임 전체 조회 함수
def generate_table(dataframe, max_rows=5):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns]) ),
        html.Tbody([
            html.Tr([ html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
                      ]) for i in range(min(len(dataframe), max_rows)) ]) ])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.GRID])
fig = px.bar(df, x='categories', y='target_amounts', width=800, height=400)
# default_fig.update_layout(parper_bgcolor='LightSteelBlue')
# wordcloud = WordCloud(background_color='w', width=50, height=50).generate((''.join(df['categories'])))

# 레이어 설정
app.layout = html.Div([
    html.H1('Dashboards', style={'text-align':'center'}),
    html.H4('카테고리별 데이터 현황'),
    dcc.Dropdown(id='slct_cate',
                 options=[
                     {'label':'전체', 'value':'전체'},
                     {'label':'뷰티', 'value':'뷰티'},
                     {'label':'출판', 'value':'출판'}],
                 multi=False,
                 value='전체',
                 style={'width':'40%'}),
    html.Br(),
    html.Div([
        dbc.Row(dbc.Col(html.Div(id='output_container'))),
        dbc.Row([
            dbc.Col(html.Div(id='output_container_info')),
            dbc.Col(html.Div(id='output_container_mean')),
            dbc.Col(html.Div('asd'))
        ])
    ]),
    html.P("Fig"),
    dcc.Slider(id='width', min=200, max=500, step=25, value=300,marks={x:str(x) for x in [200, 300, 400, 500]}),
    dcc.Graph(id='wadiz_graph', figure=fig),
    # generate_table(df)
])

app.row = html.Div([
    dbc.Row(dbc.Col(html.Div('A single, half-width column'), width=6))
])

@app.callback(
    [Output('output_container', 'children'),
    Output('output_container_info', 'children'),
    Output('output_container_mean', 'children'),
    Output('wadiz_graph', 'figure')],
    [Input('slct_cate', 'value')]
)
def update_graph(option_slct):
    dff = df.copy()
    dff = dff[dff['categories'] == option_slct]
    time = dff[dff['categories'] == option_slct]['time'].mean()
    mean_targetprice = dff[dff['categories'] == option_slct]['target_amounts'].mean()

    if option_slct == '전체':
        fig = px.bar(df, x='categories', y='target_amounts', width=800, height=400)
        time = df['time'].mean()
        mean_targetprice = df['target_amounts'].mean()
    else :
        fig = px.bar(dff, x='categories', y='target_amounts', width=800, height=400)
    container = '{} 카테고리에 대한 정보입니다. '.format(option_slct)
    information = '평균 펀딩기간 : {}일'.format(time)
    mean_price = '평균 목표금액 : {}원'.format(mean_targetprice)
    return container, information, mean_price, fig

if __name__ == '__main__':
    app.run_server()