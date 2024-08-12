import joblib

def predict(data): 
    clf = joblib.load("logistic_regression_model.pkl")

    return clf.predict(data)