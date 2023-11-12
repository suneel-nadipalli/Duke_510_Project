import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import requests
import regex as re

def get_soup(url):
    """
    Get the soup of a url
    Input: url
    Output: soup
    """
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


def get_game_table(soup):
    """
    Get the game table from the wikipedia page
    Input: soup
    Output: game_table
    """
    tables = soup.findAll("table", attrs={"class":"wikitable"})

    # throw away first table, keep the second table
    count = 0
    for table in tables:
        if count==0:
            count += 1
            continue
        game_table = table
        count += 1

    return game_table


def parse(game_table):
    """
    Parse the game table to get the needed information
    Input: game_table
    Output: df
    """

    # for each table row <tr>, get each table data <td> and append to list called "cells"
    rows = game_table.findAll('tr')
    cells = []
    for row in rows:
        if row.find('td'):
            cells.append(row.findAll('td'))

    # set columns in dictionary
    game_dict = {}
    game_dict["Date time, TV"] = []
    game_dict["Rank"] = []
    game_dict["Opponent"] = []
    game_dict["Result"] = []
    game_dict["Record"] = []
    game_dict["Site"] = []

    # append rows to dictionary values
    for row in cells:
        try:
            # append to value list
            game_dict["Date time, TV"].append(row[0].text)
            game_dict["Rank"].append(row[1].text)
            game_dict["Opponent"].append(row[2].text)
            game_dict["Result"].append(row[3].text)
            game_dict["Record"].append(row[4].text)
            game_dict["Site"].append(row[8].text)
        except:
            pass

    return game_dict


def create_dataframe(game_dict):
    """
    Create a dataframe from the game dictionary
    Input: game_dict
    Output: df
    """
    # loop through dictionary and make a list of column names
    col_names = []
    rows = []
    for key, value in game_dict.items():
        col_names.append(key)
        rows.append(value)

    # create dataframe of col_names
    df = pd.DataFrame(columns=col_names)

    # loop through lists and form rows
    count = 1
    for i in range(len(rows[0])):
        try:
            row = []
            for j in range(len(rows)):
                row.append(rows[j][i])
            df.loc[i] = row
            count += 1
        except:
            pass

    return df


def clean_dataframe(df):
    """
    Clean the dataframe
    Input: df
    Output: df
    """
    # take out the following characters from each column
    # "*" and "\n"
    df["Date time, TV"] = df["Date time, TV"].str.replace("*", "")
    df["Date time, TV"] = df["Date time, TV"].str.replace("\n", "")
    df["Rank"] = df["Rank"].str.replace("\n", "")
    df["Opponent"] = df["Opponent"].str.replace("\n", "")
    df["Result"] = df["Result"].str.replace("\n", "")
    df["Record"] = df["Record"].str.replace("\n", "")
    df["Site"] = df["Site"].str.replace("\n", "")

    # convert each column to string
    df["Date time, TV"] = df["Date time, TV"].astype(str)
    df["Rank"] = df["Rank"].astype(str)
    df["Opponent"] = df["Opponent"].astype(str)
    df["Result"] = df["Result"].astype(str)
    df["Record"] = df["Record"].astype(str)
    df["Site"] = df["Site"].astype(str)

    # only use standard latin characters and numbers
    df["Date time, TV"] = df["Date time, TV"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["Rank"] = df["Rank"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["Opponent"] = df["Opponent"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["Result"] = df["Result"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["Record"] = df["Record"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["Site"] = df["Site"].str.encode('ascii', 'ignore').str.decode('ascii')

    return df


if __name__ == "__main__":
    url_list = [
        "https://en.wikipedia.org/wiki/2016%E2%80%9317_Duke_Blue_Devils_women%27s_basketball_team"
        ,"https://en.wikipedia.org/wiki/2017%E2%80%9318_Duke_Blue_Devils_women%27s_basketball_team"
        ,"https://en.wikipedia.org/wiki/2018%E2%80%9319_Duke_Blue_Devils_women%27s_basketball_team"
        ,"https://en.wikipedia.org/wiki/2019%E2%80%9320_Duke_Blue_Devils_women%27s_basketball_team"
    ]

    year = 2016
    for url in url_list:
        soup = get_soup(url)
        
        game_table = get_game_table(soup)
        game_dict = parse(game_table)
        df = create_dataframe(game_dict)
        df = clean_dataframe(df)

        df.to_csv("C:/Users/JaredBailey/Desktop/Home/Class/510/Project/data/wb_attendance_" + str(year) + "_" + str(year + 1) + ".csv", index=False)
        year += 1

