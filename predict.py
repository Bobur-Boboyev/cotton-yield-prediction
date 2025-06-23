import pandas as pd
import pickle

def make_prediction():
    try:
        rain = float(input("Enter rainfall amount (mm): "))
        fert = float(input("Enter fertilizer amount (kg): "))
        seed = float(input("Enter seed quality (1-10): "))
        irrig = int(input("Enter number of irrigations: "))
        land = float(input("Enter land size (hectares): "))
    except ValueError:
        print("\nOnly numbers are allowed.")
        return

    input_data = pd.DataFrame([{
        "rainfall_mm": rain,
        "fertilizer_kg": fert,
        "seed_quality": seed,
        "irrigation_count": irrig,
        "land_hectare": land
    }])

    with open("models/model.pkl", 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(input_data)
    predicted_yield = prediction[0, 0]

    if predicted_yield < 0:
        print("\nPrediction result is negative, likely due to invalid input. Try again.")
        return

    input_data["cotton_prediction"] = round(predicted_yield, 2)
    input_data["status"] = "valid"
    input_data.to_json("logs/user_input.json", orient='records', indent=4)

    print(f"\n✅ Predicted cotton yield: {round(predicted_yield, 2)} tons")
