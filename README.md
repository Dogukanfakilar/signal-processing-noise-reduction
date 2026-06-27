# Signal Processing & Noise Reduction in Python

This project demonstrates digital signal processing (DSP) and data smoothing techniques using Python. It simulates a real-world engineering scenario where raw sensor data is corrupted by environmental noise and needs to be cleaned for further data analysis or machine learning models.

## Key Features
- **Signal Simulation:** Generates a clean synthetic sine wave and corrupts it using random Gaussian noise.
- **Data Filtering:** Implements a Moving Average Filter utilizing NumPy's convolution techniques to eliminate high-frequency noise.
- **Statistical Analytics:** Computes Mean Absolute Error (MAE) metrics to quantify the efficiency of the noise reduction algorithm.

## Technologies Used
- Python 3
- NumPy (Data manipulation and matrix operations)
- Matplotlib (Data visualization setup)

## Performance Results
The implemented moving average filter successfully eliminates a significant portion of the random noise, reducing the Mean Absolute Error (MAE) relative to the clean signal by over 50%.
