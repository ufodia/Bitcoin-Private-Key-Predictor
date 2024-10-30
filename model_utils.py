from tensorflow.keras import layers, models
from data_processing import float_array_to_hex  

def create_model(input_dim, output_dim, first_layer_dim, hidden_layers, hidden_dim):
    sequential_layers = [
        layers.Dense(first_layer_dim, activation='relu', input_shape=(input_dim,))
    ]
    for _ in range(hidden_layers):
        sequential_layers.append(layers.Dense(hidden_dim, activation='relu'))
    sequential_layers.append(layers.Dense(output_dim, activation='tanh'))
    
    model = models.Sequential(sequential_layers)
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model


def save_model(model, file_path):
    model.save(file_path)

def load_model(file_path):
    return models.load_model(file_path)

def create_prediction_file(model, x_data, file_name):
    predictions = model.predict(x_data)
    with open(file_name, 'w') as f:
        for prediction in predictions:
            hex_pred = float_array_to_hex(prediction, 64)  
            f.write(f"{hex_pred}\n")
