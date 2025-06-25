import os
import time
import joblib
import pickle
from colorama import Fore, Style
from tensorflow import keras
from src.params import *

def save_model(model=None) -> None:
    """
    Persist trained model locally:
    - Keras → saves as .h5
    - Scikit-learn → saves as .joblib
    """
    if MODEL_TARGET == "local":
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        models_dir = os.path.join(LOCAL_REGISTRY_PATH, "models")
        os.makedirs(models_dir, exist_ok=True)

        if isinstance(model, keras.Model):
            # Save Keras model
            model_path = os.path.join(models_dir, f"{timestamp}.h5")
            model.save(model_path)
            print(Fore.GREEN + "✅ Keras model saved locally" + Style.RESET_ALL)

        else:
            # Save sklearn or other pickle-able models
            model_path = os.path.join(models_dir, f"{timestamp}.joblib")
            joblib.dump(model, model_path)
            print(Fore.GREEN + "✅ Sklearn model saved locally" + Style.RESET_ALL)


    if MODEL_TARGET == "mlflow":
        # mlflow.tensorflow.log_model(
        #     model=model,
        #     artifact_path="model",
        #     registered_model_name=MLFLOW_MODEL_NAME
        # )

        print("✅ Model saved to MLflow")

        return None

    return None


def load_model():
    if MODEL_TARGET == "local":
        models_dir = "models"
        # Load latest sklearn model
        for fname in sorted(os.listdir(models_dir), reverse=True):
            if fname.endswith(".joblib"):
                print("✅ Model loaded from local disk, joblib format")
                return joblib.load(os.path.join(models_dir, fname))
            elif fname.endswith(".h5"):
                print("✅ Model loaded from local disk, Keras format")
                return keras.models.load_model(os.path.join(models_dir, fname))
        raise FileNotFoundError("No model found in models/")


