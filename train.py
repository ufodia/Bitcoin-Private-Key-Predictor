import data_generator
from model_utils import create_model, save_model

def train_model(file_name, train_data_length=10000, seed=1337):
    
    x_train, y_train = data_generator.generate_training_data(train_data_length, seed)[:2]
    
    
    input_dim = 256
    output_dim = 160
    first_layer_dim = 128
    hidden_layers = 20     
    hidden_dim = 512       
    
    
    model = create_model(input_dim, output_dim, first_layer_dim, hidden_layers, hidden_dim)
    
    
    model.compile(optimizer='adam', loss='mean_squared_error')
    
    
    model.fit(x_train, y_train, epochs=5000, batch_size=1024)  
    save_model(model, file_name)
    print(f"Model saved succesfuly to {file_name} ")

if __name__ == "__main__":
    file_name = "prediction_model.keras"
    train_model(file_name)
