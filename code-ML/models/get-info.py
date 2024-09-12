from keras.models import load_model

model_path = './model_20240912-174238.keras'

# Load the model
model = load_model(model_path)

# Output the summary of the model
model.summary()
