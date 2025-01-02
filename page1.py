from dash import Input, Output, State, dcc, html, callback
import query
from functions import get_table_from_query, give_pie_chart, get_new_products
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import dash_ag_grid as dag
import psycopg2
import dash

# import sqlalchemy
# import flask_sqlalchemy

# ------------------------------------------------ Page Initialisation -------------------------------------------------

dash.register_page(__name__, path='/')


# ----------------------------------- Psycopg2 PostgreSQL driver Database Connection -----------------------------------

# Optional
'''conn = psycopg2.connect(
    dbname='trial3',
    user='postgres',
    password='020921100961',
    host='localhost',
    port='5432',
)'''


# IN-USE
query_conn = 'postgresql://trial_user:TCeWMoXo1PoduKMsP5fb1P9Woo6Gx1Bb@dpg-ctqvvs52ng1s73eqfvng-a.singapore-postgres.render.com:5432/public_xp5i'


# --------------------------------------------- Definitions: Use for table ---------------------------------------------

# Column Definitions for count of new product table (small table)
# 2 columns: for regs admin, and the count
columnDefs = [
    {'headerName': 'Regulatory Administrations', 'field': 'regs_admins'},
    {'headerName': 'Number of New Registered Products', 'field': 'count'},
]


# Object definition for alternative row colors
# Makes the rows in the table to have alternating colours. white and grey for better legibility
getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.rowIndex % 2 === 0",
            "style": {"backgroundColor": "whitesmoke", "color": "black"},
        },
    ]
}


# --------------------------------------- Load SQL query scripts into dataframes ---------------------------------------

# Load query of "Count of new registered products in each national regulatory administration" for small table
# Displays the regs admin the amount of products registered based on the backlog dropdown
# and when the radio button is set to all products
# new_count_df = pd.read_sql(query.new_product_count, query_conn)


# Load query of "Every data of the new registered products in the month of October
# from all national regulatory administration" for the main table
# new_table_df = pd.read_sql(query.new_product_table, query_conn)


# Load "Count of new registered products in each national regulatory administration" for a pie chart
# new_graph_df = pd.read_sql(query.new_product_pie_chart, query_conn)


# --------------------------------------------------- Create graphs ----------------------------------------------------

