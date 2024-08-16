from jugaad_data.nse import NSELive
import pandas as pd
import time



def updatenseIndex():
    try:
        n = NSELive()
        all_indices = n.all_indices()

        nseData = pd.DataFrame(all_indices['data'])
        columns_to_keep = ['indexSymbol', 'last', 'percentChange']
        columns_to_drop = [col for col in nseData.columns if col not in columns_to_keep]
        nseData.drop(columns=columns_to_drop, inplace=True)
        row_to_start ='A2'
        # print(nseData)
        
    except Exception as e:
        print(f"update_google_sheet nsedata  -------------->>>>{e}")

def maketStatus():
    try:
        n = NSELive()
        status = n.market_status()
        data =status['marketState'][0]['marketStatus']
       
        return data
    except Exception as e:
        print(f"maketStatus  -------------->>>>{e}")
def marketAdvacneDecline():
    try:
        n = NSELive()
        status = n.all_indices()
        data = [status['advances'], status['declines']]
        row_to_start = 'C2'
        time.sleep(0.1)
      
        time.sleep(0.1)
       
    except Exception as e:
        print(f"marketAdvacneDecline  -------------->>>>{e}")

