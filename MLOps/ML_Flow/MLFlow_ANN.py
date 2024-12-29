import keras
import numpy as np
import pandas as pd
from hyperopt import STATUS_OK,Trials,fmin,hp,tpe
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

import mlflow
from mlflow.models import infer_signature


data = pd.read_csv("data/winequality-white.csv",sep=',')
data.head()

def X_y(data):
    X = data.drop(['quality'],axis =1).values
    y = data['quality'].to_numpy()

    return X,y

train,test = train_test_split(data,test_size=0.3,random_state=42)
X_test, y_test = X_y(train)

train,validate = train_test_split(train,test_size=0.2,random_state=42)
X_train, y_train = X_y(train)
X_validate, y_validate = X_y(validate)
X_train.shape
signature = infer_signature(X_train, y_train)

# ANN compile

def train_model(params,epochs,train_x,train_y,valid_x,valid_y,test_x,test_y):
    mean = np.mean(train_x,axis=0)
    var = np.var(train_x,axis=0)

    model = keras.Sequential(
        [
            keras.Input([train_x.shape[1]]),
            keras.layers.Normalization(mean=mean,variance=var),
            keras.layers.Dense(64, activation = 'relu'),
            keras.layers.Dense(1)

        ]
    )

    model.compile(optimizer = keras.optimizers.SGD(
        learning_rate=params["lr"],momentum=params["momentum"]),
        loss = "mean_squared_error",
        metrics=[keras.metrics.RootMeanSquaredError()]
    )

    with mlflow.start_run(nested=True):
        model.fit(train_x,train_y,validation_data=(valid_x,valid_y),
            epochs=epochs,
            batch_size=64)

        eval_result = model.evaluate(valid_x,valid_y,batch_size=64)

        eval_rmse = eval_result[1]

        # log parameters and metrics

        mlflow.log_params(params)
        mlflow.log_metric("eval_rmse",eval_rmse)

        # log the model

        mlflow.tensorflow.log_model(model,"model",signature=signature)

        return {"loss":eval_rmse, "status": STATUS_OK, "model":model}

def objective(params):
    result = train_model(
        params,
        epochs = 3,
        train_x = X_train,
        train_y = y_train,
        valid_x = X_validate,
        valid_y = y_validate,
        test_x = X_test,
        test_y = y_test
    )

    return result

space = {
    "lr":hp.loguniform("lr",np.log(1e-5),np.log(1e-1)),
    "momentum":hp.uniform("momentum",0.0,1.0)
}

mlflow.set_experiment("Wine Quality ANN Model")

with mlflow.start_run():
    trials = Trials()
    best = fmin(
        fn=objective,
        space=space,
        algo=tpe.suggest,
        max_evals=4,
        trials=trials
    )

    best_run = sorted(trials.results,key=lambda x: x["loss"])[0]
    # Log the best parameters, loss, and model
    mlflow.log_params(best)
    mlflow.log_metric("eval_rmse", best_run["loss"])
    mlflow.tensorflow.log_model(best_run["model"], "model", signature=signature)

    # Print out the best parameters and corresponding loss
    print(f"Best parameters: {best}")
    print(f"Best eval rmse: {best_run['loss']}")