# Pie chart definition
'''pie = px.pie(
    # new_graph_df,
    values='count',
    names='regs_admin',
    title='% of New Registered Products'
)
pie.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})'''


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
                        ], width=1
                    ),
                    # End of first component

                    # Start of 2nd component
                    dbc.Col(
                        [
                            # Button to access New Products page (current page)
                            dbc.Breadcrumb(
                                items=[{'label': 'New Products', 'active': True}],
                                itemClassName='center mitr-bigger'
                            ),
                        ], align='end',
                        width=2
                    ),
                    # End of 2nd component

                    # Start of 3rd component
                    dbc.Col(
                        [
                            # Button to access All Products page (clickable)
                            dbc.Breadcrumb(
                                items=[{'label': 'All Products', 'href': '/page2', 'external_link': True}],
                                itemClassName='center mitr-bigger'
                            ),
                        ], align='end',
                        width=2
                    ),
                    # End of 3rd component

                ], className='fixed-top border shadow-sm dp_gradient p-1'
            ),
            # End of Dashboard Header


            # Start of Title Header
            dbc.Row(
                [

                    # Start title
                    dbc.Col(
                        [
                            'The Latest Registered Products'
                        ], className='m2',
                        sm=5
                    ),
                    # End title

                    # Start dropdown component to pick backlog
                    dbc.Col(
                        [
                            dcc.Dropdown(
                                [
                                    'November 2024',
                                    'October 2024',
                                    'September 2024',
                                    'August 2024',
                                    'July 2024',
                                    'June 2024'
                                ], value='October 2024',
                                id='month-dropdown',
                                className='rounded-3 shadow mitr-smaller',
                                style={'width': '400px'},
                            ),
                        ], sm=4
                    )
                    # End of dropdown to pick backlog

                ], className='p-3 rounded-top h2 border mitr-regular bg-white text-center',
                align='center',
                justify='evenly'
            ),
            # End of page title header


            # Start of main data visualisation
            dbc.Row(
                [
                    # Start of left wing - for small table and graphs
                    dbc.Col([
                        dbc.Stack([

                            # Start of small table
                            html.Div([

                                # Title for small table
                                html.Div(
                                    [
                                        # 'New Products Registered in October 2024'
                                    ], className='text-center p-1',
                                    id='count-table-title'
                                ),

                                # Actual small table
                                dag.AgGrid(
                                    # rowData=new_count_df.to_dict("records"),
                                    # columnDefs=[{"field": i} for i in new_count_df.columns],
                                    columnDefs=columnDefs,
                                    getRowStyle=getRowStyle,
                                    id='count-table',
                                    dashGridOptions={
                                        'rowSelection': 'single',
                                        'pagination': False,
                                        'animateRows': False,
                                        # "domLayout": "autoHeight",
                                        "suppressColumnMoveAnimation": True,
                                        "enableCellTextSelection": True
                                    },
                                    # columnSize='responsiveSizeToFit',
                                    defaultColDef={
                                        "filter": False,
                                        "sortable": True,
                                        "floatingFilter": False,
                                        "resizable": True
                                    },
                                    style={'height': '250px', 'width': '100%'},
                                    columnSize='sizeToFit',
                                    # columnSize='autoSize',
                                    className='ag-theme-balham'
                                    # exportDataAsCsv=True,
                                )
                                # End actual small table

                            ], className='border bg-white rounded-3 shadow-sm'),
                            # End of small table

                            # Start of graph
                            html.Div(
                                [
                                    dcc.Graph(
                                        # figure=pie,
                                        style={'height': '275px'},
                                        id='pie-chart'
                                    )
                                ], className='border bg-white rounded-3 shadow-sm'
                            )
                            # End of graph

                        ], gap=2)
                    ], sm=3, className='ps-3'),
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
                                                                id="new-radios",
                                                                className="btn-group",
                                                                inputClassName="btn-check",
                                                                labelClassName="btn btn-outline-primary",
                                                                labelCheckedClassName="active",
                                                                options=[
                                                                    {"label": "All New Products",
                                                                     "value": 'all_product'},
                                                                    {"label": "Malaysia NPRA", "value": 'npra'},
                                                                    {"label": "Singapore HSA", "value": 'hsa'},
                                                                    {"label": "Indonesia BPOM", "value": 'bpom'},
                                                                    {"label": "Philippines FDA", "value": 'ph_fda'}
                                                                ],
                                                                value='all_product',
                                                            ),
                                                        ], className="radio-group ms-2 my-1",
                                                    ),
                                                ], sm=9, width={'order': 'first'}
                                            ),
                                            # End of radio button to pick regs admin

                                            # Start of download button
                                            dbc.Col(
                                                [
                                                    dcc.Download(id='download-new'),
                                                    dbc.Button(
                                                        ["Download as .csv"],
                                                        color="info",
                                                        className="mx-1 my-1",
                                                        id='btn-1',
                                                    ),
                                                ], sm=3,
                                                className='d-flex justify-content-end text-center',
                                                width={'order': 'last'}
                                            ),
                                            # End of download button
                                        ]
                                    ),
                                    # End of upper section

                                    # Start of table and lower section
                                    html.Div(
                                        [
                                            dag.AgGrid(
                                                id='new_grid',
                                                # rowData=new_table_df.to_dict("records"),
                                                # columnDefs=[{"field": i} for i in new_table_df.columns],
                                                getRowStyle=getRowStyle,
                                                dashGridOptions={
                                                    'rowSelection': 'single',
                                                    'pagination': False,
                                                    'animateRows': False,
                                                    "enableCellTextSelection": True
                                                },
                                                # columnSize='responsiveSizeToFit',
                                                defaultColDef={"filter": True,
                                                               "sortable": True,
                                                               "floatingFilter": True,
                                                               },
                                                style={'height': '500px'},
                                                className='ag-theme-balham'
                                                # exportDataAsCsv=True,
                                            )
                                        ], className='mx-2'
                                    ),
                                    # End  of table nad lower section

                                ], className='me-1 border rounded-3 bg-white'
                            )
                            # End stack

                        ], sm=9
                    ),
                    # End of main table

                ]
            ),
            # End of main data visualisation

        ], className="dash_back border rounded-3 m-2 shadow"
    ),
    # End of app container

], className='')
# End of app layout


