import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")

from mlflow.models import validate_serving_input


try:
    model_uri = model_info.mode.uri  # Works if model and validation is in same file
except:
    model_uri = 'runs:/da6e6672e74741d5bc1e12fc24183028/iris_model'

# The model is logged with an input example. MLflow converts
# it into the serving payload format for the deployed model endpoint,
# and saves it to 'serving_input_payload.json'

serving_payload = {
    "inputs": [
        [6.4, 2.8, 5.6, 2.2],
        [6.1, 3.0, 4.6, 1.4],
        [4.9, 3.0, 1.4, 0.2],
        [5.5, 4.2, 1.4, 0.2],
        [5.1, 3.7, 1.5, 0.4],
        [6.6, 3.0, 4.4, 1.4],
        [5.7, 2.8, 4.1, 1.3],
        [5.8, 2.8, 5.1, 2.4],
        [4.9, 2.4, 3.3, 1.0],
        [6.7, 3.3, 5.7, 2.5],
        [4.7, 3.2, 1.3, 0.2],
        [6.9, 3.2, 5.7, 2.3],
        [7.7, 3.8, 6.7, 2.2],
        [6.7, 3.1, 4.7, 1.5],
        [5.5, 3.5, 1.3, 0.2],
        [6.1, 2.8, 4.7, 1.2],
        [4.8, 3.0, 1.4, 0.3],
        [6.3, 3.3, 4.7, 1.6],
        [6.1, 2.8, 4.0, 1.3],
        [6.4, 3.2, 4.5, 1.5],
        [5.0, 3.6, 1.4, 0.2],
        [6.7, 3.1, 4.4, 1.4],
        [6.8, 3.0, 5.5, 2.1],
        [4.6, 3.4, 1.4, 0.3],
        [4.9, 2.5, 4.5, 1.7],
        [4.4, 2.9, 1.4, 0.2],
        [5.1, 2.5, 3.0, 1.1],
        [5.0, 3.4, 1.5, 0.2],
        [6.9, 3.1, 4.9, 1.5],
        [5.5, 2.5, 4.0, 1.3],
        [6.3, 2.7, 4.9, 1.8],
        [5.1, 3.3, 1.7, 0.5],
        [6.7, 3.3, 5.7, 2.1],
        [5.0, 3.3, 1.4, 0.2],
        [5.1, 3.5, 1.4, 0.2],
        [6.0, 3.0, 4.8, 1.8],
        [5.8, 4.0, 1.2, 0.2],
        [4.8, 3.4, 1.9, 0.2],
        [6.2, 2.9, 4.3, 1.3],
        [5.2, 2.7, 3.9, 1.4],
        [5.4, 3.7, 1.5, 0.2],
        [5.4, 3.4, 1.7, 0.2],
        [5.0, 3.2, 1.2, 0.2],
        [5.3, 3.7, 1.5, 0.2],
        [6.5, 3.2, 5.1, 2.0],
        [5.2, 3.5, 1.5, 0.2],
        [5.2, 4.1, 1.5, 0.1],
        [5.7, 3.8, 1.7, 0.3],
        [5.7, 2.6, 3.5, 1.0],
        [4.3, 3.0, 1.1, 0.1],
        [6.9, 3.1, 5.1, 2.3],
        [7.6, 3.0, 6.6, 2.1],
        [5.1, 3.8, 1.9, 0.4],
        [6.8, 3.2, 5.9, 2.3],
        [5.8, 2.6, 4.0, 1.2],
        [7.2, 3.6, 6.1, 2.5],
        [6.1, 2.9, 4.7, 1.4],
        [6.0, 2.2, 4.0, 1.0],
        [5.0, 3.5, 1.6, 0.6],
        [6.1, 2.6, 5.6, 1.4],
        [5.7, 4.4, 1.5, 0.4],
        [4.9, 3.1, 1.5, 0.2],
        [4.4, 3.0, 1.3, 0.2],
        [7.2, 3.0, 5.8, 1.6],
        [6.5, 3.0, 5.8, 2.2],
        [5.8, 2.7, 5.1, 1.9],
        [6.4, 2.9, 4.3, 1.3],
        [4.6, 3.6, 1.0, 0.2],
        [5.6, 2.8, 4.9, 2.0],
        [6.4, 3.2, 5.3, 2.3],
        [6.4, 2.7, 5.3, 1.9],
        [6.3, 2.3, 4.4, 1.3],
        [5.6, 2.9, 3.6, 1.3],
        [6.3, 2.9, 5.6, 1.8],
        [6.5, 3.0, 5.2, 2.0],
        [5.7, 2.5, 5.0, 2.0],
        [6.7, 2.5, 5.8, 1.8],
        [5.8, 2.7, 4.1, 1.0],
        [5.4, 3.0, 4.5, 1.5],
        [5.0, 2.3, 3.3, 1.0],
        [7.3, 2.9, 6.3, 1.8],
        [6.9, 3.1, 5.4, 2.1],
        [6.0, 2.9, 4.5, 1.5],
        [5.9, 3.2, 4.8, 1.8],
        [4.6, 3.1, 1.5, 0.2],
        [5.9, 3.0, 5.1, 1.8],
        [7.2, 3.2, 6.0, 1.8],
        [6.3, 2.5, 4.9, 1.5],
        [5.0, 2.0, 3.5, 1.0],
        [6.6, 2.9, 4.6, 1.3],
        [6.4, 3.1, 5.5, 1.8],
        [6.8, 2.8, 4.8, 1.4],
        [5.2, 3.4, 1.4, 0.2],
        [5.4, 3.4, 1.5, 0.4],
        [6.1, 3.0, 4.9, 1.8],
        [4.8, 3.1, 1.6, 0.2],
        [6.2, 3.4, 5.4, 2.3],
        [6.3, 2.5, 5.0, 1.9],
        [6.7, 3.1, 5.6, 2.4],
        [6.3, 2.8, 5.1, 1.5],
        [5.7, 3.0, 4.2, 1.2],
        [6.3, 3.3, 6.0, 2.5],
        [5.1, 3.5, 1.4, 0.3],
        [4.9, 3.6, 1.4, 0.1],
        [6.0, 2.2, 5.0, 1.5]
    ]
}

# Validate the serving payload works on the model
validate_serving_input(model_uri, serving_payload)

# Validate the serving payload works on the model
output = validate_serving_input(model_uri, serving_payload)

print(output)

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(model_uri)

# Predict on a Pandas DataFrame.
import pandas as pd

serving_payload_parsed = serving_payload
input_df = pd.DataFrame(serving_payload_parsed['inputs'])
output = loaded_model.predict(pd.DataFrame(input_df))
print(output)
