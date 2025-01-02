import pandas as pd
import plotly.express as px
import dash_ag_grid as dag
import query


getRowStyle = {
    "styleConditions": [
        {
            "condition": "params.rowIndex % 2 === 0",
            "style": {"backgroundColor": "whitesmoke", "color": "black"},
        },
    ]
}


# -------------------------------------------- New Products Page functions ---------------------------------------------

# Function to update tables
def get_table_from_query(start, table, end, connection):
    df = pd.read_sql(start + table + end + ';', connection)
    data = df.to_dict("records")
    columns_def = [{"field": i} for i in df.columns]
    return columns_def, data


# Function only to get tables for new products
def get_new_products(end, connection):
    call = f"""SELECT regulatory_admin, registration_number, product_name, license_holder, manufacturer, date_of_issuance, expiry_date FROM npra {end}
                UNION
                SELECT regulatory_admin, registration_number, product_name, license_holder, null as manufacturer, date_of_issuance, null as expiry_date FROM hsa {end}
                union
                SELECT regulatory_admin, registration_number, product_name, importer, manufacturer, date_of_issuance, expiry_date FROM ph_fda {end} and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                union
                SELECT regulatory_admin, registration_number, product_name, license_holder, manufacturer, date_of_issuance, expiry_date FROM bpom {end};"""
    df = pd.read_sql(call, connection)
    data = df.to_dict("records")
    columns_def = [{"field": i} for i in df.columns]
    return columns_def, data, df


# Function to update graphs
def give_pie_chart(start, table, end, month_n_year, connection):
    columns, data = get_table_from_query(start, table, end, connection)
    df = pd.read_sql(start + table + end, connection)
    fig = px.pie(
        df,
        values='number_of_products_registered',
        names='license_holders',
        title='% of New Registered Products'
    )
    fig.update_layout(
        {'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'},
        showlegend=False
    )
    title = f'{table.upper()} Registered in {month_n_year}'
    return columns, data, title, fig


# -------------------------------------------------- All Products Page -------------------------------------------------


# update upper graph to become count table
def replace_chart_with_table(start, table, end, connection):
    df = pd.read_sql(start + table + end, connection)
    grid = dag.AgGrid(
        rowData=df.to_dict("records"),
        columnDefs=[{"field": i} for i in df.columns],
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
        defaultColDef={"filter": True,
                       "sortable": True,
                       "floatingFilter": True,
                       "resizable": True
                        },
        style={'height': '250px', 'width': '100%'},
        columnSize='sizeToFit',
        # columnSize='autoSize',
        className='ag-theme-balham'
        # exportDataAsCsv=True,
    )

    return grid


# update bar chart
def update_bar_chart(query, connection):
    df = pd.read_sql_query(query, connection)
    fig = px.bar(
        df,
        x="year",
        y="count",
        color="table_name",
        title="Products Registered by Year"
    )
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)'})
    return fig


# Function to get table only for all_products
def get_all_products(connection):
    call = f"""SELECT regulatory_admin, registration_number, product_name, license_holder, manufacturer, date_of_issuance, expiry_date FROM npra
                    UNION
                    SELECT regulatory_admin, registration_number, product_name, license_holder, null as manufacturer, date_of_issuance, null as expiry_date FROM hsa
                    union
                    SELECT regulatory_admin, registration_number, product_name, importer, manufacturer, date_of_issuance, expiry_date FROM ph_fda where classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                    union
                    SELECT regulatory_admin, registration_number, product_name, license_holder, manufacturer, date_of_issuance, expiry_date FROM bpom;"""
    df = pd.read_sql(call, connection)
    data = df.to_dict("records")
    columns_def = [{"field": i} for i in df.columns]
    return columns_def, data, df
