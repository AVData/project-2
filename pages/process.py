"""Imports from 3rd party libraries."""

import dash_bootstrap_components as dbc
import dash_core_components as dcc

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Process
            """
        ),

    ],
)

layout = dbc.Row([column1])
