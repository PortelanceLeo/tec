from datetime import datetime,timedelta
import multiprocessing
import pandas as pd
from data_utils import CYCLE_COUNT, download_csv, get_csv_url
from db_utils import get_db_connection, create_table, insert_into_table

RANDOM_DATA = {
    'loc': [123, 456],
    'loc_zn': ['A', 'B'],
    'loc_name': ['Test1', 'Test2'],
    'loc_purp_desc': ['X', 'Y'],
    'loc_qti': ['ABC', 'DEF'],
    'flow_ind': ['F', 'R'],
    'dc': [10, 20],
    'opc': [30, 40],
    'tsq': [50, 60],
    'oac': [70, 80],
    'it': [True, False],
    'auth_overrun_ind': [False, True],
    'nom_cap_exceed_ind': [True, False],
    'all_qty_avail': [True, True],
    'qty_reason': ['Reason1', 'Reason2'],
    'gas_day': ['2023-01-01', '2023-01-02'],
    'cycle': [1, 2]
}

if __name__ == "__main__":
    # df = pd.DataFrame(RANDOM_DATA)
    # with get_db_connection() as conn:
    #     create_table(conn)
    #     insert_into_table(conn, df)
    #     with conn.cursor() as cursor:
    #         cursor.execute("SELECT * FROM oac_tw_table")
    #         rows = cursor.fetchall()
    # for row in rows:
    #     print(row)
    
    def process(date,cycle):
        url = get_csv_url(date,cycle)
        filename = f"tw_oac_{date.strftime('%Y%m%d')}_{cycle}.csv"
        file = download_csv(url,filename)
        return file
    
    day_count = 3
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=day_count-1)
    dates = pd.date_range(start_date,end_date)
    targets = [(d,c) for d in dates for c in range(CYCLE_COUNT)]
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.starmap(process,targets)
        
        



