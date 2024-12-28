import mlflow

try:
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("Getting Started")

    with mlflow.start_run():
        mlflow.log_metric("test", 1)
        mlflow.log_metric("Vara", 2)

except Exception as e:
    print(f"An error occurred: {e}")
