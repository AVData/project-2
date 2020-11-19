"""Imports from 3rd party libraries."""

import dash_bootstrap_components as dbc
import dash_core_components as dcc

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Predictions
            Your instructions: How to use your app to get new predictions.
            """
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1, column2])
