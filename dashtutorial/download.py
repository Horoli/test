import dash
from dash.dependencies import Output, Input
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

app = dash.Dash(prevent_initial_callbacks=True)
df = pd.read_csv('https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Bootstrap/Side-Bar/iranian_students.csv')

app.layout = html.Div([
    html.Button('Download CSV', id='btn_csv'),
    dcc.Download(id='download-dataframe-csv')
])

@app.callback(
    Output('download-dataframe-csv', 'data'),
    Input('btn_csv', 'n_clicks'),
    prevent_initial_call=True
)
def download(n_clicks):
    return dcc.send_data_frame(df.to_csv, 'mydf.csv')

if __name__ == '__main__':
    app.run_server()