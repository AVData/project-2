"""Imports from 3rd party libraries."""


import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
# import dash.dependencies import Input, Output

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Insights
            """
        ),
        html.P(
            [
                html.Img(src='assets/pdp_lead.jpg', className='img-fluid')
            ]
        ),

        dcc.Markdown(
            """
            ####
            """

        ),

        html.P(
            [
                html.Img(src='assets/pdp_parking.jpg', className='img-fluid')
            ]
        )

    ],
)

column2 = dbc.Col(
    [
        html.P(
            [
                html.Img(src='assets/shap_summary.jpg', className='img-fluid')
            ]
        ),

        dcc.Markdown(
            """
            ####
            """
        ),

        html.P(
            [
                html.Img(src='assets/pdp_deposit.jpg', className='img-fluid')
            ]
        ),

        dcc.Markdown(
            """
            """
        ),

        html.P(
            [
                html.Img(src='assets/shap_prediction.jpg', className='img-fluid')
            ]
        ),

        dcc.Markdown(
            """
            ####
            """
        ),

        html.P(
            [
                html.Img(src='assets/pdp_cxl.jpg', className='img-fluid')
            ]
        ),


    ],
    style={'margin-top': '30px'}
)

layout = dbc.Row([column1, column2])
