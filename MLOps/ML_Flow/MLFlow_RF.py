import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import mean_squared_error, r2_score
from mlflow.models import infer_signature
import pandas as pd

# 1. Experiment setup
experiment_name = "Best RF Model"
mlflow.set_tracking_uri("http://127.0.0.1:5000")  # Or your tracking server URI
mlflow.set_experiment(experiment_name)

# 2. Hyperparameter grid
param_grid = {
    "n_estimators": [50, 100],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5, 10],
}

# 3. Load and preprocess the data
cali_housing = fetch_california_housing(as_frame=True)
X = cali_housing.data
y = cali_housing.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. MLflow run with hyperparameter tuning
with mlflow.start_run():
    # a. Grid search with cross-validation
    rf = RandomForestRegressor(random_state=42)
    grid_search = GridSearchCV(
        rf, param_grid, scoring="neg_mean_squared_error", cv=3, n_jobs=-1, verbose=2
    )
    grid_search.fit(X_train, y_train)

    # b. Log parameters
    # Log best parameters directly
    best_params = grid_search.best_params_
    for param, value in best_params.items():
        mlflow.log_param(f"best_{param}", value)

    mlflow.log_metric("cv_mean_squared_error", -grid_search.best_score_)

    # c. Train best model, log metrics, and model
    best_rf = grid_search.best_estimator_
    y_pred = best_rf.predict(X_test)

    # Create input example (single row)
    input_example = X_train.iloc[[0]]

    # Infer signature using the input example and corresponding prediction
    signature = infer_signature(input_example, y_pred[:1])

    mlflow.sklearn.log_model(
        best_rf,
        "best_rf_model",
        signature=signature,
        input_example=input_example,
    )

    # Evaluate and log test metrics
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    mlflow.log_metric("mse", mse)
    mlflow.log_metric("r2", r2)

    # Log training metrics (using the best model)
    train_predictions = best_rf.predict(X_train)
    train_mse = mean_squared_error(y_train, train_predictions)
    mlflow.log_metric("train_mse", train_mse)

    # Print run information
    print(f"MLflow Run ID: {mlflow.active_run().info.run_id}")
    print(f"Best Parameters: {grid_search.best_params_}")
    print(f"Test MSE: {mse}")
    print(f"Test R-squared: {r2}")
