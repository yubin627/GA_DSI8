# Project 2 - Ames Housing Data and Kaggle Challenge


**Approach**
Applied Linear Regression without Regularization, Ridge, Lasso and Elastic Net models on the dataset and explored the best performing ones.


**Summary**

|Model|R2 (train)|R2 (test)|RMSE (USD)|
|:--- | --- | --- | --- | 
|OLS (no regularization)|0.944| -4.17e+20|8.48X10^9|
|Ridge (L2 penalty)|0.941|0.913|0.120|
|Lasso (L1 penalty)|0.929|0.906|0.122|
|Elastic Net|0.935|0.911|0.124|

In general, with regularization and hyperparameter tuning, we are able to achieve an RMSE of about ~0.12 USD for our model. All the three models (Ridge, Lasso and Elastic Net) are consistent in identifying the top correlated features, namely: how well the property can function, the ground living area, how recent the property was built and the overall material and finish quality.


After reviewing all the models evaluated so far, I will proceed with the Ridge and Elastic Net models for submission of the kaggle challenge.

**Caveat:**
- Although the RMSE may look reasonably good, the model has its own limitation. It might not be able to produce a good fit for housing properties of rare type such as those with pools or those in agricultural zones. Recall that we have removed a few features due to limited samples in certain categories, e.g. pool_area was removed as only less than 4% of the properties have pools.
- The model still has room for further improvement if domain expert could step in during the feature selection/engineering stage. For example, there are 28 categories in the 'neighorhood' feature. It could certainly be refined if we know that if there are ways to group the neighborhood to reduce complexity of the model. 
