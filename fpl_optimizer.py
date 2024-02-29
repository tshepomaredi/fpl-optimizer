import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from data_collection import get_player_data
players_df = get_player_data()

# Select relevant features and target variable
features = ['goals_scored', 'assists', 'form', 'clean_sheets',
             'bps', 'expected_goal_involvements']
target = 'points_per_game'

# Drop rows with missing values
players_df.dropna(subset=features + [target], inplace=True)

# Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(players_df[features], players_df[target], test_size=0.1, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
# y_pred = model.predict(X_test)


players_df['predicted_performance'] = model.predict(players_df[features])

# Assuming you have already trained a machine learning model and obtained predictions for player performance

def select_starting_11(players_df, budget_constraint, position_constraints):
    # Sort players by predicted performance (e.g., PPG or total points)
    players_df.sort_values(by='predicted_performance', ascending=False, inplace=True)
    
    # Initialize variables
    selected_team = []
    remaining_budget = budget_constraint
    position_counts = {position: 0 for position in position_constraints.keys()}
    
    # Iterate over sorted players and select the best starting 11 within constraints
    for _, player in players_df.iterrows():
        if player['now_cost'] <= remaining_budget:
            pos_counts = player['element_type']
            pos_consts = player['element_type']
            if position_counts[pos_counts] < position_constraints[pos_consts]:
                selected_team.append(player)
                remaining_budget -= player['now_cost']
                position_counts[player['element_type']] += 1
        
        if len(selected_team) == 11:
            break
    
    return selected_team

# Example usage
budget_constraint = 1000  # Example budget constraint in millions
position_constraints = {1: 1, 2: 4, 3: 4, 4: 2}  # Example position constraints
selected_starting_11 = select_starting_11(players_df, budget_constraint, position_constraints)

def type_to_position(elem_type):
    switch = {
        1 : "GK",
        2 : "DEF",
        3 : "MID",
        4 : "FWD"
    }
    return switch.get(elem_type)

print('Predicted optimal starting XI:')
for player in selected_starting_11:
    print(type_to_position(player['element_type']) + ": " + player['web_name'])