# --------------------------------------------------- App Callbacks ----------------------------------------------------

# The start of a query - used with other call variables to complete a query sentence
call_start = "select * from "


# callback for dropdown and table
# Updates the main table based on the month backlog selected from dropdown and regs admin selected from radio buttons
@callback(
    Output("new_grid", "columnDefs"),
    Output("new_grid", "rowData"),
    Input("new-radios", "value"),
    Input("month-dropdown", "value"),
)
def display_monthly(table, month_n_year):
    if month_n_year == 'November 2024':

        # the end of a call - used as the final piece to complete a query sentence
        call_end = " where date_of_issuance >= '2024-11-01' and date_of_issuance <= '2024-11-30'"

        if table == 'all_product':
            # Assign three variable to receive values from get_new_products()
            columns, data, df = get_new_products(call_end, query_conn)
            # Only returns the first 2 variables
            return columns, data

        elif table == 'npra':
            # Directly returns columns and row data from get_table_from_query()
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'hsa':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'bpom':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'ph_fda':
            return get_table_from_query(call_start, table, call_end, query_conn)

    elif month_n_year == 'October 2024':
        call_end = " where date_of_issuance >= '2024-10-01' and date_of_issuance <= '2024-10-31'"

        if table == 'all_product':
            columns, data, df = get_new_products(call_end, query_conn)
            return columns, data

        elif table == 'npra':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'hsa':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'bpom':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'ph_fda':
            return get_table_from_query(call_start, table, call_end, query_conn)

    elif month_n_year == 'September 2024':
        call_end = " where date_of_issuance >= '2024-09-01' and date_of_issuance <= '2024-09-30'"

        if table == 'all_product':
            columns, data, df = get_new_products(call_end, query_conn)
            return columns, data

        elif table == 'npra':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'hsa':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'bpom':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'ph_fda':
            return get_table_from_query(call_start, table, call_end, query_conn)

    elif month_n_year == 'August 2024':
        call_end = " where date_of_issuance >= '2024-08-01' and date_of_issuance <= '2024-08-31'"

        if table == 'all_product':
            columns, data, df = get_new_products(call_end, query_conn)
            return columns, data

        elif table == 'npra':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'hsa':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'bpom':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'ph_fda':
            return get_table_from_query(call_start, table, call_end, query_conn)

    elif month_n_year == 'July 2024':
        call_end = " where date_of_issuance >= '2024-07-01' and date_of_issuance <= '2024-07-31'"

        if table == 'all_product':
            columns, data, df = get_new_products(call_end, query_conn)
            return columns, data

        elif table == 'npra':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'hsa':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'bpom':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'ph_fda':
            return get_table_from_query(call_start, table, call_end, query_conn)

    elif month_n_year == 'June 2024':
        call_end = " where date_of_issuance >= '2024-06-01' and date_of_issuance <= '2024-06-30'"

        if table == 'all_product':
            columns, data, df =  get_new_products(call_end, query_conn)
            return columns, data

        elif table == 'npra':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'hsa':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'bpom':
            return get_table_from_query(call_start, table, call_end, query_conn)

        elif table == 'ph_fda':
            return get_table_from_query(call_start, table, call_end, query_conn)


