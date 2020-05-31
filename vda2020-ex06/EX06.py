#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:54:54 2020

@author: anirban
"""
import dash
import dash_core_components as dcc
import dash_html_components as html
import seaborn as sns
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
from dash.dependencies import Input, Output
import json


#def generate_scatter_plot():
    
data = pd.read_excel('Data_Cortex_Nuclear.xls')
data = data.interpolate(method = 'linear', limit_direction='forward')
    #print(data['class'].value_counts())
t_CS_s = data.loc[data['class'] == 't-CS-s']
c_CS_s = data.loc[data['class'] == 'c-CS-s']
new_data = [t_CS_s, c_CS_s]
new_data = pd.concat(new_data)
print(new_data)
#cCSs = data.loc[data['class'] == 'c-CS-s']    
new_data = new_data[['pPKCG_N', 'pP70S6_N', 'pS6_N', 'pGSK3B_N', 'ARC_N', 'class']]
#cCSs = cCSs[['pPKCG_N', 'pP70S6_N', 'pS6_N', 'pGSK3B_N', 'ARC_N', 'class']]
print(new_data)
index_vals = new_data['class'].astype('category').cat.codes

class_vals = new_data['class'].astype('category')

fig = go.Figure(data=go.Splom(
                  dimensions=[dict(label='pPKCG_N', values=new_data['pPKCG_N']),
                              dict(label='pP70S6_N', values=new_data['pP70S6_N']),
                              dict(label='pS6_N', values=new_data['pS6_N']),
                              dict(label='pGSK3B_N', values=new_data['pGSK3B_N']),
                              dict(label='ARC_N', values=new_data['ARC_N']),
                              #dict(label='BMI', values=tCSs['BMI']),
                              #dict(label='DiabPedigreeFun', values=tCSs['DiabetesPedigreeFunction']),
                              #dict(label='Age', values=tCSs['Age'])],
                              ],
                  marker=dict(color=index_vals,
                              size=5,
                              colorscale='Bluered',
                              line=dict(width=0.5,
                                        color='rgb(230,230,230)')),
                  hovertext = new_data['class'],
                  hoverinfo = 'all',
                  #text=textd,
                  #diagonal=dict(visible=True)
                  ))

#fig = px.scatter_matrix(new_data)
                  
fig.update_layout(
    title='Parallel Coordinates Plot',
    width=1000,
    height=1000,
)

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

styles = {
    'pre': {
        'border': 'thin lightgrey solid',
        'overflowX': 'scroll'
    }
}
app.layout = html.Div(children=[
    html.H1(children='Scatterplot Matrix'),

    html.Div(children=''' '''),
    #plot = generate_scatter_plot()
    dcc.Graph(id='plot', figure=fig),
    '''html.Div(className='row', children=[
        html.Div([
            dcc.Markdown(),
            html.Pre(id='hover-data', style=styles['pre'])
        ], className='three columns'),
            html.Div([
            dcc.Markdown(),
            html.Pre(id='click-data', style=styles['pre']),
        ], className='three columns'),

        html.Div([
            dcc.Markdown(),
            html.Pre(id='selected-data', style=styles['pre']),
        ], className='three columns'),

        html.Div([
            dcc.Markdown(),
            html.Pre(id='relayout-data', style=styles['pre']),
        ], className='three columns')
            ])'''

])

'''          
@app.callback(
    Output('hover-data', 'children'),
    [Input('basic-interactions', 'hoverData')])
def display_hover_data(hoverData):
    return json.dumps(hoverData, indent=2)

@app.callback(
    Output('click-data', 'children'),
    [Input('basic-interactions', 'clickData')])
def display_click_data(clickData):
    return json.dumps(clickData, indent=2)


@app.callback(
    Output('selected-data', 'children'),
    [Input('basic-interactions', 'selectedData')])
def display_selected_data(selectedData):
    return json.dumps(selectedData, indent=2)


@app.callback(
    Output('relayout-data', 'children'),
    [Input('basic-interactions', 'relayoutData')])
def display_relayout_data(relayoutData):
    return json.dumps(relayoutData, indent=2)
'''

if __name__ == '__main__':
    app.run_server(debug=True)
    #generate_scatter_plot()