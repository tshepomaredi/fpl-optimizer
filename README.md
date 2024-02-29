# Fantasy Premier League Optimizer

This repository contains a Python project for optimizing team selection in the Fantasy Premier League (FPL) using machine learning techniques.

## Overview

Fantasy Premier League is a popular fantasy football game where participants build virtual teams of real-life players and earn points based on their performances in actual Premier League matches. This project aims to develop an optimizer to predict player performance and select the best starting 11 players for each gameweek.

## Project Structure

- `data_collection/`: Contains the dataset collection code from the official Premier League API used for training and evaluation.
- `linear_regression_model_test/`: Contains trained machine learning model for predicting player performance.
- `fpl_optimizer/`: Source code for data preprocessing, model training, optimization, and team selection.
- `README.md`: Overview of the project, instructions, and results.

## Data Preprocessing

- Data on player performances, team line-ups, fixtures, and other relevant factors are gathered from the official Premier League API.
- Feature engineering techniques are applied to transform raw data into meaningful features for machine learning models.

## Model Training

- Machine learning models, including linear regression, random forest regression, and gradient boosting regression, are trained to predict player performance metrics such as points per game (PPG) or total points.
- Models are evaluated using cross-validation and various performance metrics such as mean absolute error (MAE), mean squared error (MSE), and R-squared score.

## Optimization

- The team selection problem is formulated as an optimization task to maximize predicted total points while adhering to budget and position constraints.
- Optimization algorithms such as linear programming or heuristic algorithms are applied to search for the optimal solution.

## Results

- The trained linear regression model achieves the following results:
  - Mean Absolute Error: 0.5366
  - Mean Squared Error: 0.4178
  - R-squared Score: 0.8039
- Coefficients of the linear regression model:
  - `goals_scored`: 0.2175
  - `assists`: 0.1227
  - `minutes`: -0.0001
  - `influence`: -0.0013
  - `form`: 0.0335
  - `clean_sheets`: 0.0762
  - `threat`: 0.0004
  - `bps`: 0.0080
  - `ict_index`: -0.0052

## Selected Starting 11

Based on the predictions of player performance, the optimal starting 11 players for the next gameweek are:

- FWD: Watkins
- FWD: Haaland
- MID: Saka
- MID: Salah
- MID: Foden
- MID: Son
- DEF: Trippier
- DEF: Saliba
- DEF: Alexander-Arnold
- DEF: Schär
- GK: Onana

## How to Use

1. Clone this repository to your local machine.
2. Install the required dependencies listed in `requirements.txt`.
3. Run the Python scripts fpl_optimizer.py to preprocess data, train models, perform optimization, and select the best starting 11.


## License

This project is licensed under the MIT License - see the `LICENSE` file for details.

---
