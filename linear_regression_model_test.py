"""
Testing the model here. Print the results and plot the coefficients of the linear regression
to further analyze each feature and its effect/importance

written by: Tshepo Maredi
"""
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
y_pred = model.predict(X_test)

# Evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("Mean Squared Error:", mse)
print("R-squared Score:", r2)

# Print the coefficients of the linear regression model
coefficients = pd.DataFrame({'feature': features, 'coefficient': model.coef_})
print("\nCoefficients:")
print(coefficients)

import matplotlib.pyplot as plt
# Visualize feature importance
plt.figure(figsize=(10, 6))
plt.barh(features, model.coef_)
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.title('Feature Importance')
plt.show()