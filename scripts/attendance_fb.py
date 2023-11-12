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
        if count>0:
            break
        game_table = table
        count += 1

    return game_table


def parse(game_table):
    """
    Parse the game table to get the needed information
    Input: game_table
    Output: df
    """
    game_dict = {}
    game_dict["date"] = []
    game_dict["time"] = []
    game_dict["opponent"] = []
    game_dict["site"] = []
    game_dict["tv"] = []
    game_dict["result"] = []
    game_dict["attendance"] = []

    for row in game_table.findAll("tr"):
        cells = row.findAll("td")
        
        if len(cells) == 7:

            game_dict["date"].append(cells[0].find(text=True))
            game_dict["time"].append(cells[1].find(text=True))
            game_dict["opponent"].append(cells[2].find(text=True))
            game_dict["site"].append(cells[3].find(text=True))
            game_dict["tv"].append(cells[4].find(text=True))
            game_dict["result"].append(cells[5].find(text=True))
            game_dict["attendance"].append(cells[6].find(text=True))

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
        if count == 36:
            break
        row = []
        for j in range(len(rows)):
            row.append(rows[j][i])
        df.loc[i] = row
        count += 1

    return df


def clean_dataframe(df):
    """
    Clean the dataframe
    Input: df
    Output: df
    """
    # take out the following characters from each column
    # "*" and "\n"
    df["date"] = df["date"].str.replace("*", "")
    df["date"] = df["date"].str.replace("\n", "")
    df["time"] = df["time"].str.replace("*", "")
    df["time"] = df["time"].str.replace("\n", "")
    df["opponent"] = df["opponent"].str.replace("*", "")
    df["opponent"] = df["opponent"].str.replace("\n", "")
    df["site"] = df["site"].str.replace("*", "")
    df["site"] = df["site"].str.replace("\n", "")
    df["tv"] = df["tv"].str.replace("*", "")
    df["tv"] = df["tv"].str.replace("\n", "")
    df["result"] = df["result"].str.replace("*", "")
    df["result"] = df["result"].str.replace("\n", "")
    df["attendance"] = df["attendance"].str.replace("*", "")
    df["attendance"] = df["attendance"].str.replace("\n", "")

    # convert each column to string
    df["date"] = df["date"].astype(str)
    df["time"] = df["time"].astype(str)
    df["opponent"] = df["opponent"].astype(str)
    df["site"] = df["site"].astype(str)
    df["tv"] = df["tv"].astype(str)
    df["result"] = df["result"].astype(str)
    df["attendance"] = df["attendance"].astype(str)

    # only use standard latin characters and numbers
    df["date"] = df["date"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["time"] = df["time"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["opponent"] = df["opponent"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["site"] = df["site"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["tv"] = df["tv"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["result"] = df["result"].str.encode('ascii', 'ignore').str.decode('ascii')
    df["attendance"] = df["attendance"].str.encode('ascii', 'ignore').str.decode('ascii')   

    return df


if __name__ == "__main__":
    url_list = [
        "https://en.wikipedia.org/wiki/2016_Duke_Blue_Devils_football_team"
        ,"https://en.wikipedia.org/wiki/2017_Duke_Blue_Devils_football_team"
    ]

    year = 2016
    for url in url_list:
        soup = get_soup(url)
        
        game_table = get_game_table(soup)
        game_dict = parse(game_table)
        df = create_dataframe(game_dict)
        df = clean_dataframe(df)

        df.to_csv("C:/Users/JaredBailey/Desktop/Home/Class/510/Project/data/fb_attendance_" + str(year) + "_" + str(year + 1) + ".csv", index=False)
        year += 1
