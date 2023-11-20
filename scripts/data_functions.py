#####
###
# 00 Imports
# 01 Load Data
# 02 Split Data
# 03 Clean Data
# 04 Data Features
# 05 Split Train Test
# 06 Data Pipeline
###
#####




#####
###
# 00 Imports
###
#####
import pandas as pd
import numpy as np




#####
###
# 01 Load Data
###
#####

def load_data():
    """
    Load data from the combined men's football and women's basektball dataset
    Args:
        None
    Returns:
        df: Pandas dataframe
    """

    df = pd.read_csv('data/Merged_V12.csv')

    return df



#####
###
# 02 Split Data
###
#####

def split_data(df):
    """
    Split data into men's football and women's basketball datasets
    Args:
        df: Pandas dataframe
    Returns:
        mf_df: Men's football dataframe
        wm_df: Women's basketball dataframe
    """

    # Split data
    mf_df = df[df['Sport'] == 'MF'].reset_index(drop=True)
    wm_df = df[df['Sport'] == 'WB'].reset_index(drop=True)

    return mf_df, wm_df




#####
###
# 03 Clean Data
###
#####

def clean_data(df):
    """
    Clean data
    Args:
        df: Pandas dataframe
    Returns:
        df: Pandas dataframe
    """
    ###
    # Season
    ###

    # convert season to int
    df['Season'] = np.where(df['Season'] == '2016-2017', '2016', df['Season'])
    df['Season'] = np.where(df['Season'] == '2017-2018', '2017', df['Season'])
    df['Season'] = np.where(df['Season'] == '2018-2019', '2018', df['Season'])
    df['Season'] = np.where(df['Season'] == '2019-2020', '2019', df['Season'])
    df['Season'] = np.where(df['Season'] == '2020-2021', '2020', df['Season'])
    df['Season'] = np.where(df['Season'] == '2021-2022', '2021', df['Season'])
    df['Season'] = np.where(df['Season'] == '2022-2023', '2022', df['Season'])

    # convert season to int
    df['Season'] = df['Season'].astype(int)


    ###
    # Drop Sport
    ###
    
    # drop column
    df.drop(columns=['Sport'], inplace=True)


    ###
    # Game Date
    ###

    # convert game date to datetime
    df['Game_Date'] = pd.to_datetime(df['Date'])

    # create game year
    df['Game_Year'] = df['Game_Date'].dt.year

    # create game month
    df['Game_Month'] = df['Game_Date'].dt.month

    # create game day
    df['Game_Day'] = df['Game_Date'].dt.day

    # create game day of week
    df['Game_Day_Of_Week'] = df['Game_Date'].dt.dayofweek

    # create game quarter
    df['Game_Quarter'] = df['Game_Date'].dt.quarter

    # drop column
    df.drop(columns=['Date'], inplace=True)


    ###
    # Game Time
    ###

    # convert game time to int
    df['Game_Time'] = df['Time'].astype(int)

    # drop column
    df.drop(columns=['Time'], inplace=True)


    ###
    # Opponent
    ###

    # replace opponent
    df["Opponent"] = df["Opponent"].str.replace("NCA&T", "NCA_T")
    df["Opponent"] = df["Opponent"].str.replace("TexasA&M", "TexasA_M")


    ###
    # Drop Duke Record
    ###

    # drop column
    df.drop(columns=['Duke Record'], inplace=True)


    ###
    # Duke W
    ###

    # convert duke w to int
    df['Duke W'] = df['Duke W'].astype(int)

    # rename column
    df.rename(columns={'Duke W': 'Duke_Win'}, inplace=True)


    ###
    # Duke L
    ###

    # convert duke l to int
    df['Duke L'] = df['Duke L'].astype(int)

    # rename column
    df.rename(columns={'Duke L': 'Duke_Loss'}, inplace=True)


    ###
    # Duke Overall W/L
    ###

    # convert duke overall w/l to float
    df['Duke Overall W/L'] = df['Duke Overall W/L'].astype(float)

    # rename column
    df.rename(columns={'Duke Overall W/L': 'Duke_Overall_Win_Loss'}, inplace=True)


    ###
    # Duke Ranking
    ###

    # convert duke rank to int
    df['Duke Ranking'] = df['Duke Ranking'].astype(int)

    # replace 0 with -1
    df['Duke Ranking'] = np.where(df['Duke Ranking'] == 0, -1, df['Duke Ranking'])

    # rename column
    df.rename(columns={'Duke Ranking': 'Duke_Ranking'}, inplace=True)


    ###
    # Opponent Ranking
    ###

    # convert opponent rank to int
    df['Opponent Ranking'] = df['Opponent Ranking'].astype(int)

    # replace 0 with -1
    df['Opponent Ranking'] = np.where(df['Opponent Ranking'] == 0, -1, df['Opponent Ranking'])

    # rename column
    df.rename(columns={'Opponent Ranking': 'Opponent_Ranking'}, inplace=True)


    ###
    # Game W/L
    ###

    # drop column
    df.drop(columns=['Game W/L'], inplace=True)


    ###
    # W/L Margin
    ###

    # drop column
    df.drop(columns=['W/L Margin'], inplace=True)


    ###
    # Attendance
    ###

    # convert attendance to int
    df['Attendance'] = df['Attendance'].astype(int)


    ###
    # Category
    ###

    # rename column
    df.rename(columns={'Category': 'Class_Or_Holiday'}, inplace=True)


    ###
    # tempmax
    ###

    # convert tempmax to float
    df['tempmax'] = df['tempmax'].astype(float)

    # convert degrees celcius to degrees fahrenheit
    df['tempmax'] = df['tempmax'] * 9/5 + 32


    ###
    # tempmin
    ###

    # convert tempmin to float
    df['tempmin'] = df['tempmin'].astype(float)

    # convert degrees celcius to degrees fahrenheit
    df['tempmin'] = df['tempmin'] * 9/5 + 32


    ###
    # temp
    ###

    # convert temp to float
    df['temp'] = df['temp'].astype(float)

    # convert degrees celcius to degrees fahrenheit
    df['temp'] = df['temp'] * 9/5 + 32

    # rename column
    df.rename(columns={'temp': 'tempavg'}, inplace=True)


    ###
    # feelslikemax
    ###

    # convert feelslikemax to float
    df['feelslikemax'] = df['feelslikemax'].astype(float)

    # convert degrees celcius to degrees fahrenheit
    df['feelslikemax'] = df['feelslikemax'] * 9/5 + 32


    ###
    # feelslikemin
    ###

    # convert feelslikemin to float
    df['feelslikemin'] = df['feelslikemin'].astype(float)

    # convert degrees celcius to degrees fahrenheit
    df['feelslikemin'] = df['feelslikemin'] * 9/5 + 32


    ###
    # feelslike
    ###

    # convert feelslike to float
    df['feelslike'] = df['feelslike'].astype(float)

    # convert degrees celcius to degrees fahrenheit
    df['feelslike'] = df['feelslike'] * 9/5 + 32

    # rename column
    df.rename(columns={'feelslike': 'feelslikeavg'}, inplace=True)


    ###
    # dew
    ###

    # convert dew to float
    df['dew'] = df['dew'].astype(float)

    
    ###
    # humidity
    ###

    # convert humidity to float
    df['humidity'] = df['humidity'].astype(float)


    ###
    # pressure
    ###

    # convert pressure to float
    df['pressure'] = df['pressure'].astype(float)


    ###
    # visibility
    ###

    # convert visibility to float
    df['visibility'] = df['visibility'].astype(float)


    ###
    # windspeed
    ###

    # convert windspeed to float
    df['windspeed'] = df['windspeed'].astype(float)


    ###
    # icon
    ###

    # replace values
    df['icon'] = df['icon'].str.replace('clear-day', 'clear_day')
    df['icon'] = df['icon'].str.replace('partly-cloudy-day', 'partly_cloudy_day')

    # rename column
    df.rename(columns={'icon': 'weather'}, inplace=True)


    ###
    # Event Type
    ###

    # rename column
    df.rename(columns={'Event Type': 'Event_Type'}, inplace=True)

    
    ###
    # Day of Week
    ###

    # drop column
    df.drop(columns=['Day of Week'], inplace=True)


    ###
    # Day of Week Str
    ###

    # drop column
    df.drop(columns=['Day of Week Str'], inplace=True)


    ###
    # Return Dataframe
    ###

    return df




