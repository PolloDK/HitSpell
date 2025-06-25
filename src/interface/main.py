import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from src.model.registry import save_model


def train_model():
    df = pd.read_csv("titanic_data/train.csv")
    df = df[["Pclass", "Sex", "Age", "Fare", "Survived"]].dropna()
    X = df[["Pclass", "Sex", "Age", "Fare"]]
    y = df["Survived"]
    model = RandomForestClassifier()
    model.fit(X, y)
    save_model(model=model)
    return model

if __name__ == '__main__':
    train_model()
