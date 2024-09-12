# PicPredict: Google Quick, Draw Image Recognition

## Overview
This is a machine learning project designed to classify hand-drawn images from Google's Quick, Draw dataset into 15 distinct categories. Utilizing a Convolutional Neural Network (CNN) implemented with TensorFlow and Keras, the model is built to achieve high accuracy in recognizing and categorizing various sketches.

## Features
- **Image Classification:** Recognizes and classifies hand-drawn images into 15 distinct categories such as accessories, fruits, vehicles, and more, leveraging the QuickDraw dataset.
- **Dataset Customization:** Downloads and organizes QuickDraw data into major and minor class structures, enabling flexible dataset management and efficient storage.
- **Model Architecture:** A deep convolutional neural network (CNN) with multiple convolutional layers, pooling layers, and fully connected dense layers, incorporating Batch Normalization and Dropout for improved regularization and performance.
- **Dataset Splitting:** Automatically splits the dataset into training and validation subsets with an 80/20 split ratio for robust model evaluation.
- **TensorBoard Integration:** Tracks and visualizes training and validation metrics, including accuracy and loss, in real time via TensorBoard.
- **Dynamic Image Preprocessing:** Rescales input grayscale images to ensure consistency in pixel value ranges for effective training.
- **Scalable Dataset Management:** Efficiently handles large datasets, organizing them into major classes, automatically creating and managing directories.
- **Optimized Training:** Utilizes Adam optimizer and Sparse Categorical Crossentropy loss for efficient training on multi-class classification tasks.
- **Model Export:** Saves trained models with timestamped filenames, making them ready for future deployment in real-world applications.

## Running Predictions with the Pre-Trained Model

The pre-trained model is saved as `model_20240912-174238.keras`. You can run predictions on sample images by executing the `run.py` script located in the `evaluator-Datathon` directory.

Make sure you have the necessary Python packages installed:
```bash
pip install keras Pillow numpy Flask
```

## Running the Evaluation
The evaluator script used to assess the model's performance was provided by the Datathon organizers as part of the competition framework.

```bash
# Navigate to the evaluator-Datathon directory:
cd evaluator-Datathon

# Run the run.py script to start the evaluation server:
python run.py

# After the server is running, open another terminal window and run Runner.py:
python Runner.py

# Enter the port number when prompted:
Enter your port number: 5555

# The evaluator will now process images and output the results
```

This script will launch a Flask application that serves the evaluator on a local address. By default, it will run on port 5555. Follow the prompts to enter the port number (in this case, 5555) to start the evaluation process. For each image evaluated, the system will output a message indicating the class it guessed and update the score accordingly.
