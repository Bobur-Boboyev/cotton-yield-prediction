import pandas as pd
import matplotlib.pyplot as plt
from train import data

user_input = pd.read_json("logs/user_input.json")
land = user_input[["land_hectare"]]
prediction = user_input[["cotton_prediction"]]

area = data[["land_hectare"]]
cotton_yield = data[["total_yield_ton"]]

def visualize_data():
    plt.figure(figsize=(12, 6))
    plt.scatter(area, cotton_yield,color='green', alpha=0.7, marker='x', label="Actual yield")
    plt.scatter(land, prediction, label="Prediction")
    plt.title("land area and cotton yield", size=15)
    plt.xlabel("Land area (hectares)", size=12)
    plt.ylabel("total yield (tons)", size = 12)
    plt.grid(True)
    plt.legend()
    plt.savefig("visualizations/cotton.png")
    plt.show()