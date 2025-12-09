from src.logger import logging
from src.exception import CustomException
import os, sys
import pickle
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, precision_recall_curve, precision_score, recall_score
from sklearn.model_selection import GridSearchCV



def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)

def load_object(file_path):
    try:
        with open(file_path, 'rb') as file_objt:
            return pickle.load(file_objt)
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}

        for model_name, model in models.items():

            # Get parameters for this specific model
            param_grid = params[model_name]

            # Grid Search
            gs = GridSearchCV(model, param_grid, cv=5)
            gs.fit(X_train, y_train)

            # Set best params
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)

            # Prediction & Accuracy
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)

            # Save result using model name as key
            report[model_name] = acc

        return report

    except Exception as e:
        raise CustomException(e, sys)



