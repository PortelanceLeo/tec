from datetime import datetime,timedelta
import multiprocessing
import numpy as np
import pandas as pd
from data_utils import ALL_FIELDS, FIELD_MAPPING,CYCLES, TW_FALSE_VALUE, TW_TRUE_VALUE, BooleanFields, FloatFields, IntFields, SizedStringFields, StringFields, download_csv, get_csv_url
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
    
    def download_data(date,cycle):
        url = get_csv_url(date,cycle)
        filename = f"tw_oac_{date.strftime('%Y%m%d')}_{cycle}.csv"
        file = download_csv(url,filename)
        return file
    
    def clean_data(file,date,cycle):
        df = pd.read_csv(file).rename(columns=FIELD_MAPPING, 
                                      errors='ignore')
        if df.empty:
            return
        valid_columns = np.array([col for col in ALL_FIELDS if col in df.columns])
        df = df[valid_columns]

        # clean boolean
        boolean_columns = np.array([f.value for f in BooleanFields])
        true_grid_mask = df[boolean_columns] == TW_TRUE_VALUE
        false_grid_mask = df[boolean_columns] == TW_FALSE_VALUE
        invalid_boolean_row_mask = np.all(~true_grid_mask & ~true_grid_mask,axis=1)
        df[true_grid_mask] = True
        df[false_grid_mask] = False

        #clean strings
        string_columns = np.array(([f.value for f in StringFields] + 
                            [f.value[0] for f in SizedStringFields]))
        string_sizes = np.array(([255 for f in StringFields] + 
                            [f.value[1] for f in SizedStringFields]))
        df[string_columns] = df[string_columns].fillna("")
        vectorized_len = np.vectorize(len)
        lengths = vectorized_len(df[string_columns])
        length_grid_mask =  (lengths.T <= np.expand_dims(string_sizes,axis=1)).T
        invalid_string_row_mask = np.all(length_grid_mask,axis=1)

        #clean ints
        int_columns = np.array([f.value for f in IntFields])
        df[int_columns] = df[int_columns].fillna(-1)

        #clean floats
        float_columns = np.array([f.value for f in FloatFields])
        df[float_columns] = df[float_columns].fillna(-1.0)

        #remove invalid rows
        invalid_row_mask = ~(invalid_boolean_row_mask & invalid_string_row_mask)
        df = df[invalid_row_mask]
        return df if not df.empty else None

    def process_data(date,cycle):
        print(f"Downloading data for {date.strftime('%m/%d/%Y')} cycle {cycle}")
        file = download_data(date,cycle)
        print(f"Cleaning data for {date.strftime('%m/%d/%Y')} cycle {cycle}")
        df = clean_data(file,date,cycle)
        if df is not None:
            df['gas_day'] = date
            df['cycle'] = cycle
            return df
        else:
            print(f"No data or invalid data for {date.strftime('%m/%d/%Y')} cycle {cycle}")
            return None

    MAX_PROCESS = 4
    day_count = 3
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=day_count-1)
    dates = pd.date_range(start_date,end_date)
    targets = [(d,c) for d in dates for c in CYCLES]
    with multiprocessing.Pool(processes=MAX_PROCESS) as pool:
        results = pool.starmap(process_data,targets)
    
        
        



