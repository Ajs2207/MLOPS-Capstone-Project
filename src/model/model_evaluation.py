# model_evaluation.py - Updated for MLflow 3.11.1
import numpy as np
import pandas as pd
import pickle
import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
import logging
import mlflow
import mlflow.sklearn
import dagshub
import os
from src.logger import logging

# Setup tracking
mlflow.set_tracking_uri('https://dagshub.com/Ajs2207/MLOPS-Capstone-Project.mlflow')
dagshub.init(repo_owner='Ajs2207', repo_name='MLOPS-Capstone-Project', mlflow=True)

def load_model(file_path: str):
    """Load the trained model from a file."""
    try:
        with open(file_path, 'rb') as file:
            model = pickle.load(file)
        logging.info('Model loaded from %s', file_path)
        return model
    except FileNotFoundError:
        logging.error('File not found: %s', file_path)
        raise
    except Exception as e:
        logging.error('Unexpected error occurred while loading the model: %s', e)
        raise

def load_data(file_path: str) -> pd.DataFrame:
    """Load data from a CSV file."""
    try:
        df = pd.read_csv(file_path)
        logging.info('Data loaded from %s', file_path)
        return df
    except pd.errors.ParserError as e:
        logging.error('Failed to parse the CSV file: %s', e)
        raise
    except Exception as e:
        logging.error('Unexpected error occurred while loading the data: %s', e)
        raise

def evaluate_model(clf, X_test: np.ndarray, y_test: np.ndarray) -> dict:
    """Evaluate the model and return the evaluation metrics."""
    try:
        y_pred = clf.predict(X_test)
        y_pred_proba = clf.predict_proba(X_test)[:, 1]

        metrics_dict = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'auc': roc_auc_score(y_test, y_pred_proba)
        }
        logging.info('Model evaluation metrics calculated')
        return metrics_dict
    except Exception as e:
        logging.error('Error during model evaluation: %s', e)
        raise

def save_metrics(metrics: dict, file_path: str) -> None:
    """Save the evaluation metrics to a JSON file."""
    try:
        with open(file_path, 'w') as file:
            json.dump(metrics, file, indent=4)
        logging.info('Metrics saved to %s', file_path)
    except Exception as e:
        logging.error('Error occurred while saving the metrics: %s', e)
        raise

def save_model_info(run_id: str, model_name: str, model_version: str, file_path: str) -> None:
    """Save the model run ID, name, and version to a JSON file."""
    try:
        model_info = {
            'run_id': run_id, 
            'model_name': model_name,
            'model_version': model_version,
            'model_uri': f"models:/{model_name}/{model_version}"
        }
        with open(file_path, 'w') as file:
            json.dump(model_info, file, indent=4)
        logging.debug('Model info saved to %s', file_path)
        print(f"✅ Model info saved: {model_info}")
    except Exception as e:
        logging.error('Error occurred while saving the model info: %s', e)
        raise

def main():
    mlflow.set_experiment("my-dvc-pipeline")
    
    with mlflow.start_run() as run:
        try:
            print(f"Starting run: {run.info.run_id}")
            
            # Load model and data
            clf = load_model('./models/model.pkl')
            test_data = load_data('./data/processed/test_bow.csv')
            
            X_test = test_data.iloc[:, :-1].values
            y_test = test_data.iloc[:, -1].values

            # Evaluate
            metrics = evaluate_model(clf, X_test, y_test)
            save_metrics(metrics, 'reports/metrics.json')
            
            # Log metrics to MLflow
            for metric_name, metric_value in metrics.items():
                mlflow.log_metric(metric_name, metric_value)
                print(f"Logged metric: {metric_name} = {metric_value}")
            
            # Log model parameters
            if hasattr(clf, 'get_params'):
                params = clf.get_params()
                # Log only a subset to avoid too many params
                for param_name, param_value in list(params.items())[:10]:
                    mlflow.log_param(param_name, param_value)
            
            # Register the model directly (this is the key change)
            print("Registering model to MLflow Model Registry...")
            model_name = "my_model"
            
            # Log and register the model in one step
            model_info = mlflow.sklearn.log_model(
                sk_model=clf,
                name=model_name,  # This creates the model in the registry
                registered_model_name=model_name
            )
            
            # Get the model version
            client = mlflow.tracking.MlflowClient()
            model_version = client.get_latest_versions(model_name, stages=["None"])[0]
            
            print(f"✅ Model registered successfully!")
            print(f"   Model name: {model_name}")
            print(f"   Model version: {model_version.version}")
            print(f"   Model URI: {model_info.model_uri}")
            
            # Save model info for register_model.py (which we might not even need now)
            save_model_info(
                run.info.run_id, 
                model_name, 
                model_version.version, 
                'reports/experiment_info.json'
            )
            
            # Transition to staging
            client.transition_model_version_stage(
                name=model_name,
                version=model_version.version,
                stage="Staging"
            )
            print(f"✅ Model transitioned to Staging stage")
            
            # Log metrics file as artifact
            mlflow.log_artifact('reports/metrics.json')
            
            print(f"\n🎉 Run completed successfully!")
            print(f"🔗 View run: {mlflow.get_tracking_uri()}/#/experiments/{mlflow.active_run().info.experiment_id}/runs/{run.info.run_id}")
            print(f"📦 Model in Registry: {model_name} version {model_version.version}")
            
        except Exception as e:
            logging.error('Failed to complete the model evaluation process: %s', e)
            print(f"Error: {e}")
            raise

if __name__ == '__main__':
    main()