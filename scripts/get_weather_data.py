import sys
import pandas as pd
import requests
import json
from tqdm import tqdm
from datetime import datetime

def get_data(url):
    """
    Get data from url and return it as a pandas dataframe
    Args:
        url: url of the data
    Returns:
        weather_data: pandas dataframe
    """

    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        weather_data = data["days"][0]
    
    return weather_data

def prep_data(old_df, column_names):

    """
    Prepares the data for the weather data
    Args:
        old_df: pandas dataframe
    Returns:
        new_df: pandas dataframe
    """

    base_dataset["Date"] = pd.to_datetime(old_df["Date"], format="%m/%d/%Y")

    dates = base_dataset["Date"].tolist()

    dates = [date.strftime("%Y-%m-%d") for date in dates]

    new_df = pd.DataFrame(pd.DataFrame(index=range(len(base_dataset)), columns=column_names))

    new_df['date'] = dates
    
    return new_df

if __name__ == "__main__":
    # Get the data
    api_key = "API_KEY"

    base_data_path = sys.argv[1]

    base_dataset = pd.read_csv(base_data_path)

    column_names = ['tempmax', 'tempmin', 'temp', 'feelslikemax', 'feelslikemin', 'feelslike', 'dew', 'humidity', 'pressure', 'visibility', 'windspeed', 'icon']

    weather_df = prep_data(base_dataset, column_names=column_names)

    for idx, row in tqdm(weather_df.iterrows()):
        date = row["date"]

        url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Durham%2CUS/{date}/{date}?unitGroup=metric&key={api_key}"

        weather_data = get_data(url)

        for column in column_names:
            weather_df.loc[idx, column] = weather_data[column]
    
    weather_df.to_csv(sys.argv[2], index=False)


    