#####
###
# 04 Data Features
###
#####

def data_features(df):
    """
    Create data features
    Args:
        df: Pandas dataframe
    Returns:
        df: Pandas dataframe
    """

    ###
    # Opponent
    ###

    # replace opponent
    opponent_dict = {
        'AppalachianState': '1'
        ,'Army': '2'
        ,'AustinPeay': '3'
        ,'Baylor': '4'
        ,'BostonCollege': '5'
        ,'Charlotte': '6'
        ,'CharlestonSouthern': '7'
        ,'Clemson': '8'
        ,'Colorado': '9'
        ,'Davidson': '10'
        ,'EastCarolina': '11'
        ,'Elon': '12'
        ,'FloridaGulfCoast': '13'
        ,'FloridaState': '14'
        ,'GeorgiaTech': '15'
        ,'GrandCanyon': '16'
        ,'Hampton': '17'
        ,'HighPoint': '18'
        ,'IdahoState': '19'
        ,'Iona': '20'
        ,'Iowa': '21'
        ,'Kansas': '22'
        ,'Kentucky': '23'
        ,'Liberty': '24'
        ,'Longwood': '25'
        ,'Louisville': '26'
        ,'Maine': '27'
        ,'Marist': '28'
        ,'Miami': '29'
        ,'NCA_T': '30'
        ,'NCCU': '31'
        ,'NCState': '32'
        ,'NorthCarolina': '33'
        ,'Northwestern': '34'
        ,'NotreDame': '35'
        ,'OhioState': '36'
        ,'OldDominion': '37'
        ,'Oregon': '38'
        ,'OregonState': '39'
        ,'Penn': '40'
        ,'Pittsburgh': '41'
        ,'Presbyterian': '42'
        ,'SouthCarolina': '43'
        ,'Syracuse': '44'
        ,'Temple': '45'
        ,'TexasA_M': '46'
        ,'Troy': '47'
        ,'UNCWilmington': '48'
        ,'UNLV': '49'
        ,'Villanova': '50'
        ,'Virginia': '51'
        ,'VirginiaTech': '52'
        ,'WakeForest': '53'
        ,'Winthrop': '54'
        ,'Wyoming': '55'
    }

    df['Opponent'] = df['Opponent'].map(opponent_dict)

    # convert opponent to int
    df['Opponent'] = df['Opponent'].astype(int)

    # if opponent is only in the dictionary once, then set the value to 0
    value_counts = df['Opponent'].value_counts().to_dict()
    # keep only values that appear once
    value_counts = {k: v for k, v in value_counts.items() if v == 1}
    # put keys in a list
    keys = list(value_counts.keys())
    # replace values
    for key in keys:
        df['Opponent'] = df['Opponent'].replace(key, -1)




    ###
    # Class_Or_Holiday
    ###

    # replace class as 0, holiday as 1
    class_or_holiday_dict = {
        'Class': '0'
        ,'Holiday': '1'
    }

    df['Class_Or_Holiday'] = df['Class_Or_Holiday'].map(class_or_holiday_dict)

    # convert class or holiday to int
    df['Class_Or_Holiday'] = df['Class_Or_Holiday'].astype(int)


    ###
    # Weather
    ###

    # replace weather
    weather_dict = {
        'clear_day': '0'
        ,'partly_cloudy_day': '1'
        ,'cloudy': '2'
        ,'rain': '3'
        ,'snow': '3' # treat like rain due to very few snow days
    }

    df['weather'] = df['weather'].map(weather_dict)

    # convert weather to int
    df['weather'] = df['weather'].astype(int)


    ###
    # Event_Type
    ###

    # replace event type
    event_type_dict = {
        'None': '0'
        ,'ACCRivalry': '1'
        ,'TournamentGame': '2'
    }

    df['Event_Type'] = df['Event_Type'].fillna('None')

    df['Event_Type'] = df['Event_Type'].map(event_type_dict)

    # convert event type to int
    df['Event_Type'] = df['Event_Type'].astype(int)


    ###
    # Return Dataframe
    ###

    return df




#####
###
# 05 Split Train Test
###
#####

def split_train_test(df):
    """
    Split data into train and test datasets
    Args:
        df: Pandas dataframe
    Returns:
        X_train: X train
        X_test: X test
        y_train: y train
        y_test: y test
    """

    # split data
    df_train = df[df['Season'] < 2022].reset_index(drop=True)
    df_test = df[df['Season'] == 2022].reset_index(drop=True)


    return df_train, df_test




#####
###
# 06 Data Pipeline
###
#####

def data_pipeline():
    """
    Run the data pipeline
    Args:
        None
    Returns:
        mf_df: Men's football dataframe
        wm_df: Women's basketball dataframe
    """

    # Load data
    df = load_data()

    # Split data
    mf_df, wm_df = split_data(df)

    # Clean data
    mf_df = clean_data(mf_df)
    wm_df = clean_data(wm_df)

    # Create data features
    mf_df = data_features(mf_df)
    wm_df = data_features(wm_df)

    # Split train test
    mf_train_df, mf_test_df = split_train_test(mf_df)
    wm_train_df, wm_test_df = split_train_test(wm_df)

    return mf_train_df, mf_test_df, wm_train_df, wm_test_df
