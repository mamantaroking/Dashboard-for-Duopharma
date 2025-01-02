
# --------------------------------------------------- Query Scripts ----------------------------------------------------


# Query used to get all product data for a tree map
# The attributes of use are region, regs_admin, and count
all_product_tree_map = '''SELECT 'South East Asia' as region, 'Malaysia NPRA' AS regs_admin, COUNT(*) as count FROM npra
                        union all
                        SELECT 'South East Asia' as region, 'Indonesia BPOM' AS regs_admin, COUNT(*) as count FROM bpom
                        union all
                        SELECT 'South East Asia' as region, 'Singapore HSA' AS regs_admin, COUNT(*) as count FROM hsa
                        union all
                        SELECT 'South East Asia' as region, 'Philippines FDA' AS regs_admin, COUNT(*) as count FROM ph_fda where classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%';'''


# Query used to get all product data for a bar chart
# Every regs admin are queried along with their count and are segmented by year
# From 2017 to 2024 is 8 years, times with 4 regs admins, equals to 32 SELECT statements
all_product_bar_chart = '''select 'npra' as table_name, '2024' as year, count(*) from npra where date_of_issuance >= '2024-01-01' and date_of_issuance <= '2025-01-01'
                            union all
                            select 'npra' as table_name, '2023' as year, count(*) from npra where date_of_issuance >= '2023-01-01' and date_of_issuance <= '2024-01-01'
                            union all
                            select 'npra' as table_name, '2022' as year, count(*) from npra where date_of_issuance >= '2022-01-01' and date_of_issuance <= '2023-01-01'
                            union all
                            select 'npra' as table_name, '2021' as year, count(*) from npra where date_of_issuance >= '2021-01-01' and date_of_issuance <= '2022-01-01'
                            union all
                            select 'npra' as table_name, '2020' as year, count(*) from npra where date_of_issuance >= '2020-01-01' and date_of_issuance <= '2021-01-01'
                            union all
                            select 'npra' as table_name, '2019' as year, count(*) from npra where date_of_issuance >= '2019-01-01' and date_of_issuance <= '2020-01-01'
                            union all
                            select 'npra' as table_name, '2018' as year, count(*) from npra where date_of_issuance >= '2018-01-01' and date_of_issuance <= '2019-01-01'
                            union all
                            select 'npra' as table_name, '2017' as year, count(*) from npra where date_of_issuance >= '2017-01-01' and date_of_issuance <= '2018-01-01'
                            union all
                            select 'hsa' as table_name, '2024' as year, count(*) from hsa where date_of_issuance >= '2024-01-01' and date_of_issuance <= '2025-01-01'
                            union all
                            select 'hsa' as table_name, '2023' as year, count(*) from hsa where date_of_issuance >= '2023-01-01' and date_of_issuance <= '2024-01-01'
                            union all
                            select 'hsa' as table_name, '2022' as year, count(*) from hsa where date_of_issuance >= '2022-01-01' and date_of_issuance <= '2023-01-01'
                            union all
                            select 'hsa' as table_name, '2021' as year, count(*) from hsa where date_of_issuance >= '2021-01-01' and date_of_issuance <= '2022-01-01'
                            union all
                            select 'hsa' as table_name, '2020' as year, count(*) from hsa where date_of_issuance >= '2020-01-01' and date_of_issuance <= '2021-01-01'
                            union all
                            select 'hsa' as table_name, '2019' as year, count(*) from hsa where date_of_issuance >= '2019-01-01' and date_of_issuance <= '2020-01-01'
                            union all
                            select 'hsa' as table_name, '2018' as year, count(*) from hsa where date_of_issuance >= '2018-01-01' and date_of_issuance <= '2019-01-01'
                            union all
                            select 'hsa' as table_name, '2017' as year, count(*) from hsa where date_of_issuance >= '2017-01-01' and date_of_issuance <= '2018-01-01'
                            union all
                            select 'bpom' as table_name, '2024' as year, count(*) from bpom where date_of_issuance >= '2024-01-01' and date_of_issuance <= now()
                            union all
                            select 'bpom' as table_name, '2023' as year, count(*) from bpom where date_of_issuance >= '2023-01-01' and date_of_issuance <= '2025-01-01'
                            union all
                            select 'bpom' as table_name, '2022' as year, count(*) from bpom where date_of_issuance >= '2022-01-01' and date_of_issuance <= '2023-01-01'
                            union all
                            select 'bpom' as table_name, '2021' as year, count(*) from bpom where date_of_issuance >= '2021-01-01' and date_of_issuance <= '2022-01-01'
                            union all
                            select 'bpom' as table_name, '2020' as year, count(*) from bpom where date_of_issuance >= '2020-01-01' and date_of_issuance <= '2021-01-01'
                            union all
                            select 'bpom' as table_name, '2019' as year, count(*) from bpom where date_of_issuance >= '2019-01-01' and date_of_issuance <= '2020-01-01'
                            union all
                            select 'bpom' as table_name, '2018' as year, count(*) from bpom where date_of_issuance >= '2018-01-01' and date_of_issuance <= '2019-01-01'
                            union all
                            select 'bpom' as table_name, '2017' as year, count(*) from bpom where date_of_issuance >= '2017-01-01' and date_of_issuance <= '2018-01-01'
                            union all
                            select 'ph_fda' as table_name, '2024' as year, count(*) from ph_fda where date_of_issuance >= '2024-01-01' and date_of_issuance <= '2025-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2023' as year, count(*) from ph_fda where date_of_issuance >= '2023-01-01' and date_of_issuance <= '2024-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2022' as year, count(*) from ph_fda where date_of_issuance >= '2022-01-01' and date_of_issuance <= '2023-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2021' as year, count(*) from ph_fda where date_of_issuance >= '2021-01-01' and date_of_issuance <= '2022-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2020' as year, count(*) from ph_fda where date_of_issuance >= '2020-01-01' and date_of_issuance <= '2021-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2019' as year, count(*) from ph_fda where date_of_issuance >= '2019-01-01' and date_of_issuance <= '2020-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2018' as year, count(*) from ph_fda where date_of_issuance >= '2018-01-01' and date_of_issuance <= '2019-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2017' as year, count(*) from ph_fda where date_of_issuance >= '2017-01-01' and date_of_issuance <= '2018-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%' order by year asc;'''


