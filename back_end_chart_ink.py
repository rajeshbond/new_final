import os
import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import logging


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = 'https://chartink.com/screener/process'

def chartinkLogicBankend(condition, row_to_start, row_to_clean, sheetname, conditionName, conditionNameLocation):
    logging.info(f"Starting process for condition: {conditionName}")
    
    directory = 'super'
    
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    try:
        with requests.Session() as s:
            # Get the CSRF token
            raw_data = s.get(URL)
            soup = bs(raw_data.content, "lxml")
            meta = soup.find('meta', {"name": "csrf-token"})['content']
            header = {"X-Csrf-Token": meta}
            
            # Post the condition to the server
            response = s.post(url=URL, headers=header, data=condition, timeout=10)
            print(response.json())
            if response.content:
                data = response.json()
                stock_list = pd.DataFrame(data['data'])
                
                if stock_list.empty:
                    logging.info(f"No data returned for condition: {conditionName}")
                    df_empty = pd.DataFrame(columns=['nsecode', 'per_chg', 'close', 'volume'])
                    df_empty.to_csv(f'{directory}/{conditionName}.csv', index=False)
                    
              
                    return
                
                # Sort the stock list and save it to a CSV file
                stock_list_sorted = stock_list.sort_values(by='per_chg', ascending=False)
                stock_list_sorted1 = stock_list_sorted[['nsecode', 'per_chg', 'close', 'volume']]
                stock_list_sorted1.to_csv(f'{directory}/{conditionName}.csv', index=False)
                print(f"----------------{conditionName}--------------")
                print(stock_list_sorted1)
                
         
                logging.info(f"Data successfully processed and saved for condition: {conditionName}")
            else:
                logging.info(f"No content returned from server for condition: {conditionName}")
    
    except requests.exceptions.RequestException as req_err:
        logging.error(f"Request error in chartinkLogicBankend: {req_err}")
    except Exception as e:
        logging.error(f"Unexpected error in chartinkLogicBankend: {e}")

