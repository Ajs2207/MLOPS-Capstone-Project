# register_model.py - Fixed for MLflow 3.11.1
import json
import mlflow
import logging
from src.logger import logging
import os
import dagshub

import warnings
warnings.simplefilter("ignore", UserWarning)
warnings.filterwarnings("ignore")

# Setup tracking
mlflow.set_tracking_uri('https://dagshub.com/Ajs2207/MLOPS-Capstone-Project.mlflow')
dagshub.init(repo_owner='Ajs2207', repo_name='MLOPS-Capstone-Project', mlflow=True)

def load_model_info(file_path: str) -> dict:
    """Load the model info from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            model_info = json.load(file)
        logging.debug('Model info loaded from %s', file_path)
        return model_info
    except FileNotFoundError:
        logging.error('File not found: %s', file_path)
        raise
    except Exception as e:
        logging.error('Unexpected error occurred while loading the model info: %s', e)
        raise

def transition_model_stage(model_name: str, version: str, stage: str):
    """Transition a model version to a different stage."""
    try:
        client = mlflow.tracking.MlflowClient()
        
        # Get current model version info - FIXED attribute name
        model_version_details = client.get_model_version(model_name, version)
        
        # In MLflow 3.11.1, use 'current_stage' instead of 'stage'
        print(f"Current stage for {model_name} v{version}: {model_version_details.current_stage}")
        
        # Transition to new stage
        client.transition_model_version_stage(
            name=model_name,
            version=version,
            stage=stage,
            archive_existing_versions=False
        )
        
        logging.info(f'Model {model_name} version {version} transitioned to {stage}.')
        print(f"✅ Model transitioned from '{model_version_details.current_stage}' to '{stage}' stage")
        
    except Exception as e:
        logging.error('Error during model stage transition: %s', e)
        raise

def list_model_versions(model_name: str):
    """List all versions of a model."""
    try:
        client = mlflow.tracking.MlflowClient()
        versions = client.search_model_versions(f"name='{model_name}'")
        
        print(f"\n📦 All versions of '{model_name}':")
        for v in versions:
            print(f"   Version {v.version}: stage={v.current_stage}, run_id={v.run_id[:8]}...")
        
        return versions
    except Exception as e:
        logging.error(f'Error listing model versions: {e}')
        return []

def main():
    try:
        model_info_path = 'reports/experiment_info.json'
        
        # Check if file exists
        if not os.path.exists(model_info_path):
            print(f"⚠️ {model_info_path} not found.")
            print("You can still transition models manually.")
            
            # Allow manual input
            model_name = input("Enter model name (default: my_model): ").strip() or "my_model"
            
            # List existing versions first
            list_model_versions(model_name)
            
            version = input("Enter model version: ").strip()
            stage = input("Enter target stage (Staging/Production/Archived): ").strip()
            
            if not version or not stage:
                print("❌ Version and stage are required")
                return
                
            transition_model_stage(model_name, version, stage)
        else:
            model_info = load_model_info(model_info_path)
            print(f"Loaded model info: {model_info}")
            
            # Use model info from evaluation
            model_name = model_info.get('model_name', 'my_model')
            version = model_info.get('model_version')
            
            if not version:
                print("❌ No model version found in experiment_info.json")
                return
            
            # Show current versions before transitioning
            list_model_versions(model_name)
            
            # Ask what stage to transition to (since it might already be in Staging)
            current_stage = None
            client = mlflow.tracking.MlflowClient()
            try:
                model_details = client.get_model_version(model_name, str(version))
                current_stage = model_details.current_stage
                print(f"\n📌 Current stage for version {version}: {current_stage}")
            except:
                pass
            
            if current_stage == "Staging":
                print(f"\n✅ Model {model_name} version {version} is in Staging stage!")
            # else:
            #     stage = input(f"Enter target stage for version {version} (Staging/Production/Archived): ").strip()
            #     if stage:
            #         transition_model_stage(model_name, str(version), stage)
            #     else:
            #         print("No stage specified. No changes made.")
        
    except Exception as e:
        logging.error('Failed to complete the model registration process: %s', e)
        print(f"Error: {e}")

if __name__ == '__main__':
    main()