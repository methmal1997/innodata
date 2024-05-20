import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Input, Dense
from keras.models import Model
import tensorflow

# Generate synthetic data
# Example: 1000 samples, each with 100 features
num_samples = 1000
num_features = 100
input_data = np.random.randn(num_samples, num_features)


# Define the autoencoder architecture
input_layer = Input(shape=(num_features,))
encoded_layer = Dense(32, activation='relu')(input_layer)  # Encoding layer with 32 neurons
decoded_layer = Dense(num_features, activation='linear')(encoded_layer)  # Decoding layer

# Create the autoencoder model
autoencoder = Model(input_layer, decoded_layer)


# Compile the model
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Train the autoencoder
autoencoder.fit(input_data, input_data, epochs=50, batch_size=32, shuffle=True)

# Use the trained autoencoder to encode and decode the input data
encoded_data = autoencoder.predict(input_data)

# Visualize or
#
#
# iginal and reconstructed data for a few samples
num_samples_to_visualize = 5

for i in range(num_samples_to_visualize):
    original_sample = input_data[i]
    reconstructed_sample = encoded_data[i]

    plt.figure(figsize=(10, 4))
    plt.subplot(1, 2, 1)
    plt.title('Original Sample')
    plt.plot(original_sample)

    plt.subplot(1, 2, 2)
    plt.title('Reconstructed Sample')
    plt.plot(reconstructed_sample)
    print("Here is my code")
    plt.show()





