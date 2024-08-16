import time
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from google_sheet import clean_up, update_cell, update_google_sheet
from nse_data import updatenseIndex,maketStatus,marketAdvacneDecline
from back_end_chart_ink import chartinkLogicBankend




def trasferDataToGoogleSheet():

    URL = 'https://chartink.com/screener/process'

    # Initialize prev_data as None before the loop
    print("started")
    count = 0
    while True:

        market = maketStatus()
       
        updatenseIndex()
        marketAdvacneDecline()
 
        try:
            title = "Compounding Funda"
            sub_title = "powered by SnT Solution - 8080105062"
            update_cell(cell='A3',data=title,sheetname='DashBoard')
            update_cell(cell='A200',data=sub_title,sheetname='DashBoard')
            # Condtion 1
            conditionName = "SUPER HERO ADVANCE" # change name Here
            conditionNameLocation = "A4"
            # Put condition here
            # CONDITION1 = {'scan_clause': '( {cash} ( ( {cash} ( latest close >= latest ema( latest close , 20 ) and 1 day ago close < latest ema( latest close , 20 ) and latest volume > 1 day ago volume and latest rsi( 14 ) > 50 ) ) ) ) '}
            CONDITION1 = {"scan_clause": "( {cash} ( ( {cash} ( ( {cash} ( latest rsi( 14 ) >= latest sma( latest rsi( 14 ) , 9 ) and 1 day ago rsi( 14 ) <= 1 day ago sma( 1 day ago rsi( 14 ) , 9 ) and weekly cci( 20 ) >= -200 and latest low <= latest ema( latest close , 20 ) and latest close > latest ema( latest close , 20 ) and latest rsi( 14 ) > 40 and weekly rsi( 14 ) >= 50 and monthly rsi( 14 ) >= 50 and market cap > 500 and latest cci( 20 ) >= 1 day ago cci( 20 ) ) ) or( {cash} ( latest rsi( 14 ) >= latest sma( latest rsi( 14 ) , 9 ) and 1 day ago rsi( 14 ) <= 1 day ago sma( 1 day ago rsi( 14 ) , 9 ) and weekly cci( 20 ) >= -200 and latest low <= latest ema( latest close , 50 ) and latest close > latest ema( latest close , 50 ) and latest rsi( 14 ) > 40 and weekly rsi( 14 ) >= 50 and monthly rsi( 14 ) >= 50 and market cap > 500 and latest cci( 20 ) >= 1 day ago cci( 20 ) ) ) or( {cash} ( latest rsi( 14 ) >= latest sma( latest rsi( 14 ) , 9 ) and 1 day ago rsi( 14 ) <= 1 day ago sma( 1 day ago rsi( 14 ) , 9 ) and weekly cci( 20 ) >= -200 and latest low <= latest ema( latest close , 200 ) and latest close > latest ema( latest close , 200 ) and latest rsi( 14 ) > 40 and weekly rsi( 14 ) >= 50 and monthly rsi( 14 ) >= 50 and market cap > 500 and latest cci( 20 ) >= 1 day ago cci( 20 ) ) ) or( {cash} ( latest rsi( 14 ) >= latest sma( latest rsi( 14 ) , 9 ) and 1 day ago rsi( 14 ) <= 1 day ago sma( 1 day ago rsi( 14 ) , 9 ) and weekly cci( 20 ) >= -200 and latest low <= latest ema( latest close , 100 ) and latest close > latest ema( latest close , 100 ) and latest rsi( 14 ) > 40 and weekly rsi( 14 ) >= 50 and monthly rsi( 14 ) >= 50 and market cap > 500 and latest cci( 20 ) >= 1 day ago cci( 20 ) ) ) or( {cash} ( latest rsi( 14 ) >= latest sma( latest rsi( 14 ) , 9 ) and 1 day ago rsi( 14 ) <= 1 day ago sma( 1 day ago rsi( 14 ) , 9 ) and weekly cci( 20 ) >= -200 and latest low <= latest ema( latest close , 13 ) and latest close > latest ema( latest close , 13 ) and latest rsi( 14 ) > 40 and weekly rsi( 14 ) >= 50 and monthly rsi( 14 ) >= 50 and market cap > 500 and latest cci( 20 ) >= 1 day ago cci( 20 ) ) ) or( {cash} ( latest rsi( 14 ) >= latest sma( latest rsi( 14 ) , 9 ) and 1 day ago rsi( 14 ) <= 1 day ago sma( 1 day ago rsi( 14 ) , 9 ) and weekly cci( 20 ) >= -200 and latest low <= latest ema( latest close , 5 ) and latest close > latest ema( latest close , 5 ) and latest rsi( 14 ) > 40 and weekly rsi( 14 ) >= 50 and monthly rsi( 14 ) >= 50 and market cap > 500 and latest cci( 20 ) >= 1 day ago cci( 20 ) ) ) ) ) ) )"}
            # 
            row_to_start ='A3'
            row_to_clean = 'A3:D'
            chartinkLogicBankend(condition=CONDITION1,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 2
        try:
            # Condtion 2
            conditionName = "SUPER HERO BULLISH CROSSOVER" # change name Here
           
            CONDITION2 = {"scan_clause": "( {cash} ( ( {cash} ( latest macd line( 13 , 8 , 5 ) > latest macd signal( 13 , 8 , 5 ) and 1 day ago  macd line( 13 , 8 , 5 ) <= 1 day ago  macd signal( 13 , 8 , 5 ) and 1 day ago macd line( 13 , 8 , 5 ) < 1 day ago macd signal( 13 , 8 , 5 ) and latest rsi( 14 ) >= 40 and latest volume >= latest sma( latest volume , 20 ) and market cap >= 500 ) ) ) ) "}
            row_to_start ='F3'
            row_to_clean = "F3:I"
            conditionNameLocation = "E4"
            chartinkLogicBankend(condition=CONDITION2,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 3        
        try:
            # condition 3
            conditionName = "SUPER HERO REVERSAL"
            CONDITION3 = {'scan_clause': '( {cash} ( ( {57960} ( latest close >= latest sma( latest close , 200 ) and latest rsi( 2 ) <= 10 and latest close <= latest lower bollinger band( 20 , 2 ) and latest williams %r( 14 ) <= -90 ) ) ) ) '}
            row_to_start ='k3'
            row_to_clean = "k3:N"
            conditionNameLocation = "I4"
            chartinkLogicBankend(condition=CONDITION3,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 4    
        try:
            # condition 4
            conditionName = "SUPER HERO BOTTOM SUPPORT"
            CONDITION4 = {"scan_clause": "( {cash} ( ( {57960} ( ( {57960} ( latest close > latest sma( latest close , 200 ) and latest close >= latest sma( latest vwap , 200 ) and 1 day ago close < latest sma( latest close , 200 ) and 2 days ago close < latest sma( latest close , 200 ) and 3 days ago close < latest sma( latest close , 200 ) and 4 days ago close < latest sma( latest close , 200 ) and latest volume >= 200000 and latest close >= 20 and latest obv >= latest sma( latest obv , 21 ) ) ) or( {57960} ( latest close < latest sma( latest close , 200 ) and 1 day ago close > latest sma( latest close , 200 ) and 2 days ago close > latest sma( latest close , 200 ) and 3 days ago close > latest sma( latest close , 200 ) and 4 days ago close > latest sma( latest close , 200 ) and latest volume >= 200000 and latest close >= 20 and latest obv <= latest sma( latest obv , 21 ) ) ) ) ) ) )"}
            row_to_start ='P3'
            row_to_clean = "P3:S"
            conditionNameLocation = "M4"
            chartinkLogicBankend(condition=CONDITION4,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e) 
        # Condtion 5    - Stopped by User
        try:
            # condition 5
            conditionName = "SUPER HERO PULL BACK"
            CONDITION5 = {"scan_clause": "( {57960} ( monthly rsi( 14 ) >= 60 and weekly rsi( 14 ) >= 60 and latest rsi( 14 ) >= 40 and latest rsi( 14 ) <= 45 ) )"}
            row_to_start ='U3'
            row_to_clean = "U3:X"
            conditionNameLocation = "Q4"
            chartinkLogicBankend(condition=CONDITION5,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        except Exception as e:
            print(e)
        # Condtion 6    - Stopped by User
        # try:
        #     # condition 6
        #     # conditionName = "MOMENTUM BUY"  - to be change on 20.3.2024
        #     conditionName = "200 MA SUPPORT DAILY"
        #     CONDITION6 = {"scan_clause": "( {cash} ( ( {57960} ( ( {57960} ( latest close > latest sma( latest close , 200 ) and latest close >= latest sma( latest vwap , 200 ) and 1 day ago close < latest sma( latest close , 200 ) and 2 days ago close < latest sma( latest close , 200 ) and 3 days ago close < latest sma( latest close , 200 ) and 4 days ago close < latest sma( latest close , 200 ) and latest volume >= 200000 and latest close >= 20 and latest obv >= latest sma( latest obv , 21 ) ) ) or( {57960} ( latest close < latest sma( latest close , 200 ) and 1 day ago close > latest sma( latest close , 200 ) and 2 days ago close > latest sma( latest close , 200 ) and 3 days ago close > latest sma( latest close , 200 ) and 4 days ago close > latest sma( latest close , 200 ) and latest volume >= 200000 and latest close >= 20 and latest obv <= latest sma( latest obv , 21 ) ) ) ) ) ) )"}
        #     row_to_start ='Z3'
        #     row_to_clean = "Z3:AC"
        #     conditionNameLocation = "U4"
        #     chartinkLogicBankend(condition=CONDITION6,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        # except Exception as e:
        #     print(e)
        # Condtion 7    - Stopped by User - to be change on 20.3.2024
        # try:
        #     # condition 
        #     conditionName = "Monthly>60 Weekly>60 Daily 40-45"
        #     CONDITION7 = {"scan_clause": "( {57960} ( monthly rsi( 14 ) >= 60 and weekly rsi( 14 ) >= 60 and latest rsi( 14 ) >= 40 and latest rsi( 14 ) <= 45 ) )"}
        #     row_to_start ='AE3'
        #     row_to_clean = "AE3:AH"
        #     conditionNameLocation = "Y4"
        #     chartinkLogicBankend(condition=CONDITION7,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        # except Exception as e:
        #     print(e)
        # # Condtion 8    - Stopped by User
        # try:
        #     # condition 8
        #     conditionName = "SURPRISE MOVE"
        #     CONDITION8 = {"scan_clause": "( {cash} ( ( {cash} ( latest open > 1 day ago close * 1.03 and latest volume > 1 day ago volume ) ) ) )"}
        #     row_to_start ='AJ3'
        #     row_to_clean = "AJ3:AM"
        #     conditionNameLocation = "N16"
        #     chartinkLogicBankend(condition=CONDITION8,row_to_start=row_to_start,row_to_clean= row_to_clean,sheetname='Hello World',conditionName=conditionName,conditionNameLocation=conditionNameLocation)
        # except Exception as e:
        #     print(e)
        # print(market)    
        if(market == 'Closed' or market == "Close"):
            count +=1
            print(f"Market is {count}<--->{market}")
            return {"Market Status" : f"{market}"}
        else:
            count +=1
            print(f"Market is {count}<--->{market}")
            time.sleep(20) # 300 seconds = 5 minutes
    # Sleep for 5 minutes``
        
    # time.sleep(120) # 300 seconds = 5 minutes
