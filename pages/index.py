"""Imports from 3rd party libraries."""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import plotly.express as px

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """Your Risk Report

            The Cylinder app provides you a traffic risk report based on you,
            and how you self identify.  Be safe, for yourself and for those
            around you.
            """
        ),
        dcc.Link(dbc.Button('Get My Report', color='primary'),
                 href='/predictions')
    ],
    md=4,
)

gapminder = px.data.gapminder()
fig = px.scatter(gapminder.query("year==2007"),
                 x="gdpPercap",
                 y="lifeExp",
                 size="pop",
                 color="continent",
                 hover_name="country",
                 log_x=True, size_max=60)

column2 = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, column2])
