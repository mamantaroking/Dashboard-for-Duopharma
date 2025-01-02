from dash import html, dcc, Output, Input, callback, State
from functions import get_table_from_query, replace_chart_with_table, update_bar_chart, get_all_products
import query
import dash
import pandas as pd
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import plotly.express as px


# ------------------------------------------------ Page Initialisation -------------------------------------------------

dash.register_page(__name__)


# ----------------------------------- Psycopg2 PostgreSQL driver Database Connection -----------------------------------

# Define the connection to database
query_conn = 'postgresql+psycopg2://postgres:020921100961@localhost:5432/trial3'


# --------------------------------------------- Definitions: Use for table ---------------------------------------------

# object definition for alternative row colors
getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.rowIndex % 2 === 0",
            "style": {"backgroundColor": "whitesmoke", "color": "black"},
        },
    ]
}


# ----------------------------------------------------- App layout -----------------------------------------------------

# Start of app layout
layout = html.Div([
    # Empty component for padding
    html.Div(className='m-5 header_height'),

    # Start of app container
    html.Div(
        [

            # Start of Dashboard Header
            dbc.Row(
                [

                    # Start of first component
                    dbc.Col(
                        [
                            # For Company logo
                            html.A(
                                [
                                    html.Img(
                                        id='header-logo',
                                        src=r'assets/dp_logo.png',
                                        alt='duopharma_logo',
                                        height='67px',
                                        width='100px',
                                        className='center'
                                    ),
                                ], href='https://duopharmabiotech.com/about-duopharma-biotech/',
                                target="_blank",
                                className='center',
                                style={'width': '150px'}
                            ),
                            # End for company logo
                        ], sm=1
                    ),
                    # End of first component

                    # Start of 2nd component
                    dbc.Col(
                        [
                            dbc.Breadcrumb(
                                items=[{'label': 'New Products', 'href': '/', 'external_link': True}],
                                itemClassName='center mitr-bigger'
                            ),
                        ], align='end',
                        sm=2
                    ),
                    # End of 2nd component

                    # Start of 3rd component
                    dbc.Col(
                        [
                            dbc.Breadcrumb(
                                items=[{'label': 'All Products', 'active': True}],
                                itemClassName='center mitr-bigger'
                            ),
                        ], align='end',
                        sm=2
                    ),
                    # End of 3rd component

                ], className='fixed-top border shadow-sm dp_gradient p-1'
            ),
            # End of Dashboard Header


            # Start of Title Header
            html.Div(
                [
                    html.Div(
                        [
                            'All Registered Products'
                        ], className='p-3 rounded-top h2 border mitr-regular bg-white text-center'
                    ),

                ]
            ),
            # End of Title Header


            # Start of main data visualisation
            dbc.Row(
                [
                    # Start of left wing - for small table and graphs
                    dbc.Col(
                        [
                            dbc.Stack(
                                [

                                    # Upper graph
                                    html.Div(
                                        [],
                                        className='border bg-white rounded-3 shadow-sm',
                                        id='upper-graph-holder'
                                    ),

                                    # Lower graph
                                    html.Div(
                                        [
                                            dcc.Graph(
                                                # figure=bar,
                                                style={'height': '300px'},
                                                id='graph-2'
                                            )
                                        ], className='border bg-white rounded-3 shadow-sm'
                                    )
                                    # End lower graph

                                ], gap=2
                            )
                            # End stack
                        ],
                        sm=3,
                        className='ps-3'
                    ),
                    # End of left wing - for small table and graphs


                    # Start of main table
                    dbc.Col(
                        [
                            dbc.Stack(
                                [
                                    # Start of upper section
                                    dbc.Row(
                                        [
                                            # Start of radio button to pick regs admin
                                            dbc.Col(
                                                [
                                                    html.Div(
                                                        [
                                                            dbc.RadioItems(
                                                                id="radio-btn",
                                                                className="btn-group",
                                                                inputClassName="btn-check",
                                                                labelClassName="btn btn-outline-primary",
                                                                labelCheckedClassName="active",
                                                                options=[
                                                                    {"label": "All Products", "value": 'all_product'},
                                                                    {"label": "Malaysia NPRA", "value": 'npra'},
                                                                    {"label": "Singapore HSA", "value": 'hsa'},
                                                                    {"label": "Indonesia BPOM", "value": 'bpom'},
                                                                    {"label": "Philippines FDA", "value": 'ph_fda'}
                                                                ],
                                                                value='all_product',
                                                            ),
                                                            # End radio button component
                                                        ], className="radio-group ms-2 my-1",
                                                    ),
                                                    # End div
                                                ], sm=9,
                                                width={'order': 'first'}
                                            ),
                                            # End of radio button to pick regs admin

                                            # Start download button
                                            dbc.Col(
                                                [
                                                    dcc.Download(id='download-old'),
                                                    dbc.Button(
                                                        ["Download as .csv"],
                                                        color="info",
                                                        # className="d-flex justify-content-end",
                                                        className='mx-1 my-1',
                                                        id='btn-2',
                                                    ),
                                                ], sm=3,
                                                className='d-flex justify-content-end text-center',
                                                width={'order': 'last'}
                                            ),
                                            # Start download button

                                        ]
                                    ),
                                    # End of upper section


                                    # Start of lower section and table
                                    html.Div(
                                        [
                                            dag.AgGrid(
                                                id='all_grid',
                                                getRowStyle=getRowStyle,
                                                dashGridOptions={
                                                    'rowSelection': 'single',
                                                    'pagination': False,
                                                    'animateRows': False,
                                                    "enableCellTextSelection": True
                                                },
                                                # columnSize='responsiveSizeToFit',
                                                defaultColDef={
                                                    "filter": True,
                                                    "sortable": True,
                                                    "floatingFilter": True,
                                                },
                                                style={'height': '500px'},
                                                className='ag-theme-balham'
                                                # exportDataAsCsv=True,
                                            )
                                        ], className='mx-2'
                                    ),
                                    # End of lower section and table

                                ], className='me-1 border bg-white rounded-3'
                            )
                            # End of stack
                        ], sm=9,
                        className=''
                    ),
                    # End of main table

                ]
            ),
        ], className="dash_back border rounded-3 m-2 shadow"
    ),
    # End of app container

])
# End of app layout


