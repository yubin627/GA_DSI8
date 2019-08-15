# Project 4: West Nile Virus Prediction
## Group Members: Charles, Chu Hua, Syamil, Yu Bin

---

# Summary

This project has the following objective <br/>(1) we would like to predict the occurence of West Nile virus given certain features.

## Problem Statement
> 1. How can we predict the presence of West Nile virus in an area?


## Executive Summary
We perform data cleaning on the weather features and exploratory data analysis on the spray and distribution of the virus. We then used a variable timelag to impute the weather features on each observation. GridSearch is done on a series of estimators including LogisticRegression and ranked accordingly using the recall score of the minority class (WnvPresent = 1) as the target.

## Conclusions and Recommendations
We decide on extra trees classifier as our best classification model (for Kaggle submission) as it gives us the best ROC AUC score at 0.856.

---

# Outline of Project
Our notebooks are meant to be read in the following order:

|Order|Title|Description|
|---|---|---|
|1.|01_YuBin_weather_data_munging.ipynb|ETL on weather data|
|2.|02_YuBin_weather_data_munging_wetweather.ipynb|Further ETL on weather data|
|3.|03_Syamil_DataTransformation.ipynb|ETL on train, test and spray data|
|4.|04_Modelling.ipynb|Creating a benchmark model for Kaggle submission based on our transformed data|
|5.|05_weather_lag.ipynb|Mapping weather data to different time/date lags|
|6.|06_model_optimization.ipynb|Attempt to find an optimized model with the best parameters|


---
