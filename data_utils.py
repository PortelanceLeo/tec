
from pathlib import Path
import urllib.parse
import urllib.request


BASE_URL = "https://twtransfer.energytransfer.com/ipost/capacity/operationally-available"
ASSET = "TW"
CYCLE_COUNT = 5
SEARCH_TYPE = "NOM"
LOC_TYPE = "ALL"
LOC_ZONE = "ALL"
CSV_CACHE = Path(Path(__file__).parent,".csv_cache")

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