from train import train_model
from predict import make_prediction
from visualize import visualize_data

def main():
    while True:
        print("\nCotton Yield Prediction System")
        print("-------------------------------")
        print("1 - Train model")
        print("2 - Predict yield")
        print("3 - Visualize data")
        print("0 - Exit")

        choice = input("Enter your choice (0–3): ").strip()

        if choice == '1':
            print("\nTraining the model...")
            train_model()

        elif choice == '2':
            print("\nMaking prediction...")
            make_prediction()

        elif choice == '3':
            print("\nGenerating visualization...")
            visualize_data()

        elif choice == '0':
            print("\nExiting. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 0, 1, 2, or 3.")

if __name__ == "__main__":
    main()
