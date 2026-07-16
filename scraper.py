import requests
import pandas as pd
import os
from datetime import datetime

API_KEY = os.environ["bbcda17b-95b1-431b-ace3-c2d98695f3e5"]

CITY = "Jakarta"
STATE = "Jakarta"
COUNTRY = "Indonesia"

url = (
    f"https://api.airvisual.com/v2/city?"
    f"city={CITY}&state={STATE}&country={COUNTRY}&key={API_KEY}"
)

response = requests.get(url)

if response.status_code == 200:

    data = response.json()["data"]

    record = {
        "datetime": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "aqicn": data["current"]["pollution"]["aqicn"],
        "aqius": data["current"]["pollution"]["aqius"],
        "temperature": data["current"]["weather"]["tp"],
        "humidity": data["current"]["weather"]["hu"]
    }

    df = pd.DataFrame([record])

    file = "aqicn.csv"

    if os.path.exists(file):
        df.to_csv(file, mode="a", header=False, index=False)
    else:
        df.to_csv(file, index=False)

    print(df)