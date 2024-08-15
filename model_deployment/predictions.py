import joblib

def predict(data): 
    clf = joblib.load("model_deployment/logistic_regression_model.pkl")

    return clf.predict(data)