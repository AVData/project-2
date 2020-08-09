import os
from dotenv import load_dotenv
import pandas as pd
from sodapy import Socrata

load_dotenv(verbose=True)

# Log In site:
# https://data.lacity.org/login

# API documentation
# https://dev.socrata.com/foundry/data.lacity.org/d5tf-ez2w


# How to use this API
MyAppToken = os.getenv('MyAppToken')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')

client = Socrata("data.lacity.org",
                 MyAppToken,
                 username=USERNAME,
                 password=PASSWORD)

results = client.get('d5tf-ez2w', limit=500000)

results_df = pd.DataFrame.from_records(results)

results_df.to_csv('Traffic_Collision_Data_from_API.csv', index=True, header=True)
