import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_step_2_hist(df, feature_name, target_name, y_range_max=None):
    
    # colorblind palette:
    palette = ["#999999", "#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7"]
    
    feature_values = np.sort(df[feature_name].unique())
    num_features = len(feature_values)
    
    fig = make_subplots(
        rows=num_features, cols=1,
        subplot_titles=[feature_name + '=' + str(f) for f in feature_values]
    )
    
    fig.update_layout(
        height=200 * num_features, 
        width=800,
        title_text=target_name + ' distribution by ' + feature_name
    )
    
    for idx, feature in enumerate(feature_values):
        hist_df = df[(df[feature_name] == feature)]
        fig.add_trace(
            go.Histogram(
                x=hist_df[target_name],
                name=str(feature),
                marker={'color': palette[0]},
                showlegend=False
            ),
            row=idx+1, col=1
        )
            
    fig.update_xaxes(
        range=[df[target_name].min()-1,df[target_name].max()+1])
    
    fig.update_yaxes(
        title='Count'
    )
    
    if y_range_max:
        fig.update_yaxes(
            range=[0, y_range_max]
        )
    
    fig.update_layout(
        legend_title=feature_name
    )

                
    return fig