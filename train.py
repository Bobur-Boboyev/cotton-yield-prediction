import pandas as  pd
from sklearn.linear_model import LinearRegression
import pickle

data = pd.read_csv("data/cotton.csv")

x = data[['rainfall_mm','fertilizer_kg','seed_quality','irrigation_count','land_hectare']]
y = data[["total_yield_ton"]]

def train_model():
    model = LinearRegression()
    model.fit(x, y)

    with open('models/model.pkl', 'wb') as f:
         pickle.dump(model, f)

    print("\nThe model was successfully trained and saved.")
