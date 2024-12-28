from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import mlflow
from mlflow.models import infer_signature

X,y = datasets.load_iris(return_X_y=True)
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3)

params = {"penalty": "l2", "solver": "lbfgs", "max_iter": 1000, "multi_class": "auto", "random_state": 8888}

lr = LogisticRegression(**params)
lr.fit(X_train,y_train)

y_pred = lr.predict(X_test)
accuracy = accuracy_score(y_test,y_pred)

# ML Flow Tracking

# ML Flow tracking url
mlflow.set_tracking_uri("http://127.0.0.1:5000")
# Experiment Name
mlflow.set_experiment("First Project")

with mlflow.start_run():
    mlflow.log_params(params) # Log parameters
    mlflow.log_metric("accuracy",accuracy) # Log Metic(s)
    mlflow.set_tag("Basic LR model for Iris Data","Training Info") # Setting tags for filtering

    # Infer the model signature - Info about type and features of Inputs and Outputs
    signature = infer_signature(X_train,lr.predict(X_train))

    # Log the Model
    model_info = mlflow.sklearn.log_model(
        sk_model = lr,
        artifact_path = "iris_model",
        signature = signature,
        input_example = X_train,
        registered_model_name = "First Project"
    )
