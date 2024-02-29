"""
Get the required data from the official Premier League API and return the relevant data frames

written by: Tshepo Maredi
"""

import requests
import pandas as pd

# Define the endpoint for the Premier League API
base_url = "https://fantasy.premierleague.com/api/"

# Define function to fetch data from the API
def get_data(endpoint):
    url = base_url + endpoint
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Failed to retrieve data. Status code:", response.status_code)
        return None


def get_player_data(): 
    # Get general PL data
    general_pl_data = get_data("bootstrap-static/")
    if general_pl_data:
        # Extract required information
        required_info = general_pl_data["elements"]
        # Convert information to DataFrame
        players_df = pd.DataFrame(required_info)
        
    return players_df


def get_team_data():
    general_pl_data = get_data("bootstrap-static/")
    if general_pl_data:
        # Extract required information
        required_info = general_pl_data["teams"]
        # Convert information to DataFrame
        team_df = pd.DataFrame(required_info)
        
    return team_df

def get_season_gameweek_data():
    general_pl_data = get_data("bootstrap-static/")
    if general_pl_data:
        # Extract required information
        required_info = general_pl_data["events"]
        # Convert information to DataFrame
        gameweek_df = pd.DataFrame(required_info)      
    return gameweek_df