# callback for download button
# Will download the current table loaded into a CSV file
@callback(
    Output('download-new', 'data'),
    Input('btn-1', 'n_clicks'),
    State("month-dropdown", "value"),
    State("new-radios", "value"),
    prevent_initial_call=True
)
def download_btn(click, month_n_year, table):
    if month_n_year == 'November 2024':
        call_condition = " where date_of_issuance >= '2024-11-01' and date_of_issuance <= '2024-11-30'"
        call_end = ';'

        if table == 'all_product':
            # Assign three variable to receive values from get_new_products()
            columns, data, df = get_new_products(call_condition, query_conn)
            # Only returns the final variable
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'npra':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'hsa':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'bpom':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'ph_fda':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

    elif month_n_year == 'October 2024':
        call_condition = " where date_of_issuance >= '2024-10-01' and date_of_issuance <= '2024-10-31'"
        call_end = ';'

        if table == 'all_product':
            columns, data, df = get_new_products(call_condition, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'npra':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'hsa':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'bpom':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'ph_fda':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

    elif month_n_year == 'September 2024':
        call_condition = " where date_of_issuance >= '2024-09-01' and date_of_issuance <= '2024-09-30'"
        call_end = ';'

        if table == 'all_product':
            columns, data, df = get_new_products(call_condition, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'npra':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'hsa':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'bpom':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'ph_fda':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

    elif month_n_year == 'August 2024':
        call_condition = " where date_of_issuance >= '2024-08-01' and date_of_issuance <= '2024-08-31'"
        call_end = ';'

        if table == 'all_product':
            columns, data, df = get_new_products(call_condition, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'npra':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'hsa':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'bpom':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'ph_fda':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

    elif month_n_year == 'July 2024':
        call_condition = " where date_of_issuance >= '2024-07-01' and date_of_issuance <= '2024-07-31'"
        call_end = ';'

        if table == 'all_product':
            columns, data, df = get_new_products(call_condition, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'npra':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'hsa':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'bpom':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'ph_fda':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

    elif month_n_year == 'June 2024':
        call_condition = " where date_of_issuance >= '2024-06-01' and date_of_issuance <= '2024-06-30'"
        call_end = ';'

        if table == 'all_product':
            columns, data, df = get_new_products(call_condition, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'npra':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'hsa':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'bpom':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')

        elif table == 'ph_fda':
            df = pd.read_sql(call_start + table + call_condition + call_end, query_conn)
            return dcc.send_data_frame(df.to_csv, f'{table}_{month_n_year}.csv')


# update new count table (small table) and the graph in the left wing
# Changes when backlog is picked from dropdown, and regs admin is picked from radio buttons
@callback(
    Output("count-table", "columnDefs"),
    Output('count-table', 'rowData'),
    Output('count-table-title', 'children'),
    Output('pie-chart', 'figure'),
    Input("new-radios", "value"),
    Input("month-dropdown", "value"),
    # prevent_initial_call=True
)
def update_count_table(table, month_n_year):
    # The start of a query call - used with other calls to complete a query sentence
    call_head = "select distinct(license_holder) as License_Holders, count(*) as Number_of_Products_Registered from "
    call_end = 'group by license_holder;'
    ph_head = "select distinct(importer) as License_Holders, count(*) as Number_of_Products_Registered from "
    ph_end = 'group by importer;'

    if month_n_year == 'November 2024':
        # The end of a query call - the final piece to complete a query sentence
        call_tail = " where date_of_issuance >= '2024-11-01' and date_of_issuance <= '2024-11-30' "

        if table == 'npra':
            # Directly returns columns, row data, small table title, and pie chart
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'hsa':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'bpom':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'ph_fda':
            return give_pie_chart(ph_head, table, call_tail + ph_end, month_n_year, query_conn)

        else:
            # Without using functions because the query is long
            call_tail = " where date_of_issuance >= '2024-11-01' and date_of_issuance <= '2024-11-30'"
            # calls a major fraction of the query from query.get_count_for_callback()
            df = pd.read_sql(query.get_count_for_callback(call_tail), query_conn)
            # Graph is updated using the original dataframe from the original query definition
            fig = px.pie(df, values='count', names='regs_admins', title='% of New Registered Products')
            fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
            title = f'New Products Registered in {month_n_year}'
            return columnDefs, df.to_dict("records"), title, fig

    elif month_n_year == 'October 2024':
        call_tail = " where date_of_issuance >= '2024-10-01' and date_of_issuance <= '2024-10-31' "

        if table == 'npra':
            # Directly returns columns, row data, small table title, and pie chart
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'hsa':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'bpom':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'ph_fda':
            return give_pie_chart(ph_head, table, call_tail + ph_end, month_n_year, query_conn)

        else:
            call_tail = " where date_of_issuance >= '2024-10-01' and date_of_issuance <= '2024-10-30'"
            df = pd.read_sql(query.get_count_for_callback(call_tail), query_conn)
            fig = px.pie(df, values='count', names='regs_admins', title='% of New Registered Products')
            fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
            title = f'New Products Registered in {month_n_year}'
            return columnDefs, df.to_dict("records"), title, fig

    elif month_n_year == 'September 2024':
        call_tail = " where date_of_issuance >= '2024-09-01' and date_of_issuance <= '2024-09-30' "

        if table == 'npra':
            # Directly returns columns, row data, small table title, and pie chart
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'hsa':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'bpom':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'ph_fda':
            return give_pie_chart(ph_head, table, call_tail + ph_end, month_n_year, query_conn)

        else:
            call_tail = " where date_of_issuance >= '2024-09-01' and date_of_issuance <= '2024-09-30'"
            df = pd.read_sql(query.get_count_for_callback(call_tail), query_conn)
            fig = px.pie(df, values='count', names='regs_admins', title='% of New Registered Products')
            fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
            title = f'New Products Registered in {month_n_year}'
            return columnDefs, df.to_dict("records"), title, fig

    elif month_n_year == 'August 2024':
        call_tail = " where date_of_issuance >= '2024-08-01' and date_of_issuance <= '2024-08-31' "

        if table == 'npra':
            # Directly returns columns, row data, small table title, and pie chart
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'hsa':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'bpom':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'ph_fda':
            return give_pie_chart(ph_head, table, call_tail + ph_end, month_n_year, query_conn)

        else:
            call_tail = " where date_of_issuance >= '2024-08-01' and date_of_issuance <= '2024-08-30'"
            df = pd.read_sql(query.get_count_for_callback(call_tail), query_conn)
            fig = px.pie(df, values='count', names='regs_admins', title='% of New Registered Products')
            fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
            title = f'New Products Registered in {month_n_year}'
            return columnDefs, df.to_dict("records"), title, fig

    elif month_n_year == 'July 2024':
        call_tail = " where date_of_issuance >= '2024-07-01' and date_of_issuance <= '2024-07-31' "

        if table == 'npra':
            # Directly returns columns, row data, small table title, and pie chart
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'hsa':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'bpom':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'ph_fda':
            return give_pie_chart(ph_head, table, call_tail + ph_end, month_n_year, query_conn)

        else:
            call_tail = " where date_of_issuance >= '2024-07-01' and date_of_issuance <= '2024-07-30'"
            df = pd.read_sql(query.get_count_for_callback(call_tail), query_conn)
            fig = px.pie(df, values='count', names='regs_admins', title='% of New Registered Products')
            fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
            title = f'New Products Registered in {month_n_year}'
            return columnDefs, df.to_dict("records"), title, fig

    elif month_n_year == 'June 2024':
        call_tail = " where date_of_issuance >= '2024-06-01' and date_of_issuance <= '2024-06-30' "

        if table == 'npra':
            # Directly returns columns, row data, small table title, and pie chart
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'hsa':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'bpom':
            return give_pie_chart(call_head, table, call_tail + call_end, month_n_year, query_conn)

        elif table == 'ph_fda':
            return give_pie_chart(ph_head, table, call_tail + ph_end, month_n_year, query_conn)

        else:
            call_tail = " where date_of_issuance >= '2024-06-01' and date_of_issuance <= '2024-06-30'"
            df = pd.read_sql(query.get_count_for_callback(call_tail), query_conn)
            fig = px.pie(df, values='count', names='regs_admins', title='% of New Registered Products')
            fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
            title = f'New Products Registered in {month_n_year}'
            return columnDefs, df.to_dict("records"), title, fig
