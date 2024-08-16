from fastapi import FastAPI,BackgroundTasks,status,HTTPException
from chartink import trasferDataToGoogleSheet
import schemas
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import os
import pandas as pd







app = FastAPI()
origins = ['*']


# #  pasting CORAS CODE #################
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def st():
    return {"Message" : "Hello"}

@app.get('/start')
async def start(background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(trasferDataToGoogleSheet)
    except Exception as e:
        print(f"Exception ----> {e}")
    return{"Message" : 'code run started'}


@app.post('/api/fetchScreener', status_code=status.HTTP_200_OK, response_model=list[schemas.ScreenerDataFetch])
def screenerDataFetch(data: schemas.ScreenerData):
    directory = 'super'
    if not os.path.exists(directory):
        return {"Message": "Data not found"}
    else:
        try:
            file_name = f'{directory}/{data.conditionName}.csv'
            fetch_data = pd.read_csv(file_name)
            result = fetch_data.to_dict(orient="records")  # Convert to list of dictionaries
            return result
        except Exception as e:
            print(f"Exception ----> {e}")
            raise HTTPException(status_code=500, detail="An error occurred while processing the data.")



    

    



