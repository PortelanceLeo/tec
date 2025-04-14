
from pathlib import Path
import urllib.parse
import urllib.request
from enum import Enum

BASE_URL = "https://twtransfer.energytransfer.com/ipost/capacity/operationally-available"
ASSET = "TW"
CYCLES = [i for i in range(5)]
SEARCH_TYPE = "NOM"
LOC_TYPE = "ALL"
LOC_ZONE = "ALL"
CSV_CACHE = Path(Path(__file__).parent,".csv_cache")
TW_TRUE_VALUE = "Y"
TW_FALSE_VALUE = "N"

class IntFields(Enum):
    loc = "loc"
    opc = "opc"
    tsq = "tsq"
    oac = "oac"

class FloatFields(Enum):
    dc = "dc"

class BooleanFields(Enum):
    it = "it"
    auth_overrun_ind = "auth_overrun_ind"
    nom_cap_exceed_ind = "nom_cap_exceed_ind"
    all_qty_avail = "all_qty_avail"

class StringFields(Enum):
    loc_zn = "loc_zn"
    loc_name = "loc_name"
    qty_reason = "qty_reason"

class SizedStringFields(Enum):
    loc_purp_desc = ("loc_purp_desc", 2)
    loc_qti = ("loc_qti", 3)
    flow_ind =("flow_ind", 1)

FIELD_MAPPING = {
            'Loc': IntFields.loc.value,
            'Loc Zn': StringFields.loc_zn.value,
            'Loc Name': StringFields.loc_name.value,
            'Loc Purp Desc': SizedStringFields.loc_purp_desc.value[0],
            'Loc/QTI': SizedStringFields.loc_qti.value[0],
            'Flow Ind': SizedStringFields.flow_ind.value[0],
            'DC' : FloatFields.dc.value,
            'OPC': IntFields.opc.value,
            'TSQ': IntFields.tsq.value,
            'OAC': IntFields.oac.value,
            'IT': BooleanFields.it.value,
            'Auth Overrun Ind': BooleanFields.auth_overrun_ind.value,
            'Nom Cap Exceed Ind': BooleanFields.nom_cap_exceed_ind.value,
            'All Qty Avail': BooleanFields.all_qty_avail.value,
            'Qty Reason': StringFields.qty_reason.value
        }
ALL_FIELDS = [*[f.value for f in BooleanFields],
             *[f.value for f in StringFields],
             *[f.value[0] for f in SizedStringFields],
             *[f.value for f in IntFields],
             *[f.value for f in FloatFields]]

def get_csv_url(gas_day, cycle):
    params = {
        'f': 'csv',
        'extension': 'csv',
        'asset': ASSET,
        'gasDay': gas_day.strftime('%m/%d/%Y'),
        'cycle': cycle,
        'searchType': SEARCH_TYPE,
        'searchString': '',
        'locType': LOC_TYPE,
        'locZone': LOC_ZONE
    }
    query_string = urllib.parse.urlencode(params)
    return f"{BASE_URL}?{query_string}"

def download_csv(url, filename):
    if not CSV_CACHE.exists():
        CSV_CACHE.mkdir()
    file = Path(CSV_CACHE,filename)
    urllib.request.urlretrieve(url,str(file))
    return file