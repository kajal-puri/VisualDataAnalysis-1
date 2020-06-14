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
    't-SC-s': [[0, 'rgba(13, 118, 191, 0.1)'], [1, 'rgba(13, 118, 191, 1)']],
    'c-SC-s': [[0, 'rgba(239, 85, 59, 0.1)'], [1, 'rgba(239, 85, 59, 1)']]
})

# read data X
X_std = data.iloc[:, 0:len(data.columns)].values


def generate_dimensionality_reduction_graph(results, xaxis_label, yaxis_label):
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
    
def generate_pca():
        n_components = 10
        pca = sklearnPCA(n_components=n_components)
        pca_results = pca.fit_transform(X_std)

        return generate_dimensionality_reduction_graph(results=pca_results,
                                                   xaxis_label='PC1',
                                                   yaxis_label='PC2')
def generate_isomap():
    isomap = sklearnIsomap()
    isomap_results = isomap.fit_transform(X_std)

    return generate_dimensionality_reduction_graph(results=isomap_results,
                                                   xaxis_label='ISOMAP1',
                                                   yaxis_label='ISOMAP2')


def generate_tsne():
    tsne = sklearnTSNE(init='pca')
    tsne_results = tsne.fit_transform(X_std)

    return generate_dimensionality_reduction_graph(results=tsne_results,
                                                   xaxis_label='tSNE1',
                                                   yaxis_label='tSNE2')


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
             ])
    ])
technique_mapper = {
    'pca': generate_pca(),
    'isomap': generate_isomap(),
    'tsne': generate_tsne()
}
@app.callback(dash.dependencies.Output('dimension-reduction-graph', 'figure'),
              [dash.dependencies.Input('dr-technique', 'value')])

def render_selected_dimension_reduction_graph(dr_technique):
    logging.debug('Dimensionality Reduction Graph')
    logging.debug('Dropdown Value:', dr_technique)

    return technique_mapper.get(dr_technique, generate_isomap())


if __name__ == '__main__':
    app.run_server(debug=True)
    