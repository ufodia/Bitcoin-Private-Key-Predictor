import train
import predict

def main():
    file_name = "prediction_model.keras"
    output_file = "predictions.txt"
    
    
    train.train_model(file_name)
    
    
    predict.generate_predictions(file_name, output_file)

if __name__ == "__main__":
    main()