# Query used to get only get data for a bar chart
# Only fetches data from npra table and is queried along with the count and is segmented by year
npra_bar_chart = """select 'npra' as table_name, '2024' as year, count(*) from npra where date_of_issuance >= '2024-01-01' and date_of_issuance <= '2025-01-01'
                            union all
                            select 'npra' as table_name, '2023' as year, count(*) from npra where date_of_issuance >= '2023-01-01' and date_of_issuance <= '2024-01-01'
                            union all
                            select 'npra' as table_name, '2022' as year, count(*) from npra where date_of_issuance >= '2022-01-01' and date_of_issuance <= '2023-01-01'
                            union all
                            select 'npra' as table_name, '2021' as year, count(*) from npra where date_of_issuance >= '2021-01-01' and date_of_issuance <= '2022-01-01'
                            union all
                            select 'npra' as table_name, '2020' as year, count(*) from npra where date_of_issuance >= '2020-01-01' and date_of_issuance <= '2021-01-01'
                            union all
                            select 'npra' as table_name, '2019' as year, count(*) from npra where date_of_issuance >= '2019-01-01' and date_of_issuance <= '2020-01-01'
                            union all
                            select 'npra' as table_name, '2018' as year, count(*) from npra where date_of_issuance >= '2018-01-01' and date_of_issuance <= '2019-01-01'
                            union all
                            select 'npra' as table_name, '2017' as year, count(*) from npra where date_of_issuance >= '2017-01-01' and date_of_issuance <= '2018-01-01' order by year asc;"""


