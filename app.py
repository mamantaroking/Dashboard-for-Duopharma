from dash import Dash, Input, Output, State, dash_table, dcc, html
import dash_bootstrap_components as dbc
import query
import functions
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag
import psycopg2
import dash
import gunicorn
# import sqlalchemy
# import flask_sqlalchemy
import flask
import flask_caching


# Define external stylesheets
external_stylesheets = ["https://fonts.googleapis.com/css2?family=Mitr:wght@200;300;400;500;600;700&family=Passion+One&display=swap",
                        dbc.themes.LITERA]

# ------------------------------------------------- App Initialization -------------------------------------------------

app = Dash(__name__, use_pages=True, external_stylesheets=external_stylesheets)
server = app.server


# ----------------------------------------------------- App Layout -----------------------------------------------------

app.layout = html.Div([
    dash.page_container
])


if __name__ == '__main__':
    app.run(debug=True, port=8021)
