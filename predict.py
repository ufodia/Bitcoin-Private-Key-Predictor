from model_utils import load_model, create_prediction_file
import data_processing
from data_processing import float_array_to_hex

def generate_predictions(file_name, output_file):
    
    target_pubkey_hex = "02145d2611c823a396ef6712ce0f712f09b9b4f3135e3e0aa3230fb9b6d08d1e35"[:64]
    
    
    target_pubkey_int = int(target_pubkey_hex, 16)
    target_pubkey_binary = data_processing.convert_to_binary(target_pubkey_int, 256)
    target_pubkey_f32 = data_processing.bin_array_to_float32([target_pubkey_binary])

    model = load_model(file_name)
    predictions = model.predict(target_pubkey_f32)

    
    with open(output_file, 'w') as f:
        for prediction in predictions:
            hex_pred = float_array_to_hex(prediction, 64)  
            f.write(f"{hex_pred}\n")

if __name__ == "__main__":
    file_name = "prediction_model.keras"
    output_file = "predictions.txt"
    generate_predictions(file_name, output_file)