# Query used to get only get data for a bar chart
# Only fetches data from hsa table and is queried along with the count and is segmented by year
hsa_bar_chart = """select 'hsa' as table_name, '2024' as year, count(*) from hsa where date_of_issuance >= '2024-01-01' and date_of_issuance <= '2025-01-01'
                            union all
                            select 'hsa' as table_name, '2023' as year, count(*) from hsa where date_of_issuance >= '2023-01-01' and date_of_issuance <= '2024-01-01'
                            union all
                            select 'hsa' as table_name, '2022' as year, count(*) from hsa where date_of_issuance >= '2022-01-01' and date_of_issuance <= '2023-01-01'
                            union all
                            select 'hsa' as table_name, '2021' as year, count(*) from hsa where date_of_issuance >= '2021-01-01' and date_of_issuance <= '2022-01-01'
                            union all
                            select 'hsa' as table_name, '2020' as year, count(*) from hsa where date_of_issuance >= '2020-01-01' and date_of_issuance <= '2021-01-01'
                            union all
                            select 'hsa' as table_name, '2019' as year, count(*) from hsa where date_of_issuance >= '2019-01-01' and date_of_issuance <= '2020-01-01'
                            union all
                            select 'hsa' as table_name, '2018' as year, count(*) from hsa where date_of_issuance >= '2018-01-01' and date_of_issuance <= '2019-01-01'
                            union all
                            select 'hsa' as table_name, '2017' as year, count(*) from hsa where date_of_issuance >= '2017-01-01' and date_of_issuance <= '2018-01-01' order by year asc;"""


# Query used to get only get data for a bar chart
# Only fetches data from bpom table and is queried along with the count and is segmented by year
bpom_bar_chart = """select 'bpom' as table_name, '2024' as year, count(*) from bpom where date_of_issuance >= '2024-01-01' and date_of_issuance <= now()
                            union all
                            select 'bpom' as table_name, '2023' as year, count(*) from bpom where date_of_issuance >= '2023-01-01' and date_of_issuance <= '2025-01-01'
                            union all
                            select 'bpom' as table_name, '2022' as year, count(*) from bpom where date_of_issuance >= '2022-01-01' and date_of_issuance <= '2023-01-01'
                            union all
                            select 'bpom' as table_name, '2021' as year, count(*) from bpom where date_of_issuance >= '2021-01-01' and date_of_issuance <= '2022-01-01'
                            union all
                            select 'bpom' as table_name, '2020' as year, count(*) from bpom where date_of_issuance >= '2020-01-01' and date_of_issuance <= '2021-01-01'
                            union all
                            select 'bpom' as table_name, '2019' as year, count(*) from bpom where date_of_issuance >= '2019-01-01' and date_of_issuance <= '2020-01-01'
                            union all
                            select 'bpom' as table_name, '2018' as year, count(*) from bpom where date_of_issuance >= '2018-01-01' and date_of_issuance <= '2019-01-01'
                            union all
                            select 'bpom' as table_name, '2017' as year, count(*) from bpom where date_of_issuance >= '2017-01-01' and date_of_issuance <= '2018-01-01' order by year asc;"""


# Query used to get only get data for a bar chart
# Only fetches data from ph fda table and is queried along with the count and is segmented by year
ph_fda_bar_chart = """select 'ph_fda' as table_name, '2024' as year, count(*) from ph_fda where date_of_issuance >= '2024-01-01' and date_of_issuance <= '2025-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2023' as year, count(*) from ph_fda where date_of_issuance >= '2023-01-01' and date_of_issuance <= '2024-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2022' as year, count(*) from ph_fda where date_of_issuance >= '2022-01-01' and date_of_issuance <= '2023-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2021' as year, count(*) from ph_fda where date_of_issuance >= '2021-01-01' and date_of_issuance <= '2022-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2020' as year, count(*) from ph_fda where date_of_issuance >= '2020-01-01' and date_of_issuance <= '2021-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2019' as year, count(*) from ph_fda where date_of_issuance >= '2019-01-01' and date_of_issuance <= '2020-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2018' as year, count(*) from ph_fda where date_of_issuance >= '2018-01-01' and date_of_issuance <= '2019-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%'
                            union all
                            select 'ph_fda' as table_name, '2017' as year, count(*) from ph_fda where date_of_issuance >= '2017-01-01' and date_of_issuance <= '2018-01-01' and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%' order by year asc;"""


# new count query functiom for callback
# Functiom that creates a query statement to fetch data from all regs admins into a dataframe
# For use to create a pie chart when "All New Product" option is set for the radio buttons
def get_count_for_callback(date_interval):
    return f'''select 'Malaysia NPRA' as regs_admins, count(*) from npra {date_interval}
                union all
                select 'Singapore HSA' as regs_admins, count(*) from hsa {date_interval}
                union all
                select 'Indonesia HSA' as regs_admins, count(*) from bpom {date_interval}
                union all
                select 'Philippines FDA' as regs_admins, count(*) from ph_fda {date_interval} and classification = 'Prescription Drug (RX)' and application_type like '%%Initial%%';'''
