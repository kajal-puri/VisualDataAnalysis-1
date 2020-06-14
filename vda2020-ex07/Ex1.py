#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 22:23:32 2020

@author: shilpa
"""


import logging

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from dash.dependencies import Input, Output

from sklearn.manifold import TSNE as sklearnTSNE
from sklearn.manifold import Isomap as sklearnIsomap
from sklearn.decomposition import PCA as sklearnPCA
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

df = pd.read_excel('Data_Cortex_Nuclear.xls')
data = pd.concat([df[df['class'] == 'c-SC-s'], df[df['class'] == 't-SC-s']])

y = data.iloc[:, len(data.columns) - 1].values
mouse_ids = data.iloc[:, 0].values
data = data.drop(
    columns=['MouseID', 'Genotype', 'Treatment', 'Behavior', 'class'])
data.fillna(data.mean(), inplace=True)

class_colours = dict({
    't-SC-s': [[0, 'rgba(19, 130, 191, 0.1)'], [1, 'rgba(19, 130, 191, 1)']],
    'c-SC-s': [[0, 'rgba(239, 85, 59, 0.1)'], [1, 'rgba(239, 85, 59, 1)']]
})

# read data X
X = data.iloc[:, 0:len(data.columns)].values
X_std = data.iloc[:, 0:len(data.columns)].values


def dimensionality_reduction_graph(results, xaxis_label, yaxis_label):
    fig_data = []
    for cls in ('c-SC-s', 't-SC-s'):

        trace = dict(type='scatter',
                     x=results[y == cls, 0],
                     y=results[y == cls, 1],
                     mode='markers',
                     name=cls,
                     text=mouse_ids[y == cls],
                     marker=dict(color=class_colours[cls][1][1],
                                 size=12,
                                 line=dict(color='rgba(217, 217, 217, 0.1)',
                                           width=0.5),
                                 opacity=0.7))
        fig_data.append(trace)

        fig_layout = dict(xaxis=dict(title=xaxis_label, showline=False),
                      yaxis=dict(title=yaxis_label, showline=False),
                      clickmode='event+select')

    return dict(data=fig_data, layout=fig_layout)
    
def pca_graph():
        n_components = 10
        pca = sklearnPCA(n_components=n_components)
        pca_results = pca.fit_transform(X_std)

        return dimensionality_reduction_graph(results=pca_results,
                                                   xaxis_label='PC1',
                                                   yaxis_label='PC2')
def isomap_graph():
    isomap = sklearnIsomap()
    isomap_results = isomap.fit_transform(X_std)

    return dimensionality_reduction_graph(results=isomap_results,
                                                   xaxis_label='ISOMAP1',
                                                   yaxis_label='ISOMAP2')


def tsne_graph():
    tsne = sklearnTSNE(init='pca')
    tsne_results = tsne.fit_transform(X_std)

    return dimensionality_reduction_graph(results=tsne_results,
                                                   xaxis_label='tSNE1',
                                                   yaxis_label='tSNE2')
def generate_two_feature_graph(x_feature, y_feature, highlighted_points):

    selection_mask = np.full(y.shape[0], 1)

    if highlighted_points:
        logging.debug('Highlighting Points!')
        selection_ids = [
            point['text'] for point in highlighted_points['points']
        ]
        selection_mask = np.isin(mouse_ids,
                                 np.asarray(selection_ids)).astype(int)

    fig_data = []

    for cls in ('c-SC-s', 't-SC-s'):

        x_index = data.columns.get_loc(x_feature)
        y_index = data.columns.get_loc(y_feature)
        x_values = X[y == cls, x_index]
        y_values = X[y == cls, y_index]
        coloration_filtered = selection_mask[y == cls]
        ids = mouse_ids[y == cls]

        trace = dict(type='scatter',
                     x=x_values,
                     y=y_values,
                     mode='markers',
                     name=cls,
                     text=ids,
                     marker=dict(color=coloration_filtered,
                                 colorscale=class_colours[cls],
                                 size=12,
                                 line=dict(color='rgba(217, 217, 217, 0.14)',
                                           width=0.5)))
        fig_data.append(trace)

    layout = dict(xaxis=dict(title=x_feature, showline=False),
                  yaxis=dict(title=y_feature, showline=False),
                  clickmode='event+select')

    fig = dict(data=fig_data, layout=layout)

    return {"data": fig_data, "layout": layout}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.Div(style={
        'width': '50%',
        'display': 'inline-block'
    },
             children=[
                 html.H4(children='Dimensionality Reduction Graph'),
                 dcc.Dropdown(
                     id='dr-technique',
                     options=[{
                         'label': i,
                         'value': i
                     } for i in ['pca', 'isomap', 'tsne']],
                     multi=False,
                     placeholder='Select Dimensionality Reduction Technique'),
                 dcc.Graph(id='dimension-reduction-graph',
                           style={'height': 500})
             ]),
    html.Div(style={
        'width': '49%',
        'display': 'inline-block'
    },
             children=[
                 html.H4(children='2-Feature Graph'),
                 dcc.Dropdown(id='two-feature-graph-x',
                              options=[{
                                  'label': i,
                                  'value': i
                              } for i in data.columns],
                              multi=False,
                              placeholder='Select X Feature'),
                 dcc.Dropdown(id='two-feature-graph-y',
                              options=[{
                                  'label': i,
                                  'value': i
                              } for i in data.columns],
                              multi=False,
                              placeholder='Select Y Feature'),
                 dcc.Graph(id='two-feature-graph', style={'height': 500})
             ])
    ])
technique_mapper = {
    'pca': pca_graph(),
    'isomap': isomap_graph(),
    'tsne': tsne_graph()
}
@app.callback(dash.dependencies.Output('dimension-reduction-graph', 'figure'),
              [dash.dependencies.Input('dr-technique', 'value')])

def selected_dimension_reduction_graph(dr_technique):
    logging.debug('Dimensionality Reduction Graph')
    logging.debug('Dropdown Value:', dr_technique)

    return technique_mapper.get(dr_technique, isomap_graph())

@app.callback(dash.dependencies.Output('two-feature-graph', 'figure'), [
    dash.dependencies.Input('two-feature-graph-x', 'value'),
    dash.dependencies.Input('two-feature-graph-y', 'value'),
    dash.dependencies.Input('dimension-reduction-graph', 'selectedData')
])
def two_feature_graph(x_feature, y_feature, highlighted_points):

    logging.debug('2-Feature Graph')
    logging.debug('X Feature:', x_feature)
    logging.debug('Y Feature:', y_feature)
    logging.debug('Selected Data:', highlighted_points)

    x_feature = x_feature or 'NUMB_N'
    y_feature = y_feature or 'RAPTOR_N'

    return generate_two_feature_graph(x_feature, y_feature, highlighted_points)

if __name__ == '__main__':
    app.run_server(debug=True)
    