# --------------------------------------------------- App Callbacks ----------------------------------------------------

# Define the beginning pieces of call queries - combined with other call sections to complete a query semtemce
call_start = "select * from "


# call back for radio button
# Updates the main table based on the radio button that picks regs admin
@callback(
    Output("all_grid", "columnDefs",),
    Output("all_grid", "rowData"),
    [Input("radio-btn", "value")]
)
def display_value(value):
    call_end = ''
    if value == 'all_product':
        # Assign three variable to receive values from get_all_products()
        columns, data, df = get_all_products(query_conn)
        # Only returns the first 2 variables
        return columns, data

    elif value == 'npra':
        # Directly returns columns and row data from get_all_from_query()
        return get_table_from_query(call_start, value, call_end, query_conn)

    elif value == 'hsa':
        return get_table_from_query(call_start, value, call_end, query_conn)

    elif value == 'bpom':
        return get_table_from_query(call_start, value, call_end, query_conn)

    elif value == 'ph_fda':
        return get_table_from_query(call_start, value, call_end, query_conn)


# callback for download button
# Will download the current table loaded into a CSV file
@callback(
    Output('download-old', 'data'),
    Input('btn-2', 'n_clicks'),
    State('radio-btn', 'value'),
    prevent_initial_call=True
)
def download_btn(click, value):
    if value == 'all_product':
        # Assign three variable to receive values from get_new_products()
        columns, data, df = get_all_products(query_conn)
        # Only returns the final variable
        return dcc.send_data_frame(df.to_csv, f'all_{value}.csv')

    elif value == 'npra':
        df = pd.read_sql(call_start + value, query_conn)
        return dcc.send_data_frame(df.to_csv, f'all_{value}.csv')

    elif value == 'hsa':
        df = pd.read_sql(call_start + value, query_conn)
        return dcc.send_data_frame(df.to_csv, f'all_{value}.csv')

    elif value == 'bpom':
        df = pd.read_sql(call_start + value, query_conn)
        return dcc.send_data_frame(df.to_csv, f'all_{value}.csv')

    elif value == 'ph_fda':
        call_tail = "ph_fda where classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%';"
        df = pd.read_sql(call_start + call_tail, query_conn)
        return dcc.send_data_frame(df.to_csv, f'all_{value}.csv')


# update graphs in the left wing
# Changes when regs admin is picked from radio buttons
@callback(
    Output('upper-graph-holder', 'children'),
    Output('graph-2', 'figure'),
    Input('radio-btn', 'value')
)
def update_upper_graph(value):
    # Define the beginning and end pieces of call queries -
    # combined with other call sections to complete a query semtemce
    call_head = "select distinct(license_holder) as License_Holders, count(*) as Number_of_Products_Registered from "
    call_tail = " group by license_holder order by license_holder asc;"

    # create dataframe from query call for treemap
    dfgraph = pd.read_sql_query(query.all_product_tree_map, query_conn)

    if value == 'npra':
        # returns small table from replace_chart_with_table()
        fig1 = replace_chart_with_table(call_head, value, call_tail, query_conn)
        # returns bar chart fig for figure from replace_bar_chart()
        fig2 = update_bar_chart(query.npra_bar_chart, query_conn)
        return fig1, fig2

    elif value == 'hsa':
        fig1 = replace_chart_with_table(call_head, value, call_tail, query_conn)
        fig2 = update_bar_chart(query.hsa_bar_chart, query_conn)
        return fig1, fig2

    elif value == 'bpom':
        fig1 = replace_chart_with_table(call_head, value, call_tail, query_conn)
        fig2 = update_bar_chart(query.bpom_bar_chart, query_conn)
        return fig1, fig2

    elif value == 'ph_fda':
        call_head = "select distinct(importer) as License_Holders, count(*) as Number_of_Products_Registered from "
        call_tail = " group by importer order by importer asc;"
        fig1 = replace_chart_with_table(call_head, value, call_tail, query_conn)
        fig2 = update_bar_chart(query.ph_fda_bar_chart, query_conn)
        return fig1, fig2

    else:
        # Replace table with the original tree map - Start tree map
        fig = px.treemap(
            dfgraph,
            path=['region', 'regs_admin'],
            values='count',
            color='count',
            color_continuous_scale='RdBu',
            title='Total Registered Products'
        )
        fig.update_traces(textinfo="label+value")
        fig.update_layout(
            {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'},
            margin=dict(t=50, l=25, r=25, b=25)
        )
        # End tree map

        # create dcc.graph to insert tree map fig in the div children
        graph1 = dcc.Graph(figure=fig, style={'height': '237px'}, id='graph-1')

        # returns bar chart fig for figure from replace_bar_chart()
        fig2 = update_bar_chart(query.all_product_bar_chart, query_conn)
        return graph1, fig2
