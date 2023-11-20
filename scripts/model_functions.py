#####
###
# 00 Imports
###
#####



#####
###
# 00 Imports
###
#####
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import LeaveOneOut, RandomizedSearchCV
from sklearn.metrics import mean_squared_error, r2_score




#####
###
# 01 Columns to Model
###
#####

def columns_to_model():
    """
    Create a list of columns to model
    Args:
        df: pandas dataframe
    Returns:
        list of columns to model
    """
    return [
        "Season"
        ,"Opponent"
        ,"Duke_Win"
        ,"Duke_Loss"
        ,"Duke_Overall_Win_Loss"
        ,"Duke_Ranking"
        ,"Opponent_Ranking"
        ,"Class_Or_Holiday"
        ,"tempavg"
        ,"windspeed"
        ,"weather"
        ,"Event_Type"
        ,"Game_Year"
        ,"Game_Month"
        ,"Game_Day_Of_Week"
        ,"Game_Time"
    ]


    

#####
###
# 02 Fit Random Forest Regressor
###
#####

def fit_random_forest_regressor(df, cols):
    """
    Fit a random forest regressor
    Args:
        df: pandas dataframe
        cols: list of columns to model
    Returns:
        random forest regressor
    """

    # instantiate and fit model
    rfr = RandomForestRegressor(random_state=0)

    # leave one out cross validation
    loocv = LeaveOneOut()

    # define random search
    params = {
        'n_estimators': [500, 1000, 1500, 2000],
        'max_depth': [1, 2, 3, 4, 5],
        'min_samples_split': [2, 3, 4, 5],
        'min_samples_leaf': [1, 2, 3, 4, 5],
        'max_features': ['sqrt', 'log2'],
        'n_jobs': [-1]
    }

    # fit model
    rfr = RandomizedSearchCV(
        rfr,
        param_distributions=params,
        cv=loocv,
        n_iter=10,
        n_jobs=-1,
        verbose=1,
        random_state=0
    )

    # fit model
    rfr.fit(df[cols], df['Attendance'])

    # print best parameters
    print("")
    print('Best Parameters:')
    print(rfr.best_params_)
    print("")

    # refit model with best parameters
    rfr = RandomForestRegressor(
        n_estimators=rfr.best_params_['n_estimators'],
        min_samples_split=rfr.best_params_['min_samples_split'],
        min_samples_leaf=rfr.best_params_['min_samples_leaf'],
        max_features=rfr.best_params_['max_features'],
        max_depth=rfr.best_params_['max_depth'],
        random_state=0
    )

    # fit model
    rfr.fit(df[cols], df['Attendance'])


    return rfr




#####
###
# 03 Predict Random Forest Regressor
###
#####

def predict_random_forest_regressor(model, df, cols):
    """
    Predict using a random forest regressor
    Args:
        model: random forest regressor
        df: pandas dataframe
        cols: list of columns to model
    Returns:
        df: pandas dataframe with predictions
    """
    
    # add predictions to dataframe
    df['Predictions'] = model.predict(df[cols])
    
    
    return df




#####
###
# 04 Evaluate Random Forest Regressor
###
#####

def evaluate_random_forest_regressor(model, df):
    """
    Evaluate a random forest regressor
    Args:
        model: random forest regressor
        df: pandas dataframe
        cols: list of columns to model
    Returns:
        None
    """

    # calculate metrics
    mse = mean_squared_error(df['Attendance'], df['Predictions'])
    rmse = np.sqrt(mse)
    r2 = r2_score(df['Attendance'], df['Predictions'])

    # print metrics
    print("")
    print('Mean Squared Error: ', mse)
    print('Root Mean Squared Error: ', rmse)
    print('R Squared: ', r2)
    print("")




#####
###
# 05 Model Pipeline
###
#####

def model_pipeline(train_df, test_df):
    """
    Model pipeline
    Args:
        df: pandas dataframe
    Returns:
        df: pandas dataframe with predictions
    """

    # columns to model
    cols = columns_to_model()

    # fit model
    model = fit_random_forest_regressor(train_df, cols)

    # predict
    df = predict_random_forest_regressor(model, test_df, cols)

    # evaluate
    evaluate_random_forest_regressor(model, test_df)

    return df